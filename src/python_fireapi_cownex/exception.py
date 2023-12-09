class ParameterNotGivenException:
    raise Exception("Required Parameter don't given!")

class OneOptionalParameterRequiredException:
    raise Exception("At least one Optional Parameter is required!")

class InvalidActionException:
    raise Exception("Action is not possible!")