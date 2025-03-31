from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class DataClassificationService(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.dataClassificationService"] = Field(alias="@odata.type",)
	classifyFileJobs: Optional[list[Annotated[Union[ClassificationJobResponse, DlpEvaluatePoliciesJobResponse, EvaluateLabelJobResponse],Field(discriminator="odata_type")]]] = Field(alias="classifyFileJobs", default=None,)
	classifyTextJobs: Optional[list[Annotated[Union[ClassificationJobResponse, DlpEvaluatePoliciesJobResponse, EvaluateLabelJobResponse],Field(discriminator="odata_type")]]] = Field(alias="classifyTextJobs", default=None,)
	evaluateDlpPoliciesJobs: Optional[list[Annotated[Union[ClassificationJobResponse, DlpEvaluatePoliciesJobResponse, EvaluateLabelJobResponse],Field(discriminator="odata_type")]]] = Field(alias="evaluateDlpPoliciesJobs", default=None,)
	evaluateLabelJobs: Optional[list[Annotated[Union[ClassificationJobResponse, DlpEvaluatePoliciesJobResponse, EvaluateLabelJobResponse],Field(discriminator="odata_type")]]] = Field(alias="evaluateLabelJobs", default=None,)
	exactMatchDataStores: Optional[list[ExactMatchDataStore]] = Field(alias="exactMatchDataStores", default=None,)
	exactMatchUploadAgents: Optional[list[ExactMatchUploadAgent]] = Field(alias="exactMatchUploadAgents", default=None,)
	jobs: Optional[list[Annotated[Union[ClassificationJobResponse, DlpEvaluatePoliciesJobResponse, EvaluateLabelJobResponse],Field(discriminator="odata_type")]]] = Field(alias="jobs", default=None,)
	sensitiveTypes: Optional[list[SensitiveType]] = Field(alias="sensitiveTypes", default=None,)
	sensitivityLabels: Optional[list[SensitivityLabel]] = Field(alias="sensitivityLabels", default=None,)

from .classification_job_response import ClassificationJobResponse
from .dlp_evaluate_policies_job_response import DlpEvaluatePoliciesJobResponse
from .evaluate_label_job_response import EvaluateLabelJobResponse
from .exact_match_data_store import ExactMatchDataStore
from .exact_match_upload_agent import ExactMatchUploadAgent
from .sensitive_type import SensitiveType
from .sensitivity_label import SensitivityLabel
