from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class InformationProtection(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	bitlocker: Optional[Bitlocker] = Field(alias="bitlocker", default=None,)
	dataLossPreventionPolicies: Optional[list[DataLossPreventionPolicy]] = Field(alias="dataLossPreventionPolicies", default=None,)
	policy: Optional[InformationProtectionPolicy] = Field(alias="policy", default=None,)
	sensitivityLabels: Optional[list[SensitivityLabel]] = Field(alias="sensitivityLabels", default=None,)
	sensitivityPolicySettings: Optional[SensitivityPolicySettings] = Field(alias="sensitivityPolicySettings", default=None,)
	threatAssessmentRequests: Optional[list[Annotated[Union[EmailFileAssessmentRequest, FileAssessmentRequest, MailAssessmentRequest, UrlAssessmentRequest],Field(discriminator="odata_type")]]] = Field(alias="threatAssessmentRequests", default=None,)

from .bitlocker import Bitlocker
from .data_loss_prevention_policy import DataLossPreventionPolicy
from .information_protection_policy import InformationProtectionPolicy
from .sensitivity_label import SensitivityLabel
from .sensitivity_policy_settings import SensitivityPolicySettings
from .email_file_assessment_request import EmailFileAssessmentRequest
from .file_assessment_request import FileAssessmentRequest
from .mail_assessment_request import MailAssessmentRequest
from .url_assessment_request import UrlAssessmentRequest

