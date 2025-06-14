from .cover_letter import CoverLetter
from .job_description import JobDescription
from .master_list import MasterList
from .resume import Resume
from .supporting_document import SupportingDocument

AllDocumentContent = Resume | CoverLetter | SupportingDocument | MasterList | JobDescription

__all__ = (
    "Resume",
    "CoverLetter",
    "SupportingDocument",
    "MasterList",
    "JobDescription",
    "AllDocumentContent",
)
