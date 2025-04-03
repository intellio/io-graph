from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class EducationSubmissionResource(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.educationSubmissionResource"] = Field(alias="@odata.type", default="#microsoft.graph.educationSubmissionResource")
	assignmentResourceUrl: Optional[str] = Field(alias="assignmentResourceUrl", default=None,)
	resource: Optional[Union[EducationChannelResource, EducationExcelResource, EducationExternalResource, EducationFileResource, EducationLinkedAssignmentResource, EducationLinkResource, EducationMediaResource, EducationPowerPointResource, EducationTeamsAppResource, EducationWordResource]] = Field(alias="resource", default=None,discriminator="odata_type", )

from .education_channel_resource import EducationChannelResource
from .education_excel_resource import EducationExcelResource
from .education_external_resource import EducationExternalResource
from .education_file_resource import EducationFileResource
from .education_linked_assignment_resource import EducationLinkedAssignmentResource
from .education_link_resource import EducationLinkResource
from .education_media_resource import EducationMediaResource
from .education_power_point_resource import EducationPowerPointResource
from .education_teams_app_resource import EducationTeamsAppResource
from .education_word_resource import EducationWordResource
