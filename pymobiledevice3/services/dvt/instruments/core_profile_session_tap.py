from construct import Struct, Int32ul, Int64ul, FixedSized, GreedyRange, GreedyBytes, Enum, Switch, Padding, Padded, \
    LazyBound, CString, Computed, Array, this, Byte, Int16ul, Pass

from pymobiledevice3.services.dvt.tap import Tap
from pymobiledevice3.services.dvt.dvt_secure_socket_proxy import DvtSecureSocketProxyService

kcdata_types = {
    'KCDATA_TYPE_INVALID': 0x0,
    'KCDATA_TYPE_STRING_DESC': 0x1,
    'KCDATA_TYPE_UINT32_DESC': 0x2,
    'KCDATA_TYPE_UINT64_DESC': 0x3,
    'KCDATA_TYPE_INT32_DESC': 0x4,
    'KCDATA_TYPE_INT64_DESC': 0x5,
    'KCDATA_TYPE_BINDATA_DESC': 0x6,
    'KCDATA_TYPE_ARRAY': 0x11,
    'KCDATA_TYPE_TYPEDEFINITION': 0x12,
    'KCDATA_TYPE_CONTAINER_BEGIN': 0x13,
    'KCDATA_TYPE_CONTAINER_END': 0x14,

    'KCDATA_TYPE_ARRAY_PAD0': 0x20,
    'KCDATA_TYPE_ARRAY_PAD1': 0x21,
    'KCDATA_TYPE_ARRAY_PAD2': 0x22,
    'KCDATA_TYPE_ARRAY_PAD3': 0x23,
    'KCDATA_TYPE_ARRAY_PAD4': 0x24,
    'KCDATA_TYPE_ARRAY_PAD5': 0x25,
    'KCDATA_TYPE_ARRAY_PAD6': 0x26,
    'KCDATA_TYPE_ARRAY_PAD7': 0x27,
    'KCDATA_TYPE_ARRAY_PAD8': 0x28,
    'KCDATA_TYPE_ARRAY_PAD9': 0x29,
    'KCDATA_TYPE_ARRAY_PADa': 0x2a,
    'KCDATA_TYPE_ARRAY_PADb': 0x2b,
    'KCDATA_TYPE_ARRAY_PADc': 0x2c,
    'KCDATA_TYPE_ARRAY_PADd': 0x2d,
    'KCDATA_TYPE_ARRAY_PADe': 0x2e,
    'KCDATA_TYPE_ARRAY_PADf': 0x2f,

    'KCDATA_TYPE_LIBRARY_LOADINFO': 0x30,
    'KCDATA_TYPE_LIBRARY_LOADINFO64': 0x31,
    'KCDATA_TYPE_TIMEBASE': 0x32,
    'KCDATA_TYPE_MACH_ABSOLUTE_TIME': 0x33,
    'KCDATA_TYPE_TIMEVAL': 0x34,
    'KCDATA_TYPE_USECS_SINCE_EPOCH': 0x35,
    'KCDATA_TYPE_PID': 0x36,
    'KCDATA_TYPE_PROCNAME': 0x37,
    'KCDATA_TYPE_NESTED_KCDATA': 0x38,

    'STACKSHOT_KCTYPE_IO_STATISTICS': 0x901,
    'STACKSHOT_KCCONTAINER_TASK': 0x903,
    'STACKSHOT_KCCONTAINER_THREAD': 0x904,
    'STACKSHOT_KCTYPE_TASK_SNAPSHOT': 0x905,
    'STACKSHOT_KCTYPE_THREAD_SNAPSHOT': 0x906,
    'STACKSHOT_KCTYPE_DONATING_PIDS': 0x907,
    'STACKSHOT_KCTYPE_SHAREDCACHE_LOADINFO': 0x908,
    'STACKSHOT_KCTYPE_THREAD_NAME': 0x909,
    'STACKSHOT_KCTYPE_KERN_STACKFRAME': 0x90A,
    'STACKSHOT_KCTYPE_KERN_STACKFRAME64': 0x90B,
    'STACKSHOT_KCTYPE_USER_STACKFRAME': 0x90C,
    'STACKSHOT_KCTYPE_USER_STACKFRAME64': 0x90D,
    'STACKSHOT_KCTYPE_BOOTARGS': 0x90E,
    'STACKSHOT_KCTYPE_OSVERSION': 0x90F,
    'STACKSHOT_KCTYPE_KERN_PAGE_SIZE': 0x910,
    'STACKSHOT_KCTYPE_JETSAM_LEVEL': 0x911,
    'STACKSHOT_KCTYPE_DELTA_SINCE_TIMESTAMP': 0x912,
    'STACKSHOT_KCTYPE_KERN_STACKLR': 0x913,
    'STACKSHOT_KCTYPE_KERN_STACKLR64': 0x914,
    'STACKSHOT_KCTYPE_USER_STACKLR': 0x915,
    'STACKSHOT_KCTYPE_USER_STACKLR64': 0x916,
    'STACKSHOT_KCTYPE_NONRUNNABLE_TIDS': 0x917,
    'STACKSHOT_KCTYPE_NONRUNNABLE_TASKS': 0x918,
    'STACKSHOT_KCTYPE_CPU_TIMES': 0x919,
    'STACKSHOT_KCTYPE_STACKSHOT_DURATION': 0x91a,
    'STACKSHOT_KCTYPE_STACKSHOT_FAULT_STATS': 0x91b,
    'STACKSHOT_KCTYPE_KERNELCACHE_LOADINFO': 0x91c,
    'STACKSHOT_KCTYPE_THREAD_WAITINFO': 0x91d,
    'STACKSHOT_KCTYPE_THREAD_GROUP_SNAPSHOT': 0x91e,
    'STACKSHOT_KCTYPE_THREAD_GROUP': 0x91f,
    'STACKSHOT_KCTYPE_JETSAM_COALITION_SNAPSHOT': 0x920,
    'STACKSHOT_KCTYPE_JETSAM_COALITION': 0x921,
    'STACKSHOT_KCTYPE_THREAD_POLICY_VERSION': 0x922,
    'STACKSHOT_KCTYPE_INSTRS_CYCLES': 0x923,
    'STACKSHOT_KCTYPE_USER_STACKTOP': 0x924,
    'STACKSHOT_KCTYPE_ASID': 0x925,
    'STACKSHOT_KCTYPE_PAGE_TABLES': 0x926,
    'STACKSHOT_KCTYPE_SYS_SHAREDCACHE_LAYOUT': 0x927,
    'STACKSHOT_KCTYPE_THREAD_DISPATCH_QUEUE_LABEL': 0x928,
    'STACKSHOT_KCTYPE_THREAD_TURNSTILEINFO': 0x929,
    'STACKSHOT_KCTYPE_TASK_CPU_ARCHITECTURE': 0x92a,
    'STACKSHOT_KCTYPE_LATENCY_INFO': 0x92b,
    'STACKSHOT_KCTYPE_LATENCY_INFO_TASK': 0x92c,
    'STACKSHOT_KCTYPE_LATENCY_INFO_THREAD': 0x92d,
    'STACKSHOT_KCTYPE_LOADINFO64_TEXT_EXEC': 0x92e,

    'STACKSHOT_KCTYPE_TASK_DELTA_SNAPSHOT': 0x940,
    'STACKSHOT_KCTYPE_THREAD_DELTA_SNAPSHOT': 0x941,

    'KCDATA_TYPE_BUFFER_END': 0xF19158ED,

    'TASK_CRASHINFO_EXTMODINFO': 0x801,
    'TASK_CRASHINFO_BSDINFOWITHUNIQID': 0x802,
    'TASK_CRASHINFO_TASKDYLD_INFO': 0x803,
    'TASK_CRASHINFO_UUID': 0x804,
    'TASK_CRASHINFO_PID': 0x805,
    'TASK_CRASHINFO_PPID': 0x806,

    # Don't want anyone using this.  It's struct rusage from whatever machine generated the data
    # 'TASK_CRASHINFO_RUSAGE':               0x807,
    'Type_0x807': 0x807,

    'TASK_CRASHINFO_RUSAGE_INFO': 0x808,
    'TASK_CRASHINFO_PROC_NAME': 0x809,
    'TASK_CRASHINFO_PROC_STARTTIME': 0x80B,
    'TASK_CRASHINFO_USERSTACK': 0x80C,
    'TASK_CRASHINFO_ARGSLEN': 0x80D,
    'TASK_CRASHINFO_EXCEPTION_CODES': 0x80E,
    'TASK_CRASHINFO_PROC_PATH': 0x80F,
    'TASK_CRASHINFO_PROC_CSFLAGS': 0x810,
    'TASK_CRASHINFO_PROC_STATUS': 0x811,
    'TASK_CRASHINFO_UID': 0x812,
    'TASK_CRASHINFO_GID': 0x813,
    'TASK_CRASHINFO_PROC_ARGC': 0x814,
    'TASK_CRASHINFO_PROC_FLAGS': 0x815,
    'TASK_CRASHINFO_CPUTYPE': 0x816,
    'TASK_CRASHINFO_WORKQUEUEINFO': 0x817,
    'TASK_CRASHINFO_RESPONSIBLE_PID': 0x818,
    'TASK_CRASHINFO_DIRTY_FLAGS': 0x819,
    'TASK_CRASHINFO_CRASHED_THREADID': 0x81A,
    'TASK_CRASHINFO_COALITION_ID': 0x81B,
    'EXIT_REASON_SNAPSHOT': 0x1001,
    'EXIT_REASON_USER_DESC': 0x1002,
    'EXIT_REASON_USER_PAYLOAD': 0x1003,
    'EXIT_REASON_CODESIGNING_INFO': 0x1004,
    'EXIT_REASON_WORKLOOP_ID': 0x1005,
    'EXIT_REASON_DISPATCH_QUEUE_NO': 0x1006,
    'KCDATA_BUFFER_BEGIN_CRASHINFO': 0xDEADF157,
    'KCDATA_BUFFER_BEGIN_DELTA_STACKSHOT': 0xDE17A59A,
    'KCDATA_BUFFER_BEGIN_STACKSHOT': 0x59a25807,
    'KCDATA_BUFFER_BEGIN_COMPRESSED': 0x434f4d50,
    'KCDATA_BUFFER_BEGIN_OS_REASON': 0x53A20900,
    'KCDATA_BUFFER_BEGIN_XNUPOST_CONFIG': 0x1E21C09F,
}

kcdata_types_enum = Enum(Int32ul, **kcdata_types)

predefined_names = {
    kcdata_types_enum.STACKSHOT_KCTYPE_JETSAM_LEVEL: 'jetsam_level',
    kcdata_types_enum.STACKSHOT_KCTYPE_THREAD_POLICY_VERSION: 'thread_policy_version',
    kcdata_types_enum.STACKSHOT_KCTYPE_KERN_PAGE_SIZE: 'kernel_page_size',
    kcdata_types_enum.STACKSHOT_KCTYPE_OSVERSION: 'osversion',
    kcdata_types_enum.STACKSHOT_KCTYPE_BOOTARGS: 'boot_args',
    kcdata_types_enum.KCDATA_TYPE_TIMEBASE: 'mach_timebase_info',
    kcdata_types_enum.KCDATA_TYPE_MACH_ABSOLUTE_TIME: 'mach_absolute_time',
    kcdata_types_enum.KCDATA_TYPE_USECS_SINCE_EPOCH: 'usecs_since_epoch',
    kcdata_types_enum.STACKSHOT_KCTYPE_SHAREDCACHE_LOADINFO: 'shared_cache_dyld_load_info',
    kcdata_types_enum.STACKSHOT_KCTYPE_THREAD_GROUP_SNAPSHOT: 'thread_group_snapshot',
    kcdata_types_enum.STACKSHOT_KCCONTAINER_TASK: 'task_snapshots',
    kcdata_types_enum.STACKSHOT_KCCONTAINER_THREAD: 'thread_snapshots',
    kcdata_types_enum.STACKSHOT_KCTYPE_KERNELCACHE_LOADINFO: 'kernelcache_load_info',
    kcdata_types_enum.STACKSHOT_KCTYPE_TASK_SNAPSHOT: 'task_snapshot',
    kcdata_types_enum.STACKSHOT_KCTYPE_JETSAM_COALITION: 'jetsam_coalition',
    kcdata_types_enum.STACKSHOT_KCTYPE_IO_STATISTICS: 'io_statistics',
    kcdata_types_enum.STACKSHOT_KCTYPE_TASK_CPU_ARCHITECTURE: 'task_cpu_architecture',
    kcdata_types_enum.STACKSHOT_KCTYPE_THREAD_SNAPSHOT: 'thread_snapshot',
    kcdata_types_enum.STACKSHOT_KCTYPE_THREAD_NAME: 'pth_name',
    kcdata_types_enum.STACKSHOT_KCTYPE_CPU_TIMES: 'cpu_times',
    kcdata_types_enum.STACKSHOT_KCTYPE_THREAD_GROUP: 'thread_group',
    kcdata_types_enum.STACKSHOT_KCTYPE_KERN_STACKLR64: 'kernel_stack_frames',
    kcdata_types_enum.KCDATA_TYPE_LIBRARY_LOADINFO64: 'dyld_load_info',
    kcdata_types_enum.STACKSHOT_KCTYPE_USER_STACKLR64: 'user_stack_frames',
    kcdata_types_enum.STACKSHOT_KCTYPE_JETSAM_COALITION_SNAPSHOT: 'jetsam_coalition_snapshot',
    kcdata_types_enum.STACKSHOT_KCTYPE_DONATING_PIDS: 'donating_pids',
    kcdata_types_enum.STACKSHOT_KCTYPE_THREAD_DISPATCH_QUEUE_LABEL: 'dispatch_queue_label',
    kcdata_types_enum.KCDATA_BUFFER_BEGIN_STACKSHOT: 'kcdata_stackshot',
    kcdata_types_enum.STACKSHOT_KCTYPE_STACKSHOT_FAULT_STATS: 'stackshot_fault_stats',
}

predefined_name_substruct = 'name' / Computed(lambda ctx: predefined_names[ctx._.type])

kcdata_container = Struct(
    Padding(16),
)

uint32_desc = Struct(
    'name' / Padded(32, CString('utf8')),
    'obj' / Int32ul,
)

uint64_desc = Struct(
    'name' / Padded(32, CString('utf8')),
    'obj' / Int64ul,
)

jetsam_level = Struct(predefined_name_substruct, 'obj' / Int32ul)
thread_policy_version = Struct(predefined_name_substruct, 'obj' / Int32ul)
kernel_page_size = Struct(predefined_name_substruct, 'obj' / Int32ul)
osversion = Struct(predefined_name_substruct, 'obj' / CString('utf8'))
boot_args = Struct(predefined_name_substruct, 'obj' / CString('utf8'))
mach_timebase_info = Struct(
    predefined_name_substruct,
    'obj' / Struct(
        'numer' / Int32ul,
        'denom' / Int32ul,
    )
)
mach_absolute_time = Struct(predefined_name_substruct, 'obj' / Int64ul)
usecs_since_epoch = Struct(predefined_name_substruct, 'obj' / Int64ul)
shared_cache_dyld_load_info = Struct(
    predefined_name_substruct,
    'obj' / Struct(
        'imageLoadAddress' / Int64ul,
        'imageUUID' / Array(16, Byte),
        'imageSlidBaseAddress' / Int64ul,
    ),
)
thread_group_snapshot = Struct(
    predefined_name_substruct,
    'obj' / Struct(
        'tgs_id' / Int64ul,
        'tgs_name' / Padded(16, CString('utf8')),
        'tgs_flags' / Int64ul
    ),
)
type_array_pad0 = Struct(
    'flags_type' / Computed(lambda ctx: (ctx._.flags >> 32) & 0xffffffff),
    'type' / Computed(lambda ctx: kcdata_types_enum.decmapping[ctx.flags_type]),
    'count' / Computed(lambda ctx: ctx._.flags & 0xffffffff),
    'name' / Computed(lambda ctx: predefined_names[ctx.type]),
    'obj' / Array(this.count, LazyBound(lambda: Switch(
        lambda ctx: ctx.type,
        kcdata_types_structures,
        default=GreedyBytes
    ))),
)
type_array_pad4 = Struct(
    'flags_type' / Computed(lambda ctx: (ctx._.flags >> 32) & 0xffffffff),
    'type' / Computed(lambda ctx: kcdata_types_enum.decmapping[ctx.flags_type]),
    'count' / Computed(lambda ctx: ctx._.flags & 0xffffffff),
    'name' / Computed(lambda ctx: predefined_names[ctx.type]),
    'obj' / Array(this.count, LazyBound(lambda: Switch(
        lambda ctx: ctx.type,
        kcdata_types_structures,
        default=GreedyBytes
    ))),
    Padding(4),
)
type_array_pad8 = Struct(
    'flags_type' / Computed(lambda ctx: (ctx._.flags >> 32) & 0xffffffff),
    'type' / Computed(lambda ctx: kcdata_types_enum.decmapping[ctx.flags_type]),
    'count' / Computed(lambda ctx: ctx._.flags & 0xffffffff),
    'name' / Computed(lambda ctx: predefined_names[ctx.type]),
    'obj' / Array(this.count, LazyBound(lambda: Switch(
        lambda ctx: ctx.type,
        kcdata_types_structures,
        default=GreedyBytes
    ))),
    Padding(8),
)
type_array_padc = Struct(
    'flags_type' / Computed(lambda ctx: (ctx._.flags >> 32) & 0xffffffff),
    'type' / Computed(lambda ctx: kcdata_types_enum.decmapping[ctx.flags_type]),
    'count' / Computed(lambda ctx: ctx._.flags & 0xffffffff),
    'name' / Computed(lambda ctx: predefined_names[ctx.type]),
    'obj' / Array(this.count, LazyBound(lambda: Switch(
        lambda ctx: ctx.type,
        kcdata_types_structures,
        default=GreedyBytes
    ))),
    Padding(0xc),
)
type_container_begin = Struct(
    'obj' / kcdata_types_enum,
    'name' / Computed(lambda ctx: predefined_names[ctx.obj]),
    'unique_id' / Computed(lambda ctx: ctx._.flags),
)
kernelcache_load_info = Struct(
    predefined_name_substruct,
    'obj' / Struct(
        'imageLoadAddress' / Int64ul,
        'imageUUID' / Array(16, Byte),
    ),
)
task_snapshot = Struct(
    predefined_name_substruct,
    'obj' / Struct(
        'ts_unique_pid' / Int64ul,
        'ts_ss_flags' / Int64ul,
        'ts_user_time_in_terminated_thre' / Int64ul,
        'ts_system_time_in_terminated_th' / Int64ul,
        'ts_p_start_sec' / Int64ul,
        'ts_task_size' / Int64ul,
        'ts_max_resident_size' / Int64ul,
        'ts_suspend_count' / Int32ul,
        'ts_faults' / Int32ul,
        'ts_pageins' / Int32ul,
        'ts_cow_faults' / Int32ul,
        'ts_was_throttled' / Int32ul,
        'ts_did_throttle' / Int32ul,
        'ts_latency_qos' / Int32ul,
        'ts_pid' / Int32ul,
        'ts_p_comm' / Padded(32, CString('utf8')),
    ),
)
jetsam_coalition = Struct(predefined_name_substruct, 'obj' / Int64ul)
STACKSHOT_IO_NUM_PRIORITIES = 4
io_statistics = Struct(
    predefined_name_substruct,
    'obj' / Struct(
        'ss_disk_reads_count' / Int64ul,
        'ss_disk_reads_size' / Int64ul,
        'ss_disk_writes_count' / Int64ul,
        'ss_disk_writes_size' / Int64ul,
        'ss_io_priority_count' / Array(STACKSHOT_IO_NUM_PRIORITIES, Int64ul),
        'ss_io_priority_size' / Array(STACKSHOT_IO_NUM_PRIORITIES, Int64ul),
        'ss_paging_count' / Int64ul,
        'ss_paging_size' / Int64ul,
        'ss_non_paging_count' / Int32ul,
        'ss_non_paging_size' / Int32ul,
        'ss_data_count' / Int32ul,
        'ss_data_size' / Int32ul,
        'ss_metadata_count' / Int32ul,
        'ss_metadata_size' / Int32ul,
    ),
)
task_cpu_architecture = Struct(
    predefined_name_substruct,
    'obj' / Struct(
        'cputype' / Int32ul,
        'cpusubtype' / Int32ul,
    ),
)
thread_snapshot = Struct(
    predefined_name_substruct,
    'obj' / Struct(
        'ths_thread_id' / Int64ul,
        'ths_wait_event' / Int64ul,
        'ths_continuation' / Int64ul,
        'ths_total_syscalls' / Int64ul,
        'ths_voucher_identifier' / Int64ul,
        'ths_dqserialnum' / Int64ul,
        'ths_user_time' / Int64ul,
        'ths_sys_time' / Int64ul,
        'ths_ss_flags' / Int64ul,
        'ths_last_run_time' / Int64ul,
        'ths_last_made_runnable_time' / Int64ul,
        'ths_state' / Int32ul,
        'ths_sched_flags' / Int32ul,
        'ths_base_priority' / Int16ul,
        'ths_sched_priority' / Int16ul,
        'ths_eqos' / Byte,
        'ths_rqos' / Byte,
        'ths_rqos_override' / Byte,
        'ths_io_tier' / Byte,
        'ths_thread_t' / Int64ul,
        'ths_requested_policy' / Int64ul,
        'ths_effective_policy' / Int64ul,
    ),
)
pth_name = Struct(predefined_name_substruct, 'obj' / Padded(64, CString('utf8')))
cpu_times = Struct(
    predefined_name_substruct,
    'obj' / Struct(
        'user_usec' / Int64ul,
        'system_usec' / Int64ul,
        'runnable_usec' / Int64ul,
    ),
)
thread_group = Struct(predefined_name_substruct, 'obj' / Int64ul)
kernel_stack_frames = Struct(predefined_name_substruct, 'obj' / Struct('lr' / Int64ul))
dyld_load_info64 = Struct(
    predefined_name_substruct,
    'obj' / Struct(
        'imageLoadAddress' / Int64ul,
        'imageUUID' / Array(16, Byte),
    ),
)
user_stack_frames = Struct(predefined_name_substruct, 'obj' / Struct('lr' / Int64ul))
jetsam_coalition_snapshot = Struct(
    predefined_name_substruct,
    'obj' / Struct(
        'jcs_id' / Int64ul,
        'jcs_flags' / Int64ul,
        'jcs_thread_group' / Int64ul,
        'jcs_leader_task_uniqueid' / Int64ul,
    ),
)
donating_pids = Struct(predefined_name_substruct, 'obj' / Int32ul)
dispatch_queue_label = Struct(predefined_name_substruct, 'obj' / CString('utf8'))
stackshot_fault_stats = Struct(
    predefined_name_substruct,
    'obj' / Struct(
        'sfs_pages_faulted_in' / Int32ul,
        'sfs_time_spent_faulting' / Int64ul,
        'sfs_system_max_fault_time' / Int64ul,
        'sfs_stopped_faulting' / Byte,
    )
)

kcdata_types_structures = {
    kcdata_types_enum.KCDATA_TYPE_UINT32_DESC: uint32_desc,
    kcdata_types_enum.KCDATA_TYPE_UINT64_DESC: uint64_desc,
    kcdata_types_enum.STACKSHOT_KCTYPE_JETSAM_LEVEL: jetsam_level,
    kcdata_types_enum.STACKSHOT_KCTYPE_THREAD_POLICY_VERSION: thread_policy_version,
    kcdata_types_enum.STACKSHOT_KCTYPE_KERN_PAGE_SIZE: kernel_page_size,
    kcdata_types_enum.STACKSHOT_KCTYPE_OSVERSION: osversion,
    kcdata_types_enum.STACKSHOT_KCTYPE_BOOTARGS: boot_args,
    kcdata_types_enum.KCDATA_TYPE_TIMEBASE: mach_timebase_info,
    kcdata_types_enum.KCDATA_TYPE_MACH_ABSOLUTE_TIME: mach_absolute_time,
    kcdata_types_enum.KCDATA_TYPE_USECS_SINCE_EPOCH: usecs_since_epoch,
    kcdata_types_enum.STACKSHOT_KCTYPE_SHAREDCACHE_LOADINFO: shared_cache_dyld_load_info,
    kcdata_types_enum.KCDATA_TYPE_ARRAY_PAD0: type_array_pad0,
    kcdata_types_enum.KCDATA_TYPE_ARRAY_PAD4: type_array_pad4,
    kcdata_types_enum.KCDATA_TYPE_ARRAY_PAD8: type_array_pad8,
    kcdata_types_enum.KCDATA_TYPE_ARRAY_PADc: type_array_padc,
    kcdata_types_enum.STACKSHOT_KCTYPE_THREAD_GROUP_SNAPSHOT: thread_group_snapshot,
    kcdata_types_enum.KCDATA_TYPE_CONTAINER_BEGIN: type_container_begin,
    kcdata_types_enum.STACKSHOT_KCTYPE_KERNELCACHE_LOADINFO: kernelcache_load_info,
    kcdata_types_enum.STACKSHOT_KCTYPE_TASK_SNAPSHOT: task_snapshot,
    kcdata_types_enum.STACKSHOT_KCTYPE_JETSAM_COALITION: jetsam_coalition,
    kcdata_types_enum.STACKSHOT_KCTYPE_IO_STATISTICS: io_statistics,
    kcdata_types_enum.STACKSHOT_KCTYPE_TASK_CPU_ARCHITECTURE: task_cpu_architecture,
    kcdata_types_enum.STACKSHOT_KCTYPE_THREAD_SNAPSHOT: thread_snapshot,
    kcdata_types_enum.STACKSHOT_KCTYPE_THREAD_NAME: pth_name,
    kcdata_types_enum.STACKSHOT_KCTYPE_CPU_TIMES: cpu_times,
    kcdata_types_enum.STACKSHOT_KCTYPE_THREAD_GROUP: thread_group,
    kcdata_types_enum.STACKSHOT_KCTYPE_KERN_STACKLR64: kernel_stack_frames,
    kcdata_types_enum.KCDATA_TYPE_LIBRARY_LOADINFO64: dyld_load_info64,
    kcdata_types_enum.STACKSHOT_KCTYPE_USER_STACKLR64: user_stack_frames,
    kcdata_types_enum.STACKSHOT_KCTYPE_JETSAM_COALITION_SNAPSHOT: jetsam_coalition_snapshot,
    kcdata_types_enum.STACKSHOT_KCTYPE_DONATING_PIDS: donating_pids,
    kcdata_types_enum.STACKSHOT_KCTYPE_THREAD_DISPATCH_QUEUE_LABEL: dispatch_queue_label,
    kcdata_types_enum.STACKSHOT_KCTYPE_STACKSHOT_FAULT_STATS: stackshot_fault_stats,
    kcdata_types_enum.KCDATA_BUFFER_BEGIN_STACKSHOT: Struct(predefined_name_substruct),
    kcdata_types_enum.KCDATA_TYPE_CONTAINER_END: Pass,
    kcdata_types_enum.KCDATA_TYPE_BUFFER_END: Pass,
}

kcdata_item = Struct(
    'type' / kcdata_types_enum,
    'size' / Int32ul,
    'flags' / Int64ul,
    'data' / FixedSized(lambda ctx: ctx.size, Switch(
        lambda ctx: ctx.type, kcdata_types_structures, default=GreedyBytes
    ))
)

kcdata = GreedyRange(kcdata_item)


def clean(d):
    if isinstance(d, dict):
        return {k: clean(v) for k, v in d.items() if not k.startswith('_')}
    elif isinstance(d, list):
        return [clean(v) for v in d]
    else:
        return d


def jsonify_parsed_stackshot(stackshot, root=None, index=0):
    current_index = index
    while True:
        item = stackshot[current_index]
        current_index += 1
        if item['type'] == kcdata_types_enum.KCDATA_BUFFER_BEGIN_STACKSHOT:
            # Stackshot root, return no more parsing required after this.
            root[item['data']['name']] = {}
            jsonify_parsed_stackshot(stackshot, root[item['data']['name']], current_index)
            return
        elif str(item['type']).startswith('KCDATA_TYPE_ARRAY_PAD'):
            root[item['data']['name']] = [i['obj'] for i in item['data']['obj']]
        elif item['type'] == kcdata_types_enum.KCDATA_TYPE_CONTAINER_BEGIN:
            # Each container creates an entry in the container's dictionary with its unique id.
            if item['data']['name'] not in root:
                root[item['data']['name']] = {}
            root[item['data']['name']][item['data']['unique_id']] = {}
            current_index = jsonify_parsed_stackshot(stackshot, root[item['data']['name']][item['data']['unique_id']],
                                                     current_index)
        elif item['type'] == kcdata_types_enum.KCDATA_TYPE_CONTAINER_END:
            return current_index
        elif item['type'] == kcdata_types_enum.KCDATA_TYPE_BUFFER_END:
            return
        else:
            root[item['data']['name']] = item['data']['obj']


class CoreProfileSessionTap(Tap):
    IDENTIFIER = 'com.apple.instruments.server.services.coreprofilesessiontap'

    def __init__(self, dvt: DvtSecureSocketProxyService):
        self.dvt = dvt

        config = {
            'tc': [{
                'csd': 128,  # Callstack frame depth.
                'kdf2': {67895296, 117440512, 50462720, 67174400, 50397184, 68026368},  # Kdebug filter.
                'ta': [[3], [0], [2], [1, 1, 0]],  # Actions.
                'tk': 3,  # Kind.
                'uuid': 'E3C5CEBE-A8A8-417C-8DC9-18E721D774B5'  # UUID.
            }],  # Triggers configs
            'rp': 100,  # Recording priority
            'bm': 0,  # Buffer mode.
        }
        super().__init__(dvt, self.IDENTIFIER, config)

    def __iter__(self):
        while True:
            data = self._channel.receive_message()
            if not data.startswith(b'\x07\x58\xa2\x59'):
                continue
            parsed = kcdata.parse(data)
            # Required for removing streams from construct output.
            stackshot = clean(parsed)
            root = {}
            jsonify_parsed_stackshot(stackshot, root)
            yield root