def custom_enum_validator(value, enum_class):
    """
    Validates that a value belongs to the specified Enum class.
    Accepts values as enum members, names, or values.
    
    Args:
        value: The value to validate
        enum_class: The Enum class to validate against
        
    Returns:
        The validated enum member
        
    Raises:
        ValueError: If the value is not a valid member of the enum
    """
    if value is None:
        raise ValueError(f"Value cannot be None for {enum_class.__name__}")
        
    if isinstance(value, enum_class):
        return value
        
    try:
        # Try to get by name (string representation)
        if isinstance(value, str):
            return enum_class[value]
    except KeyError:
        pass
        
    try:
        # Try to get by value
        return enum_class(value)
    except ValueError:
        pass
        
    # If we get here, the value is invalid
    valid_options = [f"{e.name} ({e.value})" for e in enum_class]
    options_str = ", ".join(valid_options)
    
    raise ValueError(
        f"Invalid value for {enum_class.__name__}: {value}. "
        f"Valid options are: {options_str}"
    )