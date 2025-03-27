from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field, SerializeAsAny


class EducationAssignmentResource(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	distributeForStudentWork: Optional[bool] = Field(alias="distributeForStudentWork", default=None,)
	resource: Optional[Union[EducationChannelResource, EducationExcelResource, EducationExternalResource, EducationFileResource, EducationLinkedAssignmentResource, EducationLinkResource, EducationMediaResource, EducationPowerPointResource, EducationTeamsAppResource, EducationWordResource]] = Field(alias="resource", default=None,discriminator="odata_type", )
	dependentResources: Optional[list[EducationAssignmentResource]] = Field(alias="dependentResources", default=None,)

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

