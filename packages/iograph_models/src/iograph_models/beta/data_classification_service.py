from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DataClassificationService(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	classifyFileJobs: SerializeAsAny[Optional[list[JobResponseBase]]] = Field(alias="classifyFileJobs",default=None,)
	classifyTextJobs: SerializeAsAny[Optional[list[JobResponseBase]]] = Field(alias="classifyTextJobs",default=None,)
	evaluateDlpPoliciesJobs: SerializeAsAny[Optional[list[JobResponseBase]]] = Field(alias="evaluateDlpPoliciesJobs",default=None,)
	evaluateLabelJobs: SerializeAsAny[Optional[list[JobResponseBase]]] = Field(alias="evaluateLabelJobs",default=None,)
	exactMatchDataStores: Optional[list[ExactMatchDataStore]] = Field(alias="exactMatchDataStores",default=None,)
	exactMatchUploadAgents: Optional[list[ExactMatchUploadAgent]] = Field(alias="exactMatchUploadAgents",default=None,)
	jobs: SerializeAsAny[Optional[list[JobResponseBase]]] = Field(alias="jobs",default=None,)
	sensitiveTypes: Optional[list[SensitiveType]] = Field(alias="sensitiveTypes",default=None,)
	sensitivityLabels: Optional[list[SensitivityLabel]] = Field(alias="sensitivityLabels",default=None,)

from .job_response_base import JobResponseBase
from .job_response_base import JobResponseBase
from .job_response_base import JobResponseBase
from .job_response_base import JobResponseBase
from .exact_match_data_store import ExactMatchDataStore
from .exact_match_upload_agent import ExactMatchUploadAgent
from .job_response_base import JobResponseBase
from .sensitive_type import SensitiveType
from .sensitivity_label import SensitivityLabel

