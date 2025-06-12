import enum


class UserRole(str, enum.Enum):
    """
    Enum representing user roles in the application.
    """

    SUPERUSER = "superuser"
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"


class JobApplicationStatus(str, enum.Enum):
    """
    Enum representing the status of a job application.
    """

    APPLIED = "applied"
    INTERVIEW_SCHEDULED = "interview_scheduled"
    OFFERED = "offered"
    REJECTED = "rejected"
    ACCEPTED = "accepted"
    WITHDRAWN = "withdrawn"
    PENDING = "pending"


class AssistantStepStatus(str, enum.Enum):
    """
    Enum representing the status of the job application assistant.
    """

    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    NOT_STARTED = "not_started"


class AssistantStepType(str, enum.Enum):
    """
    Enum representing the steps in the job application assistant process.
    """

    INITIAL = "initial"
    MASTER_LIST = "master_list"
    TAILORED_RESUME = "tailored_resume"
    TAILORED_COVER_LETTER = "tailored_cover_letter"
    CANDIDATE_VALIDATION = "candidate_validation"
    APPLICATION_TIPS = "application_tips"
    HIRING_MANAGER_REVIEW = "hiring_manager_review"


class DocumentType(str, enum.Enum):
    """
    Enum representing different types of documents.
    """

    RESUME = "resume"
    COVER_LETTER = "cover_letter"
    SUPPORTING_DOCUMENT = "supporting_document"
    MASTER_LIST = "master_list"
    JOB_DESCRIPTION = "job_description"
    GENERAL = "general"


class DocumentStatus(str, enum.Enum):
    """
    Enum representing the status of a document.
    """

    UPLOADED = "uploaded"
    PROCESSING = "processing"
    PARSED = "parsed"
    VALIDATED = "validated"
    ERROR = "error"
    ARCHIVED = "archived"
    PENDING = "pending"


class DocumentVisibility(str, enum.Enum):
    """
    Enum representing the visibility of a document.
    """

    PUBLIC = "public"
    PRIVATE = "private"
    INTERNAL = "internal"
    CONFIDENTIAL = "confidential"


class DocumentSource(str, enum.Enum):
    """
    Enum representing the source of a document.
    """

    USER_UPLOAD = "user_upload"
    EMAIL = "email"
    EXTERNAL_API = "external_api"
    SCRAPED = "scraped"
    IMPORTED = "imported"
    GENERATED = "generated"


class DocumentVersion(str, enum.Enum):
    """
    Enum representing different versions of a document.
    """

    DRAFT = "draft"
    FINAL = "final"
    REVISED = "revised"
    ARCHIVED = "archived"
    TEMPLATE = "template"


class SkillProficiency(str, enum.Enum):
    """
    Enum representing different levels of skill proficiency.
    """

    PROFICIENT = "proficient"
    EXPERIENCED = "experienced"
    FAMILIAR_WITH = "familiar_with"


class MimeType(str, enum.Enum):
    """
    Enum representing common MIME types for documents.
    """

    PDF = "application/pdf"
    DOCX = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    DOC = "application/msword"
    CSV = "text/csv"
    XLSX = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    XLS = "application/vnd.ms-excel"
    PPTX = "application/vnd.openxmlformats-officedocument.presentationml.presentation"
    PPT = "application/vnd.ms-powerpoint"
    ODT = "application/vnd.oasis.opendocument.text"
    ODS = "application/vnd.oasis.opendocument.spreadsheet"
    ODP = "application/vnd.oasis.opendocument.presentation"
    RTF = "application/rtf"
    XML = "application/xml"
    YAML = "application/x-yaml"
    MARKDOWN = "text/markdown"
    TXT = "text/plain"
    HTML = "text/html"
    JSON = "application/json"
    UNKNOWN = "application/octet-stream"


class FileType(str, enum.Enum):
    """
    Enum representing common file types for documents.
    """

    PDF = "pdf"
    DOCX = "docx"
    DOC = "doc"
    CSV = "csv"
    XLSX = "xlsx"
    XLS = "xls"
    PPTX = "pptx"
    PPT = "ppt"
    ODT = "odt"
    ODS = "ods"
    ODP = "odp"
    RTF = "rtf"
    XML = "xml"
    YAML = "yaml"
    MARKDOWN = "md"
    TXT = "txt"
    HTML = "html"
    JSON = "json"
    UNKNOWN = "unknown"


class JobType(str, enum.Enum):
    """Enum representing different types of job positions."""

    FULL_TIME = "full_time"
    PART_TIME = "part_time"
    CONTRACT = "contract"
    INTERNSHIP = "internship"
    TEMPORARY = "temporary"
    FREELANCE = "freelance"


class JobApplicationSource(str, enum.Enum):
    """Enum representing the source of a job application."""

    LINKEDIN = "linkedin"
    COMPANY_WEBSITE = "company_website"
    INDEED = "indeed"
    GLASSDOOR = "glassdoor"
    SOCIAL_MEDIA = "social_media"
    REFERRAL = "referral"


class JobApplicationPriority(str, enum.Enum):
    """Enum representing the priority of a job application."""

    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    NONE = "none"


class SSOProvider(str, enum.Enum):
    """Enum representing different Single Sign-On (SSO) providers."""

    GOOGLE = "google"
    MICROSOFT = "microsoft"
    GITHUB = "github"
    FACEBOOK = "facebook"
    OKTA = "okta"
    DISCORD = "discord"
    APPLE = "apple"
    CUSTOM = "custom"
