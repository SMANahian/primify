from primify.cli import run

def main():
    filename = input("Enter the file name: ")
    max_digits = input("Enter the max digit: ")
    output_file = input("Enter the output file: ")

    if filename == "":
        filename = ".\prime.jpeg"
    if max_digits == "":
        max_digits = "5000"
    if output_file == "":
        output_file = "prime.txt"

    args = ["--image", filename, "--max-digits", max_digits, "--output-file", output_file]
    run(args)

if __name__ == "__main__":
    main()