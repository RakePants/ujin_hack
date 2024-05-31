from .schema import PersonRequestSchema


def from_model_to_entity(person: PersonRequestSchema, file_name: str) -> dict:
    return {"face_id": str(person.face_id),
            "is_identified": person.is_identified,
            "first_name": person.first_name,
            "last_name": person.last_name,
            "patronymic": person.patronymic,
            "detection_date": person.detection_time.isoformat(),
            "pass_issue_date": (person.start_time.isoformat() if person.start_time else None),
            "pass_expiration_date": (person.end_time.isoformat() if person.end_time else None),
            "image": file_name}
    