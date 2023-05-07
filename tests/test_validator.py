from typing import Any

import pytest

from validator_task import InputData, ValidationError, ValidatorFactory

test_data = [
    # Topic A
    (
        {
            "topic": "A",
            "name": "a",
            "description": "This is a valid description for topic A.",
        },
        None,
    ),
    (
        {
            "topic": "A",
            "name": "b",
            "description": "This is an invalid name for topic A.",
        },
        "Invalid name for topic A",
    ),
    (
        {"topic": "A", "name": "a", "description": "short"},
        "Invalid description length for topic A",
    ),
    # Topic B
    (
        {"topic": "B", "name": "x", "description": "Valid description for topic B."},
        None,
    ),
    (
        {"topic": "B", "name": "y", "description": "Invalid name for topic B."},
        "Invalid name for topic B",
    ),
    (
        {
            "topic": "B",
            "name": "x",
            "description": "This description is too long for topic B." * 2,
        },
        "Invalid description length for topic B",
    ),
    # Non-existent topic
    (
        {"topic": "C", "name": "z", "description": "This topic does not exist."},
        "No validator found for topic 'C'",
    ),
]


@pytest.mark.parametrize("data_dict,expected_error", test_data)
def test_validators(data_dict: dict[str, Any], expected_error: str) -> None:
    data = InputData.from_dict(data_dict)
    topic = data.topic

    if expected_error is not None and expected_error.startswith("No validator"):
        with pytest.raises(ValueError) as factory_exc:
            validator = ValidatorFactory.get_validator(topic)
        assert str(factory_exc.value) == expected_error
    else:
        validator = ValidatorFactory.get_validator(topic)
        if expected_error is None:
            validator.validate(data)
        else:
            with pytest.raises(ValidationError) as exc:
                validator.validate(data)
            assert str(exc.value) == expected_error
