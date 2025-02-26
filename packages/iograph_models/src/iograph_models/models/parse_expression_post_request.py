from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Parse_expressionPostRequest(BaseModel):
	expression: Optional[str] = Field(default=None,alias="expression",)
	testInputObject: Optional[ExpressionInputObject] = Field(default=None,alias="testInputObject",)
	targetAttributeDefinition: Optional[AttributeDefinition] = Field(default=None,alias="targetAttributeDefinition",)

from .expression_input_object import ExpressionInputObject
from .attribute_definition import AttributeDefinition

