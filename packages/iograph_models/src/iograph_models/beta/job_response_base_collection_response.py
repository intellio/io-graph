from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class JobResponseBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[ClassificationJobResponse, DlpEvaluatePoliciesJobResponse, EvaluateLabelJobResponse],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .classification_job_response import ClassificationJobResponse
from .dlp_evaluate_policies_job_response import DlpEvaluatePoliciesJobResponse
from .evaluate_label_job_response import EvaluateLabelJobResponse

