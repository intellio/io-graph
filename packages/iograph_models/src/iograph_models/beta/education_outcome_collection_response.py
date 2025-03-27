from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class EducationOutcomeCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[EducationFeedbackOutcome, EducationFeedbackResourceOutcome, EducationPointsOutcome, EducationRubricOutcome],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .education_feedback_outcome import EducationFeedbackOutcome
from .education_feedback_resource_outcome import EducationFeedbackResourceOutcome
from .education_points_outcome import EducationPointsOutcome
from .education_rubric_outcome import EducationRubricOutcome

