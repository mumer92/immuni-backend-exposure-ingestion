from prometheus_client import Counter, Gauge

from immuni_common.monitoring.core import NAMESPACE, Subsystem

KEYS_PROCESSED = Counter(
    namespace=NAMESPACE,
    subsystem=Subsystem.API.value,
    name="keys_processed",
    documentation="Total number of keys processed.",
)

BATCH_FILES_CREATED = Counter(
    namespace=NAMESPACE,
    subsystem=Subsystem.API.value,
    name="batches_created",
    documentation="Total number of created batches.",
)

UPLOADS_ENQUEUED = Gauge(
    namespace=NAMESPACE,
    subsystem=Subsystem.API.value,
    name="uploads_enqueued",
    documentation="Total number of Uploads still to be processed after completing a batch",
)

UPLOADS_DELETED = Counter(
    namespace=NAMESPACE,
    subsystem=Subsystem.API.value,
    name="uploads_deleted",
    documentation="Total number of deleted uploads.",
)

BATCH_FILES_DELETED = Counter(
    namespace=NAMESPACE,
    subsystem=Subsystem.API.value,
    name="batches_deleted",
    documentation="Total number of deleted batches.",
)
