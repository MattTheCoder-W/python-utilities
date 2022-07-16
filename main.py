from input.inputs import numeric_input, email_input, confirm_input, not_empty_input


def main():
    print(">> Please import different parts of this project, do not run them directly.")
    print()
    print(">> Performing functions tests")
    print()
    print(">> numeric_input() >>", numeric_input("Enter numeric input: ", None, True))
    print()
    print(">> email_input() >>", email_input("Enter email: "))
    print()
    print(">> confirm_input() >>", confirm_input("Confirm your choice [Y/n]: ", default_value=True))
    print()
    print(">> not_empty_input() >>", not_empty_input("Enter not empty value: "))
    print()
    print(">> All tests complete!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n>> Program stopped!")
        exit(0)
    exit(0)
