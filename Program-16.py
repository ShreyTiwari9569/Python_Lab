
import traceback


class FileProcessingError(Exception):
    pass


class InvalidFormatError(FileProcessingError):
    pass


class InvalidDataError(FileProcessingError):
    pass


def process_file(filename):
    file = None

    try:
        file = open(filename, "r")

        total = 0
        count = 0

        for line_number, line in enumerate(file, start=1):
            line = line.strip()

            if not line:
                continue

            parts = line.split(",")

            if len(parts) != 2:
                raise InvalidFormatError(
                    f"Line {line_number}: Expected name,marks"
                )

            name, marks_text = parts

            try:
                marks = float(marks_text)
            except ValueError:
                raise InvalidDataError(
                    f"Line {line_number}: Marks must be numeric"
                )

            if not name or not 0 <= marks <= 100:
                raise InvalidDataError(
                    f"Line {line_number}: Invalid name or marks"
                )

            print(f"Student: {name}, Marks: {marks}")
            total += marks
            count += 1

    except FileNotFoundError:
        print("Error: File not found.")

    except PermissionError:
        print("Error: Permission denied.")

    except FileProcessingError as error:
        print("Processing Error:", error)
        print("Traceback details:")
        traceback.print_exc()

    except OSError as error:
        print("File system error:", error)
        traceback.print_exc()

    else:
        print("\nFile processed successfully.")
        if count > 0:
            print("Total Students:", count)
            print("Average Marks:", round(total / count, 2))
        else:
            print("No student records found.")

    finally:
        if file is not None:
            file.close()
            print("File closed safely.")


filename = input("Enter filename (e.g., students.txt): ")
process_file(filename)
