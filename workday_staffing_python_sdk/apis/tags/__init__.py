# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from workday_staffing_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    PROMPT_VALUES = "Prompt Values"
    JOB_CHANGES = "jobChanges"
    WORKERS = "workers"
    ORGANIZATION_ASSIGNMENT_CHANGES = "organizationAssignmentChanges"
    SUPERVISORY_ORGANIZATIONS = "supervisoryOrganizations"
    JOBS = "jobs"
    JOB_FAMILIES = "jobFamilies"
    JOB_PROFILES = "jobProfiles"
