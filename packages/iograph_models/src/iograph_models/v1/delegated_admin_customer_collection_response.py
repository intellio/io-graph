from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DelegatedAdminCustomerCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[DelegatedAdminCustomer]] = Field(alias="value", default=None,)

from .delegated_admin_customer import DelegatedAdminCustomer
