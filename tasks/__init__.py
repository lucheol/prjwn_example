import os
import sys

from invoke import task, Collection, call

PROJECT_NAME = os.getenv('PROJECT_NAME', 'project')


def run_command(ctx, cmd, in_container=True):
    if in_container:
        container_id = ctx.run(
            f"docker-compose --project-name {PROJECT_NAME} ps -q django-app-maintenance"
        ).stdout.replace("\n", "")
        if not container_id:
            return print(f"{PROJECT_NAME} is not running!")
        cmd = "docker exec -it {} {}".format(container_id, cmd)
    print(f"Executing raw command: {cmd}")
    if sys.platform == "win32":
        return os.system(cmd)
    return ctx.run(cmd, pty=True)


@task
def kill(ctx):
    """Stop and kill all related containers"""
    run_command(ctx, f"docker-compose --project-name {PROJECT_NAME} kill", in_container=False)


@task(
    kill,
    default=True,
    help={
        "daemon": "Detach containers. Don't show the logs.",
        "debug": "Run stack with PyCharm debug enabled",
        "silk": "Run stack with Silk profile enabled",
        "celery": "Run stack with Celery and PyCharm debug enabled",
    },
)
def run(ctx, daemon=False, debug=False, silk=False, celery=False):
    """Run local stack"""

    pycharm_env = "set DEBUG_PYCHARM=1 && " if sys.platform == "win32" else "DEBUG_PYCHARM=1 "
    silk_env = "set USE_SILK=1 && " if sys.platform == "win32" else "USE_SILK=1 "
    celery_env = "set DEBUG_CELERY=1 && " if sys.platform == "win32" else "DEBUG_CELERY=1 "

    run_command(
        ctx,
        "{}{}{}docker-compose --project-name {} up {}".format(
            pycharm_env if debug or celery else "",
            silk_env if silk else "",
            celery_env if celery else "",
            PROJECT_NAME,
            "-d" if daemon else "",
        ),
        in_container=False,
    )


@task(help={"container": "Container name"})
def logs(ctx, container="django-app"):
    """Show logs for the running container"""
    run_command(
        ctx,
        "docker-compose --project-name {} logs -f {}".format(PROJECT_NAME, container),
        in_container=False,
    )


@task(kill)
def build(ctx):
    """Build local images"""
    run_command(ctx, f"docker-compose --project-name {PROJECT_NAME} build", in_container=False)


@task
def connect(ctx):
    """Execute a instance of bash in the local container django-app"""
    run_command(ctx, "bash")


@task
def shell(ctx):
    """Execute the django shell inside the app container"""
    run_command(ctx, "python manage.py shell_plus --ipython")


@task(help={"check": "Only check the code. Don't make changes"})
def black(ctx, check=False):
    """Execute black against code"""
    run_command(ctx, "black {} .".format("--check" if check else ""))


@task
def flake8(ctx):
    """Execute flake8 against code"""
    run_command(ctx, "flake8 .")


@task
def makemigrations(ctx):
    """Execute makemigrations"""
    run_command(ctx, "python manage.py makemigrations")


@task
def migrate(ctx):
    """Execute migrate"""
    run_command(ctx, "python manage.py migrate")


@task(help={"filename": "Database file name"})
def db_dev_backup(ctx, filename):
    """Create a backup from local database and store into /var/db-backup"""
    run_command(ctx, "python manage.py dbbackup -O /db-backup/{}".format(filename))


@task(help={"filename": "Database file name"})
def db_dev_restore(ctx, filename):
    """Restore a backup from /var/db-backup given a file name"""
    run_command(ctx, "python manage.py dbrestore -I /db-backup/{}".format(filename))


@task(post=[migrate, kill], help={"ignore_system_prune": 'Ignore system prune execution'})
def fresh_restart(ctx, ignore_system_prune=False):
    """Kill, rebuild, update database and run the stack again"""
    run_command(ctx, f"docker-compose --project-name {PROJECT_NAME} kill", in_container=False)
    if not ignore_system_prune:
        run_command(ctx, "docker system prune", in_container=False)
    run_command(ctx, f"docker volume rm -f {PROJECT_NAME}_{PROJECT_NAME}-data", in_container=False)
    run_command(ctx, f"docker-compose --project-name {PROJECT_NAME} build", in_container=False)
    run_command(ctx, f"docker-compose --project-name {PROJECT_NAME} up -d", in_container=False)


ns = Collection()
lint = Collection("lint")
lint.add_task(flake8)
lint.add_task(black)

docker = Collection("docker")
docker.add_task(kill)
docker.add_task(build)
docker.add_task(run)
docker.add_task(logs)
docker.add_task(fresh_restart)
docker.add_task(connect)

django = Collection("django")
django.add_task(makemigrations)
django.add_task(migrate)
django.add_task(shell)

db = Collection("db")
db.add_task(db_dev_backup, "backup")
db.add_task(db_dev_restore, "restore")

ns.add_collection(docker)
ns.add_collection(django)
ns.add_collection(lint)
ns.add_collection(db)
