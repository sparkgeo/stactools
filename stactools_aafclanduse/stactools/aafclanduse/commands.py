from etlcommon.datasets import AAFC_LAND_USE
from etltask.core.cli import create_cli, create_dataset_group
from etltask.aafclanduse.commands.create_items import AafclanduseCreateItemCommand

cli = create_cli()
dataset_cmd = create_dataset_group(AAFC_LAND_USE, cli)

dataset_cmd.add_command(AafclanduseCreateItemCommand.get_command())

def run_cli() -> None:
    cli(prog_name="etltask")


if __name__ == '__main__':
    run_cli()

