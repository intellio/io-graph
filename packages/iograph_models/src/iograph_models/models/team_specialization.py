from __future__ import annotations
from enum import Enum


class TeamSpecialization(Enum):
	none = "none"
	educationStandard = "educationStandard"
	educationClass = "educationClass"
	educationProfessionalLearningCommunity = "educationProfessionalLearningCommunity"
	educationStaff = "educationStaff"
	healthcareStandard = "healthcareStandard"
	healthcareCareCoordination = "healthcareCareCoordination"
	unknownFutureValue = "unknownFutureValue"

