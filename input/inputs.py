from typing import Union, Optional


def is_float(in_text: str) -> bool:
    """
    Check if given text can be a float.

    Args:
        in_text: Input text.
    """
    try:
        float(in_text)
        return True
    except ValueError:
        return False


def confirm_input(text: str, default_value: Optional[bool] = None) -> bool:
    """
    Get user input in [y/n] format.

    If user answer is not recognized, the prompt for input will be displayed again until valid answer is provided.

    Parameters:
        text (str): Input message.
        default_value (bool, optional): Default value if input not provided.

    Returns:
        bool: User confirmation.
    """
    while True:
        input_text = str(input(text))
        if default_value is not None and not input_text:
            return bool(default_value)
        if input_text.lower() in ['y', 'yes', 'tak']:
            return True
        elif input_text.lower() in ['n', 'no', 'nie']:
            return False
        else:
            print(">> Wrong answer!")


def not_empty_input(text: str) -> str:
    """
    Take user input making sure it is not empty.

    If user input is empty string, input prompt will be displayed again until user specify non-empty value.

    Parameters:
        text (str): Input message.

    Returns:
        str: Not empty user input string.
    """
    while True:
        input_text = str(input(text))
        if input_text:
            return input_text
        else:
            print(">> Please insert value!")


def email_input(text: str, provider: Optional[str] = None) -> str:
    """
    Gets email input from user making sure inserted address is correct.

    Parameters:
        text (str): Input message.
        provider (str, optional): Required email provider domain.

    Returns:
        str: User specified email in correct format.
    """
    while True:
        email_text = not_empty_input(text)
        if email_text.count("@") != 1:
            print(">> Entered email is missing '@' symbol!")
            continue
        name_text, provider_text = email_text.split("@")
        if '.' not in provider_text:
            print(f">> Domain '{provider_text}' is incorrect!")
            continue
        if len(name_text) < 1:
            print(">> Email name is to short!")
            continue
        if provider is not None:
            if provider_text.lower() != provider.lower():
                print(f">> Email has to be in '{provider}' domain!")
                continue
        return email_text


def numeric_input(text: str, round_to: Optional[Union[int, None]] = 0, accept_float: Optional[bool] = True) -> Union[int, float]:
    """
    Get user input as a numerical value.

    Args:
        text: Input message.
        round_to: Amount of decimal places to round up input to.
        accept_float: Convert input to int if float is given.

    Returns:
        Optionally rounded numerical value given by user.
    """
    while True:
        input_text = str(input(text))
        if not is_float(input_text):
            print(">> Insert numeric value!")
            continue
        input_value = float(input_text)
        input_value = int(input_value) if not accept_float else round(input_value, round_to) if round_to is not None else input_value
        input_value = int(input_value) if input_value % 1 == 0 else input_value
        return input_value
