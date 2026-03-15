import os


def move_file(
        command: str
) -> None:
    """
    Moves a text file from one location to another based on a command.

    Takes a string in the format 'mv source destination.txt', creates the
        necessary folders if they don't exist, copies the contents, and
        deletes the original.

    Args:

        command: A string containing the move instruction.
            Must follow the format "mv <source_file> <destination_file.txt>".
    """
    cmd_parts = command.split()

    if len(cmd_parts) == 3 and cmd_parts[0] == "mv":
        source = cmd_parts[1]
        dest = cmd_parts[2]
        if os.path.exists(source) and dest.endswith(".txt"):
            dest_dir = os.path.dirname(dest)
            if dest_dir and not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            with open(source) as origin, open(dest, "w") as copy:
                for line in origin:
                    copy.write(line)
            os.remove(source)
