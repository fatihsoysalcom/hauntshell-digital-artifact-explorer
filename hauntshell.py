import time
import sys

# --- Simulated "Dead Technologies" (Artifacts) ---
# These represent old data files or system outputs that HauntShell can "revive".

ARTIFACTS = {
    "ancient_log.txt": """
[1988-03-15 09:23:01] System boot sequence initiated.
[1988-03-15 09:23:05] Checking memory... OK (640KB).
[1988-03-15 09:23:10] Loading COMMAND.COM...
[1988-03-15 09:23:12] AUTOEXEC.BAT executed.
[1988-03-15 09:23:15] Path set to C:\\DOS;C:\\UTILS.
[1988-03-15 09:23:18] Starting 'MYAPP.EXE'...
[1988-03-15 09:23:25] MYAPP.EXE terminated with error code 0.
[1988-03-15 09:23:30] User logged off.
""",
    "old_config.ini": """
[SYSTEM]
MODEL=XT-286
CPU_SPEED=12MHz
RAM=1MB
OS=MS-DOS 5.0

[NETWORK]
PROTOCOL=IPX/SPX
NODE_ID=00:C0:FF:EE:00:01
SERVER=FILESERV01

[APPLICATIONS]
DEFAULT_EDITOR=EDIT.COM
DATABASE_PATH=D:\\DATA\\DB.DAT
""",
    "dos_game_score.dat": """
HIGH SCORES FOR SPACE INVADERS (1982)
------------------------------------
1. ZORK      - 15000
2. ATARI     - 12500
3. PONG      - 10000
4. PACMAN    -  8000
5. DIGDUG    -  7500
"""
}

current_artifact_name = None

def type_print(text, delay=0.02):
    """Simulates old terminal typing effect for nostalgic feel."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() # Newline at the end

def show_help():
    """Displays available commands."""
    type_print("\nHauntShell Commands:")
    type_print("  list         - List available 'dead technologies' (artifacts).")
    type_print("  load <name>  - Load a specific artifact by its name (e.g., 'load ancient_log.txt').")
    type_print("  read         - Display the content of the currently loaded artifact.")
    type_print("  clear        - Clear the terminal screen.")
    type_print("  help         - Show this help message.")
    type_print("  exit         - Quit HauntShell.")

def clear_screen():
    """Clears the terminal screen (basic simulation)."""
    print("\n" * 50) # Simulate clear by printing many newlines

def main():
    global current_artifact_name
    type_print("HauntShell v0.1 - Digital Spirit Summoning Session Initiated 👻\n", delay=0.03)
    type_print("Type 'help' for a list of commands.")

    while True:
        try:
            prompt = f"HauntShell:{current_artifact_name or 'NO_ARTIFACT'}> "
            command_line = input(prompt).strip().lower()
            parts = command_line.split(maxsplit=1)
            command = parts[0] if parts else ""
            args = parts[1] if len(parts) > 1 else ""

            if command == "exit":
                type_print("Closing connection to the past. Goodbye!")
                break
            elif command == "help":
                show_help()
            elif command == "list":
                type_print("\nAvailable Digital Artifacts:")
                for name in ARTIFACTS.keys():
                    type_print(f"  - {name}")
            elif command == "load":
                if args in ARTIFACTS:
                    current_artifact_name = args
                    type_print(f"Artifact '{args}' loaded. Ready to read its whispers.")
                else:
                    type_print(f"Error: Artifact '{args}' not found. Use 'list' to see available ones.")
            elif command == "read":
                if current_artifact_name:
                    type_print(f"\n--- Whispers from '{current_artifact_name}' ---\n")
                    # HauntShell concept: Displaying the "dead technology" content
                    type_print(ARTIFACTS[current_artifact_name], delay=0.01)
                    type_print(f"\n--- End of Whispers ---\n")
                else:
                    type_print("No artifact loaded. Use 'load <name>' first.")
            elif command == "clear":
                clear_screen()
            elif command: # If command is not empty but not recognized
                type_print(f"Unknown command: '{command}'. Type 'help' for assistance.")
            else: # If command is empty (just pressed Enter)
                pass # Do nothing, just show prompt again

        except KeyboardInterrupt:
            type_print("\nInterrupted. Closing connection to the past. Goodbye!")
            break
        except Exception as e:
            type_print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
