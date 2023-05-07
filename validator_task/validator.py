from typing import Any


class ValidationError(Exception):
    pass


class InputData:
    def __init__(self, topic: str, name: str, description: str):
        self.topic = topic
        self.name = name
        self.description = description

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "InputData":
        return cls(
            topic=data["topic"], name=data["name"], description=data["description"]
        )


class Validator:
    def validate(self, data: InputData) -> None:
        raise NotImplementedError


class TopicAValidator(Validator):
    def validate(self, data: InputData) -> None:
        if data.name != "a":
            raise ValidationError("Invalid name for topic A")

        desc_len = len(data.description)
        if not 10 < desc_len < 100:
            raise ValidationError("Invalid description length for topic A")


class TopicBValidator(Validator):
    def validate(self, data: InputData) -> None:
        if data.name != "x":
            raise ValidationError("Invalid name for topic B")

        desc_len = len(data.description)
        if not desc_len < 40:
            raise ValidationError("Invalid description length for topic B")


class ValidatorFactory:
    validators: dict[str, type[Validator]] = {
        "A": TopicAValidator,
        "B": TopicBValidator,
    }

    @classmethod
    def get_validator(cls, topic: str) -> Validator:
        validator = cls.validators.get(topic)
        if not validator:
            raise ValueError(f"No validator found for topic '{topic}'")
        return validator()
