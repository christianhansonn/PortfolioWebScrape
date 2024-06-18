from dataclasses import dataclass

@dataclass
class Applicant:
    """
    Object to track new applicants
    """
    name: str
    email: str
    phone: str

    def __str__(self):
        return f'Name: {self.name} \nEmail: {self.email} \nPhone: {self.phone}'