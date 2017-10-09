import mWindowsAPI;

class cWindowsDefine(object):
  def __init__(oWindowsDefine, uValue, sName, sDescription, sTypeId, sSecurityImpact):
    oWindowsDefine.uValue = uValue;
    oWindowsDefine.sName = sName;
    oWindowsDefine.sDescription = sDescription;
    oWindowsDefine.sTypeId = sTypeId;
    oWindowsDefine.sSecurityImpact = sSecurityImpact;

aoWindowsDefines = [];
def fAddWindowsDefine(sName, sDescription = None, sTypeId = None, sSecurityImpact = None):
  assert hasattr(mWindowsAPI, sName), \
      "Cannot find windows define %s" % repr(sName);
  aoWindowsDefines.append(cWindowsDefine(
    uValue = getattr(mWindowsAPI, sName),
    sName = sName,
    sDescription = sDescription,
    sTypeId = sTypeId or sName,
    sSecurityImpact = sSecurityImpact,
  ));

fAddWindowsDefine("STATUS_SUCCESS",
  sDescription =    "The operation completed successfully.");
fAddWindowsDefine("STATUS_ABANDONED",
  sDescription =    "The caller attempted to wait for a mutex that has been abandoned.");
fAddWindowsDefine("STATUS_USER_APC",
  sDescription =    "A user-mode APC was delivered before the given Interval expired.");
fAddWindowsDefine("STATUS_ALERTED",
  sDescription =    "The delay completed because the thread was alerted.");
fAddWindowsDefine("STATUS_TIMEOUT",
  sDescription =    "The given Timeout interval expired.");
fAddWindowsDefine("STATUS_PENDING",
  sDescription =    "The operation that was requested is pending completion.");
fAddWindowsDefine("STATUS_REPARSE",
  sDescription =    "A reparse should be performed by the Object Manager because the name of the file resulted in a symbolic link.");
fAddWindowsDefine("STATUS_MORE_ENTRIES",
  sDescription =    "Returned by enumeration APIs to indicate more information is available to successive calls.");
fAddWindowsDefine("STATUS_NOT_ALL_ASSIGNED",
  sDescription =    "Indicates not all privileges or groups that are referenced are assigned to the caller. This allows, for example, all privileges to be disabled without having to know exactly which privileges are assigned.");
fAddWindowsDefine("STATUS_SOME_NOT_MAPPED",
  sDescription =    "Some of the information to be translated has not been translated.");
fAddWindowsDefine("STATUS_OPLOCK_BREAK_IN_PROGRESS",
  sDescription =    "An open/create operation completed while an opportunistic lock (oplock) break is underway.");
fAddWindowsDefine("STATUS_VOLUME_MOUNTED",
  sDescription =    "A new volume has been mounted by a file system.");
fAddWindowsDefine("STATUS_RXACT_COMMITTED",
  sDescription =    "This success level status indicates that the transaction state already exists for the registry subtree but that a transaction commit was previously aborted. The commit has now been completed.");
fAddWindowsDefine("STATUS_NOTIFY_CLEANUP",
  sDescription =    "Indicates that a notify change request has been completed due to closing the handle that made the notify change request.");
fAddWindowsDefine("STATUS_NOTIFY_ENUM_DIR",
  sDescription =    "Indicates that a notify change request is being completed and that the information is not being returned in the caller's buffer. The caller now needs to enumerate the files to find the changes.");
fAddWindowsDefine("STATUS_NO_QUOTAS_FOR_ACCOUNT",
  sDescription =    "No system quota limits are specifically set for this account.");
fAddWindowsDefine("STATUS_PRIMARY_TRANSPORT_CONNECT_FAILED",
  sDescription =    "An attempt was made to connect to the remote server %hs on the primary transport, but the connection failed. The computer WAS able to connect on a secondary transport.");
fAddWindowsDefine("STATUS_PAGE_FAULT_TRANSITION",
  sDescription =    "The page fault was a transition fault.");
fAddWindowsDefine("STATUS_PAGE_FAULT_DEMAND_ZERO",
  sDescription =    "The page fault was a demand zero fault.");
fAddWindowsDefine("STATUS_PAGE_FAULT_COPY_ON_WRITE",
  sDescription =    "The page fault was a copy-on-write fault.");
fAddWindowsDefine("STATUS_PAGE_FAULT_GUARD_PAGE",
  sDescription =    "The page fault was a guard page fault.");
fAddWindowsDefine("STATUS_PAGE_FAULT_PAGING_FILE",
  sDescription =    "The page fault was satisfied by reading from a secondary storage device.");
fAddWindowsDefine("STATUS_CACHE_PAGE_LOCKED",
  sDescription =    "The cached page was locked during operation.");
fAddWindowsDefine("STATUS_CRASH_DUMP",
  sDescription =    "The crash dump exists in a paging file.");
fAddWindowsDefine("STATUS_BUFFER_ALL_ZEROS",
  sDescription =    "The specified buffer contains all zeros.");
fAddWindowsDefine("STATUS_REPARSE_OBJECT",
  sDescription =    "A reparse should be performed by the Object Manager because the name of the file resulted in a symbolic link.");
fAddWindowsDefine("STATUS_RESOURCE_REQUIREMENTS_CHANGED",
  sDescription =    "The device has succeeded a query-stop and its resource requirements have changed.");
fAddWindowsDefine("STATUS_TRANSLATION_COMPLETE",
  sDescription =    "The translator has translated these resources into the global space and no additional translations should be performed.");
fAddWindowsDefine("STATUS_DS_MEMBERSHIP_EVALUATED_LOCALLY",
  sDescription =    "The directory service evaluated group memberships locally, because it was unable to contact a global catalog server.");
fAddWindowsDefine("STATUS_NOTHING_TO_TERMINATE",
  sDescription =    "A process being terminated has no threads to terminate.");
fAddWindowsDefine("STATUS_PROCESS_NOT_IN_JOB",
  sDescription =    "The specified process is not part of a job.");
fAddWindowsDefine("STATUS_PROCESS_IN_JOB",
  sDescription =    "The specified process is part of a job.");
fAddWindowsDefine("STATUS_VOLSNAP_HIBERNATE_READY",
  sDescription =    "The system is now ready for hibernation.");
fAddWindowsDefine("STATUS_FSFILTER_OP_COMPLETED_SUCCESSFULLY",
  sDescription =    "A file system or file system filter driver has successfully completed an FsFilter operation.");
fAddWindowsDefine("STATUS_INTERRUPT_VECTOR_ALREADY_CONNECTED",
  sDescription =    "The specified interrupt vector was already connected.");
fAddWindowsDefine("STATUS_INTERRUPT_STILL_CONNECTED",
  sDescription =    "The specified interrupt vector is still connected.");
fAddWindowsDefine("STATUS_PROCESS_CLONED",
  sDescription =    "The current process is a cloned process.");
fAddWindowsDefine("STATUS_FILE_LOCKED_WITH_ONLY_READERS",
  sDescription =    "The file was locked and all users of the file can only read.");
fAddWindowsDefine("STATUS_FILE_LOCKED_WITH_WRITERS",
  sDescription =    "The file was locked and at least one user of the file can write.");
fAddWindowsDefine("STATUS_RESOURCEMANAGER_READ_ONLY",
  sDescription =    "The specified ResourceManager made no changes or updates to the resource under this transaction.");
fAddWindowsDefine("STATUS_WAIT_FOR_OPLOCK",
  sDescription =    "An operation is blocked and waiting for an oplock.");
fAddWindowsDefine("DBG_EXCEPTION_HANDLED",
  sDescription =    "Debugger handled the exception.");
fAddWindowsDefine("DBG_CONTINUE",
  sDescription =    "The debugger continued.");
fAddWindowsDefine("ERROR_SUCCESS",
  sDescription =    "The operation completed successfully.");
fAddWindowsDefine("STATUS_FLT_IO_COMPLETE",
  sDescription =    "The IO was completed by a filter.");
fAddWindowsDefine("STATUS_OBJECT_NAME_EXISTS",
  sDescription =    "An attempt was made to create an object but the object name already exists.");
fAddWindowsDefine("STATUS_THREAD_WAS_SUSPENDED",
  sDescription =    "A thread termination occurred while the thread was suspended. The thread resumed, and termination proceeded.");
fAddWindowsDefine("STATUS_WORKING_SET_LIMIT_RANGE",
  sDescription =    "An attempt was made to set the working set minimum or maximum to values that are outside the allowable range.");
fAddWindowsDefine("STATUS_IMAGE_NOT_AT_BASE",
  sDescription =    "An image file could not be mapped at the address that is specified in the image file. Local fixes must be performed on this image.");
fAddWindowsDefine("STATUS_RXACT_STATE_CREATED",
  sDescription =    "This informational level status indicates that a specified registry subtree transaction state did not yet exist and had to be created.");
fAddWindowsDefine("STATUS_SEGMENT_NOTIFICATION",
  sDescription =    "A virtual DOS machine (VDM) is loading, unloading, or moving an MS-DOS or Win16 program segment image. An exception is raised so that a debugger can load, unload, or track symbols and breakpoints within these 16-bit segments.");
fAddWindowsDefine("STATUS_LOCAL_USER_SESSION_KEY",
  sDescription =    "A user session key was requested for a local remote procedure call (RPC) connection. The session key that is returned is a constant value and not unique to this connection.");
fAddWindowsDefine("STATUS_BAD_CURRENT_DIRECTORY",
  sDescription =    "The process cannot switch to the startup current directory %hs. Select OK to set the current directory to %hs, or select CANCEL to exit.");
fAddWindowsDefine("STATUS_SERIAL_MORE_WRITES",
  sDescription =    "A serial I/O operation was completed by another write to a serial port. (The IOCTL_SERIAL_XOFF_COUNTER reached zero.)");
fAddWindowsDefine("STATUS_REGISTRY_RECOVERED",
  sDescription =    "One of the files that contains the system registry data had to be recovered by using a log or alternate copy. The recovery was successful.");
fAddWindowsDefine("STATUS_FT_READ_RECOVERY_FROM_BACKUP",
  sDescription =    "To satisfy a read request, the Windows NT operating system fault-tolerant file system successfully read the requested data from a redundant copy. This was done because the file system encountered a failure on a member of the fault-tolerant volume but was unable to reassign the failing area of the device.");
fAddWindowsDefine("STATUS_FT_WRITE_RECOVERY",
  sDescription =    "To satisfy a write request, the Windows NT fault-tolerant file system successfully wrote a redundant copy of the information. This was done because the file system encountered a failure on a member of the fault-tolerant volume but was unable to reassign the failing area of the device.");
fAddWindowsDefine("STATUS_SERIAL_COUNTER_TIMEOUT",
  sDescription =    "A serial I/O operation completed because the time-out period expired. (The IOCTL_SERIAL_XOFF_COUNTER had not reached zero.)");
fAddWindowsDefine("STATUS_NULL_LM_PASSWORD",
  sDescription =    "The Windows password is too complex to be converted to a LAN Manager password. The LAN Manager password that returned is a NULL string.");
fAddWindowsDefine("STATUS_IMAGE_MACHINE_TYPE_MISMATCH",
  sDescription =    "The image file %hs is valid but is for a machine type other than the current machine. Select OK to continue, or CANCEL to fail the DLL load.");
fAddWindowsDefine("STATUS_RECEIVE_PARTIAL",
  sDescription =    "The network transport returned partial data to its client. The remaining data will be sent later.");
fAddWindowsDefine("STATUS_RECEIVE_EXPEDITED",
  sDescription =    "The network transport returned data to its client that was marked as expedited by the remote system.");
fAddWindowsDefine("STATUS_RECEIVE_PARTIAL_EXPEDITED",
  sDescription =    "The network transport returned partial data to its client and this data was marked as expedited by the remote system. The remaining data will be sent later.");
fAddWindowsDefine("STATUS_EVENT_DONE",
  sDescription =    "The TDI indication has completed successfully.");
fAddWindowsDefine("STATUS_EVENT_PENDING",
  sDescription =    "The TDI indication has entered the pending state.");
fAddWindowsDefine("STATUS_CHECKING_FILE_SYSTEM",
  sDescription =    "Checking file system on %wZ.");
fAddWindowsDefine("STATUS_FATAL_APP_EXIT",
  sDescription =    "%hs");
fAddWindowsDefine("STATUS_PREDEFINED_HANDLE",
  sDescription =    "The specified registry key is referenced by a predefined handle.");
fAddWindowsDefine("STATUS_WAS_UNLOCKED",
  sDescription =    "The page protection of a locked page was changed to 'No Access' and the page was unlocked from memory and from the process.");
fAddWindowsDefine("STATUS_SERVICE_NOTIFICATION",
  sDescription =    "%hs");
fAddWindowsDefine("STATUS_WAS_LOCKED",
  sDescription =    "One of the pages to lock was already locked.");
fAddWindowsDefine("STATUS_LOG_HARD_ERROR",
  sDescription =    "Application popup: %1 : %2");
fAddWindowsDefine("STATUS_ALREADY_WIN32",
  sDescription =    "A Win32 process already exists.");
fAddWindowsDefine("STATUS_WX86_UNSIMULATE",
  sDescription =    "An exception status code that is used by the Win32 x86 emulation subsystem.");
fAddWindowsDefine("STATUS_WX86_CONTINUE",
  sDescription =    "An exception status code that is used by the Win32 x86 emulation subsystem.");
fAddWindowsDefine("STATUS_WX86_SINGLE_STEP",
  sDescription =    "A single step or trace operation has just been completed.",
  sTypeId =         "SingleStep");
fAddWindowsDefine("STATUS_WX86_BREAKPOINT",
  sDescription =    "An exception status code that is used by the Win32 x86 emulation subsystem.",
   sTypeId =         "Breakpoint");
fAddWindowsDefine("STATUS_WX86_EXCEPTION_CONTINUE",
  sDescription =    "An exception status code that is used by the Win32 x86 emulation subsystem.");
fAddWindowsDefine("STATUS_WX86_EXCEPTION_LASTCHANCE",
  sDescription =    "An exception status code that is used by the Win32 x86 emulation subsystem.");
fAddWindowsDefine("STATUS_WX86_EXCEPTION_CHAIN",
  sDescription =    "An exception status code that is used by the Win32 x86 emulation subsystem.");
fAddWindowsDefine("STATUS_IMAGE_MACHINE_TYPE_MISMATCH_EXE",
  sDescription =    "The image file %hs is valid but is for a machine type other than the current machine.");
fAddWindowsDefine("STATUS_NO_YIELD_PERFORMED",
  sDescription =    "A yield execution was performed and no thread was available to run.");
fAddWindowsDefine("STATUS_TIMER_RESUME_IGNORED",
  sDescription =    "The resume flag to a timer API was ignored.");
fAddWindowsDefine("STATUS_ARBITRATION_UNHANDLED",
  sDescription =    "The arbiter has deferred arbitration of these resources to its parent.");
fAddWindowsDefine("STATUS_CARDBUS_NOT_SUPPORTED",
  sDescription =    "The device has detected a CardBus card in its slot.");
fAddWindowsDefine("STATUS_WX86_CREATEWX86TIB",
  sDescription =    "An exception status code that is used by the Win32 x86 emulation subsystem.");
fAddWindowsDefine("STATUS_MP_PROCESSOR_MISMATCH",
  sDescription =    "The CPUs in this multiprocessor system are not all the same revision level. To use all processors, the operating system restricts itself to the features of the least capable processor in the system. If problems occur with this system, contact the CPU manufacturer to see if this mix of processors is supported.");
fAddWindowsDefine("STATUS_HIBERNATED",
  sDescription =    "The system was put into hibernation.");
fAddWindowsDefine("STATUS_RESUME_HIBERNATION",
  sDescription =    "The system was resumed from hibernation.");
fAddWindowsDefine("STATUS_FIRMWARE_UPDATED",
  sDescription =    "Windows has detected that the system firmware (BIOS) was updated [previous firmware date = %2, current firmware date %3].");
fAddWindowsDefine("STATUS_DRIVERS_LEAKING_LOCKED_PAGES",
  sDescription =    "A device driver is leaking locked I/O pages and is causing system degradation. The system has automatically enabled the tracking code to try and catch the culprit.");
fAddWindowsDefine("STATUS_MESSAGE_RETRIEVED",
  sDescription =    "The ALPC message being canceled has already been retrieved from the queue on the other side.");
fAddWindowsDefine("STATUS_SYSTEM_POWERSTATE_TRANSITION",
  sDescription =    "The system power state is transitioning from %2 to %3.");
fAddWindowsDefine("STATUS_ALPC_CHECK_COMPLETION_LIST",
  sDescription =    "The receive operation was successful. Check the ALPC completion list for the received message.");
fAddWindowsDefine("STATUS_SYSTEM_POWERSTATE_COMPLEX_TRANSITION",
  sDescription =    "The system power state is transitioning from %2 to %3 but could enter %4.");
fAddWindowsDefine("STATUS_ACCESS_AUDIT_BY_POLICY",
  sDescription =    "Access to %1 is monitored by policy rule %2.");
fAddWindowsDefine("STATUS_ABANDON_HIBERFILE",
  sDescription =    "A valid hibernation file has been invalidated and should be abandoned.");
fAddWindowsDefine("STATUS_BIZRULES_NOT_ENABLED",
  sDescription =    "Business rule scripts are disabled for the calling application.");
fAddWindowsDefine("STATUS_WAKE_SYSTEM",
  sDescription =    "The system has awoken.");
fAddWindowsDefine("STATUS_DS_SHUTTING_DOWN",
  sDescription =    "The directory service is shutting down.");
fAddWindowsDefine("DBG_REPLY_LATER",
  sDescription =    "Debugger will reply later.");
fAddWindowsDefine("DBG_UNABLE_TO_PROVIDE_HANDLE",
  sDescription =    "Debugger cannot provide a handle.");
fAddWindowsDefine("DBG_TERMINATE_THREAD",
  sDescription =    "Debugger terminated the thread.");
fAddWindowsDefine("DBG_TERMINATE_PROCESS",
  sDescription =    "Debugger terminated the process.");
fAddWindowsDefine("DBG_CONTROL_C",
  sDescription =    "Debugger obtained control of C.");
fAddWindowsDefine("DBG_PRINTEXCEPTION_C",
  sDescription =    "Debugger printed an exception on control C.");
fAddWindowsDefine("DBG_RIPEXCEPTION",
  sDescription =    "Debugger received a RIP exception.");
fAddWindowsDefine("DBG_CONTROL_BREAK",
  sDescription =    "Debugger received a control break.");
fAddWindowsDefine("DBG_COMMAND_EXCEPTION",
  sDescription =    "Debugger command communication exception.");
fAddWindowsDefine("RPC_NT_UUID_LOCAL_ONLY",
  sDescription =    "A UUID that is valid only on this computer has been allocated.");
fAddWindowsDefine("RPC_NT_SEND_INCOMPLETE",
  sDescription =    "Some data remains to be sent in the request buffer.");
fAddWindowsDefine("WRT_ORIGINATE_ERROR_EXCEPTION",
  sDescription =    "A Windows Run-time originate error was encountered",
  sTypeId =         "WRTOriginate");
fAddWindowsDefine("WRT_TRANSFORM_ERROR_EXCEPTION",
  sDescription =    "A Windows Run-time transform error was encountered",
  sTypeId =         "WRTTransform");
fAddWindowsDefine("STATUS_CTX_CDM_CONNECT",
  sDescription =    "The Client Drive Mapping Service has connected on Terminal Connection.");
fAddWindowsDefine("STATUS_CTX_CDM_DISCONNECT",
  sDescription =    "The Client Drive Mapping Service has disconnected on Terminal Connection.");
fAddWindowsDefine("STATUS_SXS_RELEASE_ACTIVATION_CONTEXT",
  sDescription =    "A kernel mode component is releasing a reference on an activation context.");
fAddWindowsDefine("STATUS_RECOVERY_NOT_NEEDED",
  sDescription =    "The transactional resource manager is already consistent. Recovery is not needed.");
fAddWindowsDefine("STATUS_RM_ALREADY_STARTED",
  sDescription =    "The transactional resource manager has already been started.");
fAddWindowsDefine("STATUS_LOG_NO_RESTART",
  sDescription =    "The log service encountered a log stream with no restart area.");
fAddWindowsDefine("STATUS_VIDEO_DRIVER_DEBUG_REPORT_REQUEST",
  sDescription =    "The %hs display driver has detected a failure and recovered from it. Some graphical operations might have failed. The next time you restart the machine, a dialog box appears, giving you an opportunity to upload data about this failure to Microsoft.");
fAddWindowsDefine("STATUS_GRAPHICS_PARTIAL_DATA_POPULATED",
  sDescription =    "The specified buffer is not big enough to contain the entire requested dataset. Partial data is populated up to the size of the buffer. The caller needs to provide a buffer of the size as specified in the partially populated buffer's content (interface specific).");
fAddWindowsDefine("STATUS_GRAPHICS_DRIVER_MISMATCH",
  sDescription =    "The kernel driver detected a version mismatch between it and the user mode driver.");
fAddWindowsDefine("STATUS_GRAPHICS_MODE_NOT_PINNED",
  sDescription =    "No mode is pinned on the specified VidPN source/target.");
fAddWindowsDefine("STATUS_GRAPHICS_NO_PREFERRED_MODE",
  sDescription =    "The specified mode set does not specify a preference for one of its modes.");
fAddWindowsDefine("STATUS_GRAPHICS_DATASET_IS_EMPTY",
  sDescription =    "The specified dataset (for example, mode set, frequency range set, descriptor set, or topology) is empty.");
fAddWindowsDefine("STATUS_GRAPHICS_NO_MORE_ELEMENTS_IN_DATASET",
  sDescription =    "The specified dataset (for example, mode set, frequency range set, descriptor set, or topology) does not contain any more elements.");
fAddWindowsDefine("STATUS_GRAPHICS_PATH_CONTENT_GEOMETRY_TRANSFORMATION_NOT_PINNED",
  sDescription =    "The specified content transformation is not pinned on the specified VidPN present path.");
fAddWindowsDefine("STATUS_GRAPHICS_UNKNOWN_CHILD_STATUS",
  sDescription =    "The child device presence was not reliably detected.");
fAddWindowsDefine("STATUS_GRAPHICS_LEADLINK_START_DEFERRED",
  sDescription =    "Starting the lead adapter in a linked configuration has been temporarily deferred.");
fAddWindowsDefine("STATUS_GRAPHICS_POLLING_TOO_FREQUENTLY",
  sDescription =    "The display adapter is being polled for children too frequently at the same polling level.");
fAddWindowsDefine("STATUS_GRAPHICS_START_DEFERRED",
  sDescription =    "Starting the adapter has been temporarily deferred.");
fAddWindowsDefine("STATUS_NDIS_INDICATION_REQUIRED",
  sDescription =    "The request will be completed later by an NDIS status indication.");
fAddWindowsDefine("MS_VC_EXCEPTION",
  sDescription =    "The thread throwing the exception is being given a name");
fAddWindowsDefine("STATUS_GUARD_PAGE_VIOLATION",
  sDescription =    "A page of memory that marks the end of a data structure, such as a stack or an array, has been accessed.",
  sTypeId =         "GuardPage",
                             sSecurityImpact = "May be a security issue, but probably not exploitable");
fAddWindowsDefine("STATUS_DATATYPE_MISALIGNMENT",
  sDescription =    "A data type misalignment was detected in a load or store instruction.",
  sTypeId =         "DataMisalign",
                             sSecurityImpact = "May be a security issue");
fAddWindowsDefine("STATUS_BREAKPOINT",
  sDescription =    "A breakpoint has been reached.",
  sTypeId =         "Breakpoint");
fAddWindowsDefine("STATUS_SINGLE_STEP",
  sDescription =    "A single step or trace operation has just been completed.",
  sTypeId =         "SingleStep");
fAddWindowsDefine("STATUS_BUFFER_OVERFLOW",
  sDescription =    "The data was too large to fit into the specified buffer.");
fAddWindowsDefine("STATUS_NO_MORE_FILES",
  sDescription =    "No more files were found which match the file specification.");
fAddWindowsDefine("STATUS_WAKE_SYSTEM_DEBUGGER",
  sDescription =    "The system debugger was awakened by an interrupt.");
fAddWindowsDefine("STATUS_HANDLES_CLOSED",
  sDescription =    "Handles to objects have been automatically closed because of the requested operation.");
fAddWindowsDefine("STATUS_NO_INHERITANCE",
  sDescription =    "An access control list (ACL) contains no components that can be inherited.");
fAddWindowsDefine("STATUS_GUID_SUBSTITUTION_MADE",
  sDescription =    "During the translation of a globally unique identifier (GUID) to a Windows security ID (SID), no administratively defined GUID prefix was found. A substitute prefix was used, which will not compromise system security. However, this might provide a more restrictive access than intended.");
fAddWindowsDefine("STATUS_PARTIAL_COPY",
  sDescription =    "Because of protection conflicts, not all the requested bytes could be copied.");
fAddWindowsDefine("STATUS_DEVICE_PAPER_EMPTY",
  sDescription =    "The printer is out of paper.");
fAddWindowsDefine("STATUS_DEVICE_POWERED_OFF",
  sDescription =    "The printer power has been turned off.");
fAddWindowsDefine("STATUS_DEVICE_OFF_LINE",
  sDescription =    "The printer has been taken offline.");
fAddWindowsDefine("STATUS_DEVICE_BUSY",
  sDescription =    "The device is currently busy.");
fAddWindowsDefine("STATUS_NO_MORE_EAS",
  sDescription =    "No more extended attributes (EAs) were found for the file.");
fAddWindowsDefine("STATUS_INVALID_EA_NAME",
  sDescription =    "The specified extended attribute (EA) name contains at least one illegal character.");
fAddWindowsDefine("STATUS_EA_LIST_INCONSISTENT",
  sDescription =    "The extended attribute (EA) list is inconsistent.");
fAddWindowsDefine("STATUS_INVALID_EA_FLAG",
  sDescription =    "An invalid extended attribute (EA) flag was set.");
fAddWindowsDefine("STATUS_VERIFY_REQUIRED",
  sDescription =    "The media has changed and a verify operation is in progress; therefore, no reads or writes can be performed to the device, except those that are used in the verify operation.");
fAddWindowsDefine("STATUS_EXTRANEOUS_INFORMATION",
  sDescription =    "The specified access control list (ACL) contained more information than was expected.");
fAddWindowsDefine("STATUS_RXACT_COMMIT_NECESSARY",
  sDescription =    "This warning level status indicates that the transaction state already exists for the registry subtree, but that a transaction commit was previously aborted. The commit has NOT been completed but has not been rolled back either; therefore, it can still be committed, if needed.");
fAddWindowsDefine("STATUS_NO_MORE_ENTRIES",
  sDescription =    "No more entries are available from an enumeration operation.");
fAddWindowsDefine("STATUS_FILEMARK_DETECTED",
  sDescription =    "A filemark was detected.");
fAddWindowsDefine("STATUS_MEDIA_CHANGED",
  sDescription =    "The media has changed.");
fAddWindowsDefine("STATUS_BUS_RESET",
  sDescription =    "An I/O bus reset was detected.");
fAddWindowsDefine("STATUS_END_OF_MEDIA",
  sDescription =    "The end of the media was encountered.");
fAddWindowsDefine("STATUS_BEGINNING_OF_MEDIA",
  sDescription =    "The beginning of a tape or partition has been detected.");
fAddWindowsDefine("STATUS_MEDIA_CHECK",
  sDescription =    "The media might have changed.");
fAddWindowsDefine("STATUS_SETMARK_DETECTED",
  sDescription =    "A tape access reached a set mark.");
fAddWindowsDefine("STATUS_NO_DATA_DETECTED",
  sDescription =    "During a tape access, the end of the data written is reached.");
fAddWindowsDefine("STATUS_REDIRECTOR_HAS_OPEN_HANDLES",
  sDescription =    "The redirector is in use and cannot be unloaded.");
fAddWindowsDefine("STATUS_SERVER_HAS_OPEN_HANDLES",
  sDescription =    "The server is in use and cannot be unloaded.");
fAddWindowsDefine("STATUS_ALREADY_DISCONNECTED",
  sDescription =    "The specified connection has already been disconnected.");
fAddWindowsDefine("STATUS_LONGJUMP",
  sDescription =    "A long jump has been executed.");
fAddWindowsDefine("STATUS_CLEANER_CARTRIDGE_INSTALLED",
  sDescription =    "A cleaner cartridge is present in the tape library.");
fAddWindowsDefine("STATUS_PLUGPLAY_QUERY_VETOED",
  sDescription =    "The Plug and Play query operation was not successful.");
fAddWindowsDefine("STATUS_UNWIND_CONSOLIDATE",
  sDescription =    "A frame consolidation has been executed.");
fAddWindowsDefine("STATUS_REGISTRY_HIVE_RECOVERED",
  sDescription =    "The registry hive (file): %hs was corrupted and it has been recovered. Some data might have been lost.");
fAddWindowsDefine("STATUS_DLL_MIGHT_BE_INSECURE",
  sDescription =    "The application is attempting to run executable code from the module %hs. This might be insecure. An alternative, %hs, is available. Should the application use the secure module %hs?");
fAddWindowsDefine("STATUS_DLL_MIGHT_BE_INCOMPATIBLE",
  sDescription =    "The application is loading executable code from the module %hs. This is secure but might be incompatible with previous releases of the operating system. An alternative, %hs, is available. Should the application use the secure module %hs?");
fAddWindowsDefine("STATUS_STOPPED_ON_SYMLINK",
  sDescription =    "The create operation stopped after reaching a symbolic link.");
fAddWindowsDefine("STATUS_DEVICE_REQUIRES_CLEANING",
  sDescription =    "The device has indicated that cleaning is necessary.");
fAddWindowsDefine("STATUS_DEVICE_DOOR_OPEN",
  sDescription =    "The device has indicated that its door is open. Further operations require it closed and secured.");
fAddWindowsDefine("STATUS_DATA_LOST_REPAIR",
  sDescription =    "Windows discovered a corruption in the file %hs. This file has now been repaired. Check if any data in the file was lost because of the corruption.");
fAddWindowsDefine("E_FAIL",
  sDescription =    "Unspecified error.");
fAddWindowsDefine("DBG_EXCEPTION_NOT_HANDLED",
  sDescription =    "Debugger did not handle the exception.");
fAddWindowsDefine("RPC_E_CALL_CANCELED",
  sDescription =    "Call was canceled by the message filter.");
fAddWindowsDefine("RPC_E_SERVER_DIED",
  sDescription =    "The callee (server [not server application]) is not available and disappeared; all connections are invalid. The call may have executed.");
fAddWindowsDefine("RPC_E_CANTTRANSMIT_CALL",
  sDescription =    "The call was not transmitted properly; the message queue was full and was not emptied after yielding.");
fAddWindowsDefine("RPC_E_SERVERFAULT",
  sDescription =    "The server threw an exception.");
fAddWindowsDefine("RPC_E_CANTCALLOUT_AGAIN",
  sDescription =    "There is no second outgoing call on same channel in DDE conversation.");
fAddWindowsDefine("RPC_E_SERVERCALL_REJECTED",
  sDescription =    "The message filter rejected the call.");
fAddWindowsDefine("RPC_E_CANTCALLOUT_ININPUTSYNCCALL",
  sDescription =    "An outgoing call cannot be made since the application is dispatching an input-synchronous call.");
fAddWindowsDefine("RPC_E_WRONG_THREAD",
  sDescription =    "The application called an interface that was marshalled for a different thread.");
fAddWindowsDefine("RPC_E_INVALID_HEADER",
  sDescription =    "OLE received a packet with an invalid header.");
fAddWindowsDefine("RPC_E_INVALID_EXTENSION",
  sDescription =    "OLE received a packet with an invalid extension.");
fAddWindowsDefine("RPC_E_UNSECURE_CALL",
  sDescription =    "Impersonate on unsecure calls is not supported.");
fAddWindowsDefine("CO_E_FAILEDTOGETTOKENINFO",
  sDescription =    "Unable to obtain user info from an access token");
fAddWindowsDefine("CO_E_NETACCESSAPIFAILED",
  sDescription =    "Either NetAccessDel or NetAccessAdd returned an error code.");
fAddWindowsDefine("CO_E_WRONGTRUSTEENAMESYNTAX",
  sDescription =    'One of the trustee strings provided by the user did not conform to the \\ syntax and it was not the "*" string"');
fAddWindowsDefine("CO_E_CONVERSIONFAILED",
  sDescription =    "Unable to convert a wide character trustee string to a multibyte trustee string");
fAddWindowsDefine("CO_E_NOMATCHINGNAMEFOUND",
  sDescription =    "Unable to find a trustee name that corresponds to a security identifier provided by the user");
fAddWindowsDefine("CO_E_FAILEDTOGENUUID",
  sDescription =    "Unable to generate a uuid.");
fAddWindowsDefine("CO_E_EXCEEDSYSACLLIMIT",
  sDescription =    "The number of ACEs in an ACL exceeds the system limit.");
fAddWindowsDefine("CO_E_ACESINWRONGORDER",
  sDescription =    "Not all the DENY_ACCESS ACEs are arranged in front of the GRANT_ACCESS ACEs in the stream.");
fAddWindowsDefine("CO_E_DECODEFAILED",
  sDescription =    "Unable to decode the ACL in the stream provided by the user");
fAddWindowsDefine("CO_E_CANCEL_DISABLED",
  sDescription =    "Call Cancellation is disabled");
fAddWindowsDefine("ERROR_INVALID_FUNCTION",
  sDescription =    "Incorrect function.");
fAddWindowsDefine("ERROR_FILE_NOT_FOUND",
  sDescription =    "The system cannot find the file specified.");
fAddWindowsDefine("ERROR_PATH_NOT_FOUND",
  sDescription =    "The system cannot find the path specified.");
fAddWindowsDefine("ERROR_TOO_MANY_OPEN_FILES",
  sDescription =    "The system cannot open the file.");
fAddWindowsDefine("ERROR_ACCESS_DENIED",
  sDescription =    "Access is denied.");
fAddWindowsDefine("ERROR_INVALID_HANDLE",
  sDescription =    "The handle is invalid.");
fAddWindowsDefine("ERROR_ARENA_TRASHED",
  sDescription =    "The storage control blocks were destroyed.");
fAddWindowsDefine("ERROR_NOT_ENOUGH_MEMORY",
  sDescription =    "Not enough storage is available to process this command.",
  sTypeId =         "OOM");
fAddWindowsDefine("ERROR_INVALID_BLOCK",
  sDescription =    "The storage control block address is invalid.");
fAddWindowsDefine("ERROR_BAD_ENVIRONMENT",
  sDescription =    "The environment is incorrect.");
fAddWindowsDefine("ERROR_BAD_FORMAT",
  sDescription =    "An attempt was made to load a program with an incorrect format.");
fAddWindowsDefine("ERROR_INVALID_ACCESS",
  sDescription =    "The access code is invalid.");
fAddWindowsDefine("ERROR_INVALID_DATA",
  sDescription =    "The data is invalid.");
fAddWindowsDefine("ERROR_OUTOFMEMORY",
  sDescription =    "Not enough storage is available to complete this operation.",
  sTypeId =         "OOM");
fAddWindowsDefine("ERROR_INVALID_DRIVE",
  sDescription =    "The system cannot find the drive specified.");
fAddWindowsDefine("ERROR_CURRENT_DIRECTORY",
  sDescription =    "The directory cannot be removed.");
fAddWindowsDefine("ERROR_NOT_SAME_DEVICE",
  sDescription =    "The system cannot move the file to a different disk drive.");
fAddWindowsDefine("ERROR_NO_MORE_FILES",
  sDescription =    "There are no more files.");
fAddWindowsDefine("ERROR_WRITE_PROTECT",
  sDescription =    "The media is write protected.");
fAddWindowsDefine("ERROR_BAD_UNIT",
  sDescription =    "The system cannot find the device specified.");
fAddWindowsDefine("ERROR_NOT_READY",
  sDescription =    "The device is not ready.");
fAddWindowsDefine("ERROR_BAD_COMMAND",
  sDescription =    "The device does not recognize the command.");
fAddWindowsDefine("ERROR_CRC",
  sDescription =    "Data error (cyclic redundancy check).");
fAddWindowsDefine("ERROR_BAD_LENGTH",
  sDescription =    "The program issued a command but the command length is incorrect.");
fAddWindowsDefine("ERROR_SEEK",
  sDescription =    "The drive cannot locate a specific area or track on the disk.");
fAddWindowsDefine("ERROR_NOT_DOS_DISK",
  sDescription =    "The specified disk or diskette cannot be accessed.");
fAddWindowsDefine("ERROR_SECTOR_NOT_FOUND",
  sDescription =    "The drive cannot find the sector requested.");
fAddWindowsDefine("ERROR_OUT_OF_PAPER",
  sDescription =    "The printer is out of paper.");
fAddWindowsDefine("ERROR_WRITE_FAULT",
  sDescription =    "The system cannot write to the specified device.");
fAddWindowsDefine("ERROR_READ_FAULT",
  sDescription =    "The system cannot read from the specified device.");
fAddWindowsDefine("ERROR_GEN_FAILURE",
  sDescription =    "A device attached to the system is not functioning.");
fAddWindowsDefine("ERROR_SHARING_VIOLATION",
  sDescription =    "The process cannot access the file because it is being used by another process.");
fAddWindowsDefine("ERROR_LOCK_VIOLATION",
  sDescription =    "The process cannot access the file because another process has locked a portion of the file.");
fAddWindowsDefine("ERROR_WRONG_DISK",
  sDescription =    "The wrong diskette is in the drive. Insert %2 (Volume Serial Number: %3) into drive %1.");
fAddWindowsDefine("ERROR_SHARING_BUFFER_EXCEEDED",
  sDescription =    "Too many files opened for sharing.");
fAddWindowsDefine("ERROR_HANDLE_EOF",
  sDescription =    "Reached the end of the file.");
fAddWindowsDefine("ERROR_HANDLE_DISK_FULL",
  sDescription =    "The disk is full.");
fAddWindowsDefine("ERROR_NOT_SUPPORTED",
  sDescription =    "The request is not supported.");
fAddWindowsDefine("ERROR_REM_NOT_LIST",
  sDescription =    "Windows cannot find the network path. Verify that the network path is correct and the destination computer is not busy or turned off. If Windows still cannot find the network path, contact your network administrator.");
fAddWindowsDefine("ERROR_DUP_NAME",
  sDescription =    "You were not connected because a duplicate name exists on the network. If joining a domain, go to System in Control Panel to change the computer name and try again. If joining a workgroup, choose another workgroup name.");
fAddWindowsDefine("ERROR_BAD_NETPATH",
  sDescription =    "The network path was not found.");
fAddWindowsDefine("ERROR_NETWORK_BUSY",
  sDescription =    "The network is busy.");
fAddWindowsDefine("ERROR_DEV_NOT_EXIST",
  sDescription =    "The specified network resource or device is no longer available.");
fAddWindowsDefine("ERROR_TOO_MANY_CMDS",
  sDescription =    "The network BIOS command limit has been reached.");
fAddWindowsDefine("ERROR_ADAP_HDW_ERR",
  sDescription =    "A network adapter hardware error occurred.");
fAddWindowsDefine("ERROR_BAD_NET_RESP",
  sDescription =    "The specified server cannot perform the requested operation.");
fAddWindowsDefine("ERROR_UNEXP_NET_ERR",
  sDescription =    "An unexpected network error occurred.");
fAddWindowsDefine("ERROR_BAD_REM_ADAP",
  sDescription =    "The remote adapter is not compatible.");
fAddWindowsDefine("ERROR_PRINTQ_FULL",
  sDescription =    "The printer queue is full.");
fAddWindowsDefine("ERROR_NO_SPOOL_SPACE",
  sDescription =    "Space to store the file waiting to be printed is not available on the server.");
fAddWindowsDefine("ERROR_PRINT_CANCELLED",
  sDescription =    "Your file waiting to be printed was deleted.");
fAddWindowsDefine("ERROR_NETNAME_DELETED",
  sDescription =    "The specified network name is no longer available.");
fAddWindowsDefine("ERROR_NETWORK_ACCESS_DENIED",
  sDescription =    "Network access is denied.");
fAddWindowsDefine("ERROR_BAD_DEV_TYPE",
  sDescription =    "The network resource type is not correct.");
fAddWindowsDefine("ERROR_BAD_NET_NAME",
  sDescription =    "The network name cannot be found.");
fAddWindowsDefine("ERROR_TOO_MANY_NAMES",
  sDescription =    "The name limit for the local computer network adapter card was exceeded.");
fAddWindowsDefine("ERROR_TOO_MANY_SESS",
  sDescription =    "The network BIOS session limit was exceeded.");
fAddWindowsDefine("ERROR_SHARING_PAUSED",
  sDescription =    "The remote server has been paused or is in the process of being started.");
fAddWindowsDefine("ERROR_REQ_NOT_ACCEP",
  sDescription =    "No more connections can be made to this remote computer at this time because there are already as many connections as the computer can accept.");
fAddWindowsDefine("ERROR_REDIR_PAUSED",
  sDescription =    "The specified printer or disk device has been paused.");
fAddWindowsDefine("ERROR_FILE_EXISTS",
  sDescription =    "The file exists.");
fAddWindowsDefine("ERROR_CANNOT_MAKE",
  sDescription =    "The directory or file cannot be created.");
fAddWindowsDefine("ERROR_FAIL_I24",
  sDescription =    "Fail on INT 24.");
fAddWindowsDefine("ERROR_OUT_OF_STRUCTURES",
  sDescription =    "Storage to process this request is not available.");
fAddWindowsDefine("ERROR_ALREADY_ASSIGNED",
  sDescription =    "The local device name is already in use.");
fAddWindowsDefine("ERROR_INVALID_PASSWORD",
  sDescription =    "The specified network password is not correct.");
fAddWindowsDefine("ERROR_INVALID_PARAMETER",
  sDescription =    "The parameter is incorrect.");
fAddWindowsDefine("ERROR_NET_WRITE_FAULT",
  sDescription =    "A write fault occurred on the network.");
fAddWindowsDefine("ERROR_NO_PROC_SLOTS",
  sDescription =    "The system cannot start another process at this time.");
fAddWindowsDefine("ERROR_TOO_MANY_SEMAPHORES",
  sDescription =    "Cannot create another system semaphore.");
fAddWindowsDefine("ERROR_EXCL_SEM_ALREADY_OWNED",
  sDescription =    "The exclusive semaphore is owned by another process.");
fAddWindowsDefine("ERROR_SEM_IS_SET",
  sDescription =    "The semaphore is set and cannot be closed.");
fAddWindowsDefine("ERROR_TOO_MANY_SEM_REQUESTS",
  sDescription =    "The semaphore cannot be set again.");
fAddWindowsDefine("ERROR_INVALID_AT_INTERRUPT_TIME",
  sDescription =    "Cannot request exclusive semaphores at interrupt time.");
fAddWindowsDefine("ERROR_SEM_OWNER_DIED",
  sDescription =    "The previous ownership of this semaphore has ended.");
fAddWindowsDefine("ERROR_SEM_USER_LIMIT",
  sDescription =    "Insert the diskette for drive %1.");
fAddWindowsDefine("ERROR_DISK_CHANGE",
  sDescription =    "The program stopped because an alternate diskette was not inserted.");
fAddWindowsDefine("ERROR_DRIVE_LOCKED",
  sDescription =    "The disk is in use or locked by another process.");
fAddWindowsDefine("ERROR_BROKEN_PIPE",
  sDescription =    "The pipe has been ended.");
fAddWindowsDefine("ERROR_OPEN_FAILED",
  sDescription =    "The system cannot open the device or file specified.");
fAddWindowsDefine("ERROR_BUFFER_OVERFLOW",
  sDescription =    "The file name is too long.");
fAddWindowsDefine("ERROR_DISK_FULL",
  sDescription =    "There is not enough space on the disk.");
fAddWindowsDefine("ERROR_NO_MORE_SEARCH_HANDLES",
  sDescription =    "No more internal file identifiers available.");
fAddWindowsDefine("ERROR_INVALID_TARGET_HANDLE",
  sDescription =    "The target internal file identifier is incorrect.");
fAddWindowsDefine("ERROR_INVALID_CATEGORY",
  sDescription =    "The IOCTL call made by the application program is not correct.");
fAddWindowsDefine("ERROR_INVALID_VERIFY_SWITCH",
  sDescription =    "The verify-on-write switch parameter value is not correct.");
fAddWindowsDefine("ERROR_BAD_DRIVER_LEVEL",
  sDescription =    "The system does not support the command requested.");
fAddWindowsDefine("ERROR_CALL_NOT_IMPLEMENTED",
  sDescription =    "This function is not supported on this system.");
fAddWindowsDefine("ERROR_SEM_TIMEOUT",
  sDescription =    "The semaphore timeout period has expired.");
fAddWindowsDefine("ERROR_INSUFFICIENT_BUFFER",
  sDescription =    "The data area passed to a system call is too small.");
fAddWindowsDefine("ERROR_INVALID_NAME",
  sDescription =    "The filename, directory name, or volume label syntax is incorrect.");
fAddWindowsDefine("ERROR_INVALID_LEVEL",
  sDescription =    "The system call level is not correct.");
fAddWindowsDefine("ERROR_NO_VOLUME_LABEL",
  sDescription =    "The disk has no volume label.");
fAddWindowsDefine("ERROR_MOD_NOT_FOUND",
  sDescription =    "The specified module could not be found.");
fAddWindowsDefine("ERROR_PROC_NOT_FOUND",
  sDescription =    "The specified procedure could not be found.");
fAddWindowsDefine("ERROR_WAIT_NO_CHILDREN",
  sDescription =    "There are no child processes to wait for.");
fAddWindowsDefine("ERROR_CHILD_NOT_COMPLETE",
  sDescription =    "The %1 application cannot be run in Win32 mode.");
fAddWindowsDefine("ERROR_DIRECT_ACCESS_HANDLE",
  sDescription =    "Attempt to use a file handle to an open disk partition for an operation other than raw disk I/O.");
fAddWindowsDefine("ERROR_NEGATIVE_SEEK",
  sDescription =    "An attempt was made to move the file pointer before the beginning of the file.");
fAddWindowsDefine("ERROR_SEEK_ON_DEVICE",
  sDescription =    "The file pointer cannot be set on the specified device or file.");
fAddWindowsDefine("ERROR_IS_JOIN_TARGET",
  sDescription =    "A JOIN or SUBST command cannot be used for a drive that contains previously joined drives.");
fAddWindowsDefine("ERROR_IS_JOINED",
  sDescription =    "An attempt was made to use a JOIN or SUBST command on a drive that has already been joined.");
fAddWindowsDefine("ERROR_IS_SUBSTED",
  sDescription =    "An attempt was made to use a JOIN or SUBST command on a drive that has already been substituted.");
fAddWindowsDefine("ERROR_NOT_JOINED",
  sDescription =    "The system tried to delete the JOIN of a drive that is not joined.");
fAddWindowsDefine("ERROR_NOT_SUBSTED",
  sDescription =    "The system tried to delete the substitution of a drive that is not substituted.");
fAddWindowsDefine("ERROR_JOIN_TO_JOIN",
  sDescription =    "The system tried to join a drive to a directory on a joined drive.");
fAddWindowsDefine("ERROR_SUBST_TO_SUBST",
  sDescription =    "The system tried to substitute a drive to a directory on a substituted drive.");
fAddWindowsDefine("ERROR_JOIN_TO_SUBST",
  sDescription =    "The system tried to join a drive to a directory on a substituted drive.");
fAddWindowsDefine("ERROR_SUBST_TO_JOIN",
  sDescription =    "The system tried to SUBST a drive to a directory on a joined drive.");
fAddWindowsDefine("ERROR_BUSY_DRIVE",
  sDescription =    "The system cannot perform a JOIN or SUBST at this time.");
fAddWindowsDefine("ERROR_SAME_DRIVE",
  sDescription =    "The system cannot join or substitute a drive to or for a directory on the same drive.");
fAddWindowsDefine("ERROR_DIR_NOT_ROOT",
  sDescription =    "The directory is not a subdirectory of the root directory.");
fAddWindowsDefine("ERROR_DIR_NOT_EMPTY",
  sDescription =    "The directory is not empty.");
fAddWindowsDefine("ERROR_IS_SUBST_PATH",
  sDescription =    "The path specified is being used in a substitute.");
fAddWindowsDefine("ERROR_IS_JOIN_PATH",
  sDescription =    "Not enough resources are available to process this command.");
fAddWindowsDefine("ERROR_PATH_BUSY",
  sDescription =    "The path specified cannot be used at this time.");
fAddWindowsDefine("ERROR_IS_SUBST_TARGET",
  sDescription =    "An attempt was made to join or substitute a drive for which a directory on the drive is the target of a previous substitute.");
fAddWindowsDefine("ERROR_SYSTEM_TRACE",
  sDescription =    "System trace information was not specified in your CONFIG.SYS file, or tracing is disallowed.");
fAddWindowsDefine("ERROR_INVALID_EVENT_COUNT",
  sDescription =    "The number of specified semaphore events for DosMuxSemWait is not correct.");
fAddWindowsDefine("ERROR_TOO_MANY_MUXWAITERS",
  sDescription =    "DosMuxSemWait did not execute; too many semaphores are already set.");
fAddWindowsDefine("ERROR_INVALID_LIST_FORMAT",
  sDescription =    "The DosMuxSemWait list is not correct.");
fAddWindowsDefine("ERROR_LABEL_TOO_LONG",
  sDescription =    "The volume label you entered exceeds the label character limit of the target file system.");
fAddWindowsDefine("ERROR_TOO_MANY_TCBS",
  sDescription =    "Cannot create another thread.");
fAddWindowsDefine("ERROR_SIGNAL_REFUSED",
  sDescription =    "The recipient process has refused the signal.");
fAddWindowsDefine("ERROR_DISCARDED",
  sDescription =    "The segment is already discarded and cannot be locked.");
fAddWindowsDefine("ERROR_NOT_LOCKED",
  sDescription =    "The segment is already unlocked.");
fAddWindowsDefine("ERROR_BAD_THREADID_ADDR",
  sDescription =    "The address for the thread ID is not correct.");
fAddWindowsDefine("ERROR_BAD_ARGUMENTS",
  sDescription =    "One or more arguments are not correct.");
fAddWindowsDefine("ERROR_BAD_PATHNAME",
  sDescription =    "The specified path is invalid.");
fAddWindowsDefine("ERROR_SIGNAL_PENDING",
  sDescription =    "A signal is already pending.");
fAddWindowsDefine("ERROR_MAX_THRDS_REACHED",
  sDescription =    "No more threads can be created in the system.");
fAddWindowsDefine("ERROR_LOCK_FAILED",
  sDescription =    "Unable to lock a region of a file.");
fAddWindowsDefine("ERROR_BUSY",
  sDescription =    "The requested resource is in use.");
fAddWindowsDefine("ERROR_DEVICE_SUPPORT_IN_PROGRESS",
  sDescription =    "Device's command support detection is in progress.");
fAddWindowsDefine("ERROR_CANCEL_VIOLATION",
  sDescription =    "A lock request was not outstanding for the supplied cancel region.");
fAddWindowsDefine("ERROR_ATOMIC_LOCKS_NOT_SUPPORTED",
  sDescription =    "The file system does not support atomic changes to the lock type.");
fAddWindowsDefine("ERROR_INVALID_SEGMENT_NUMBER",
  sDescription =    "The system detected a segment number that was not correct.");
fAddWindowsDefine("ERROR_INVALID_ORDINAL",
  sDescription =    "The operating system cannot run %1.");
fAddWindowsDefine("ERROR_ALREADY_EXISTS",
  sDescription =    "Cannot create a file when that file already exists.");
fAddWindowsDefine("ERROR_INVALID_FLAG_NUMBER",
  sDescription =    "The flag passed is not correct.");
fAddWindowsDefine("ERROR_SEM_NOT_FOUND",
  sDescription =    "The specified system semaphore name was not found.");
fAddWindowsDefine("ERROR_INVALID_STARTING_CODESEG",
  sDescription =    "The operating system cannot run %1.");
fAddWindowsDefine("ERROR_INVALID_STACKSEG",
  sDescription =    "The operating system cannot run %1.");
fAddWindowsDefine("ERROR_INVALID_MODULETYPE",
  sDescription =    "The operating system cannot run %1.");
fAddWindowsDefine("ERROR_INVALID_EXE_SIGNATURE",
  sDescription =    "Cannot run %1 in Win32 mode.");
fAddWindowsDefine("ERROR_EXE_MARKED_INVALID",
  sDescription =    "The operating system cannot run %1.");
fAddWindowsDefine("ERROR_BAD_EXE_FORMAT",
  sDescription =    "%1 is not a valid Win32 application.");
fAddWindowsDefine("ERROR_ITERATED_DATA_EXCEEDS_64k",
  sDescription =    "The operating system cannot run %1.");
fAddWindowsDefine("ERROR_INVALID_MINALLOCSIZE",
  sDescription =    "The operating system cannot run %1.");
fAddWindowsDefine("ERROR_DYNLINK_FROM_INVALID_RING",
  sDescription =    "The operating system cannot run this application program.");
fAddWindowsDefine("ERROR_IOPL_NOT_ENABLED",
  sDescription =    "The operating system is not presently configured to run this application.");
fAddWindowsDefine("ERROR_INVALID_SEGDPL",
  sDescription =    "The operating system cannot run %1.");
fAddWindowsDefine("ERROR_AUTODATASEG_EXCEEDS_64k",
  sDescription =    "The operating system cannot run this application program.");
fAddWindowsDefine("ERROR_RING2SEG_MUST_BE_MOVABLE",
  sDescription =    "The code segment cannot be greater than or equal to 64K.");
fAddWindowsDefine("ERROR_RELOC_CHAIN_XEEDS_SEGLIM",
  sDescription =    "The operating system cannot run %1.");
fAddWindowsDefine("ERROR_INFLOOP_IN_RELOC_CHAIN",
  sDescription =    "The operating system cannot run %1.");
fAddWindowsDefine("ERROR_ENVVAR_NOT_FOUND",
  sDescription =    "The system could not find the environment option that was entered.");
fAddWindowsDefine("ERROR_NO_SIGNAL_SENT",
  sDescription =    "No process in the command subtree has a signal handler.");
fAddWindowsDefine("ERROR_FILENAME_EXCED_RANGE",
  sDescription =    "The filename or extension is too long.");
fAddWindowsDefine("ERROR_RING2_STACK_IN_USE",
  sDescription =    "The ring 2 stack is in use.");
fAddWindowsDefine("ERROR_META_EXPANSION_TOO_LONG",
  sDescription =    "The global filename characters, * or ?, are entered incorrectly or too many global filename characters are specified.");
fAddWindowsDefine("ERROR_INVALID_SIGNAL_NUMBER",
  sDescription =    "The signal being posted is not correct.");
fAddWindowsDefine("ERROR_THREAD_1_INACTIVE",
  sDescription =    "The signal handler cannot be set.");
fAddWindowsDefine("ERROR_LOCKED",
  sDescription =    "The segment is locked and cannot be reallocated.");
fAddWindowsDefine("ERROR_TOO_MANY_MODULES",
  sDescription =    "Too many dynamic-link modules are attached to this program or dynamic-link module.");
fAddWindowsDefine("ERROR_NESTING_NOT_ALLOWED",
  sDescription =    "Cannot nest calls to LoadModule.");
fAddWindowsDefine("ERROR_EXE_MACHINE_TYPE_MISMATCH",
  sDescription =    "This version of %1 is not compatible with the version of Windows you're running. Check your computer's system information and then contact the software publisher.");
fAddWindowsDefine("ERROR_EXE_CANNOT_MODIFY_SIGNED_BINARY",
  sDescription =    "The image file %1 is signed, unable to modify.");
fAddWindowsDefine("ERROR_EXE_CANNOT_MODIFY_STRONG_SIGNED_BINARY",
  sDescription =    "The image file %1 is strong signed, unable to modify.");
fAddWindowsDefine("ERROR_FILE_CHECKED_OUT",
  sDescription =    "This file is checked out or locked for editing by another user.");
fAddWindowsDefine("ERROR_CHECKOUT_REQUIRED",
  sDescription =    "The file must be checked out before saving changes.");
fAddWindowsDefine("ERROR_BAD_FILE_TYPE",
  sDescription =    "The file type being saved or retrieved has been blocked.");
fAddWindowsDefine("ERROR_FILE_TOO_LARGE",
  sDescription =    "The file size exceeds the limit allowed and cannot be saved.");
fAddWindowsDefine("ERROR_FORMS_AUTH_REQUIRED",
  sDescription =    "Access Denied. Before opening files in this location, you must first add the web site to your trusted sites list, browse to the web site, and select the option to login automatically.");
fAddWindowsDefine("ERROR_VIRUS_INFECTED",
  sDescription =    "Operation did not complete successfully because the file contains a virus or potentially unwanted software.");
fAddWindowsDefine("ERROR_VIRUS_DELETED",
  sDescription =    "This file contains a virus or potentially unwanted software and cannot be opened. Due to the nature of this virus or potentially unwanted software, the file has been removed from this location.");
fAddWindowsDefine("ERROR_PIPE_LOCAL",
  sDescription =    "The pipe is local.");
fAddWindowsDefine("ERROR_BAD_PIPE",
  sDescription =    "The pipe state is invalid.");
fAddWindowsDefine("ERROR_PIPE_BUSY",
  sDescription =    "All pipe instances are busy.");
fAddWindowsDefine("ERROR_NO_DATA",
  sDescription =    "The pipe is being closed.");
fAddWindowsDefine("ERROR_PIPE_NOT_CONNECTED",
  sDescription =    "No process is on the other end of the pipe.");
fAddWindowsDefine("ERROR_MORE_DATA",
  sDescription =    "More data is available.");
fAddWindowsDefine("ERROR_VC_DISCONNECTED",
  sDescription =    "The session was canceled.");
fAddWindowsDefine("ERROR_INVALID_EA_NAME",
  sDescription =    "The specified extended attribute name was invalid.");
fAddWindowsDefine("ERROR_EA_LIST_INCONSISTENT",
  sDescription =    "The extended attributes are inconsistent.");
fAddWindowsDefine("WAIT_TIMEOUT",
  sDescription =    "The wait operation timed out.");
fAddWindowsDefine("ERROR_NO_MORE_ITEMS",
  sDescription =    "No more data is available.");
fAddWindowsDefine("ERROR_CANNOT_COPY",
  sDescription =    "The copy functions cannot be used.");
fAddWindowsDefine("ERROR_DIRECTORY",
  sDescription =    "The directory name is invalid.");
fAddWindowsDefine("ERROR_EAS_DIDNT_FIT",
  sDescription =    "The extended attributes did not fit in the buffer.");
fAddWindowsDefine("ERROR_EA_FILE_CORRUPT",
  sDescription =    "The extended attribute file on the mounted file system is corrupt.");
fAddWindowsDefine("ERROR_EA_TABLE_FULL",
  sDescription =    "The extended attribute table file is full.");
fAddWindowsDefine("ERROR_INVALID_EA_HANDLE",
  sDescription =    "The specified extended attribute handle is invalid.");
fAddWindowsDefine("ERROR_EAS_NOT_SUPPORTED",
  sDescription =    "The mounted file system does not support extended attributes.");
fAddWindowsDefine("ERROR_NOT_OWNER",
  sDescription =    "Attempt to release mutex not owned by caller.");
fAddWindowsDefine("ERROR_TOO_MANY_POSTS",
  sDescription =    "Too many posts were made to a semaphore.");
fAddWindowsDefine("ERROR_PARTIAL_COPY",
  sDescription =    "Only part of a ReadProcessMemory or WriteProcessMemory request was completed.");
fAddWindowsDefine("ERROR_OPLOCK_NOT_GRANTED",
  sDescription =    "The oplock request is denied.");
fAddWindowsDefine("ERROR_INVALID_OPLOCK_PROTOCOL",
  sDescription =    "An invalid oplock acknowledgment was received by the system.");
fAddWindowsDefine("ERROR_DISK_TOO_FRAGMENTED",
  sDescription =    "The volume is too fragmented to complete this operation.");
fAddWindowsDefine("ERROR_DELETE_PENDING",
  sDescription =    "The file cannot be opened because it is in the process of being deleted.");
fAddWindowsDefine("ERROR_INCOMPATIBLE_WITH_GLOBAL_SHORT_NAME_REGISTRY_SETTING",
  sDescription =    "Short name settings may not be changed on this volume due to the global registry setting.");
fAddWindowsDefine("ERROR_SHORT_NAMES_NOT_ENABLED_ON_VOLUME",
  sDescription =    "Short names are not enabled on this volume.");
fAddWindowsDefine("ERROR_SECURITY_STREAM_IS_INCONSISTENT",
  sDescription =    "The security stream for the given volume is in an inconsistent state. Please run CHKDSK on the volume.");
fAddWindowsDefine("ERROR_INVALID_LOCK_RANGE",
  sDescription =    "A requested file lock operation cannot be processed due to an invalid byte range.");
fAddWindowsDefine("ERROR_IMAGE_SUBSYSTEM_NOT_PRESENT",
  sDescription =    "The subsystem needed to support the image type is not present.");
fAddWindowsDefine("ERROR_NOTIFICATION_GUID_ALREADY_DEFINED",
  sDescription =    "The specified file already has a notification GUID associated with it.");
fAddWindowsDefine("ERROR_INVALID_EXCEPTION_HANDLER",
  sDescription =    "An invalid exception handler routine has been detected.");
fAddWindowsDefine("ERROR_DUPLICATE_PRIVILEGES",
  sDescription =    "Duplicate privileges were specified for the token.");
fAddWindowsDefine("ERROR_NO_RANGES_PROCESSED",
  sDescription =    "No ranges for the specified operation were able to be processed.");
fAddWindowsDefine("ERROR_NOT_ALLOWED_ON_SYSTEM_FILE",
  sDescription =    "Operation is not allowed on a file system internal file.");
fAddWindowsDefine("ERROR_DISK_RESOURCES_EXHAUSTED",
  sDescription =    "The physical resources of this disk have been exhausted.");
fAddWindowsDefine("ERROR_INVALID_TOKEN",
  sDescription =    "The token representing the data is invalid.");
fAddWindowsDefine("ERROR_DEVICE_FEATURE_NOT_SUPPORTED",
  sDescription =    "The device does not support the command feature.");
fAddWindowsDefine("ERROR_MR_MID_NOT_FOUND",
  sDescription =    "The system cannot find message text for message number 0x%1 in the message file for %2.");
fAddWindowsDefine("ERROR_SCOPE_NOT_FOUND",
  sDescription =    "The scope specified was not found.");
fAddWindowsDefine("ERROR_UNDEFINED_SCOPE",
  sDescription =    "The Central Access Policy specified is not defined on the target machine.");
fAddWindowsDefine("ERROR_INVALID_CAP",
  sDescription =    "The Central Access Policy obtained from Active Directory is invalid.");
fAddWindowsDefine("ERROR_DEVICE_UNREACHABLE",
  sDescription =    "The device is unreachable.");
fAddWindowsDefine("ERROR_DEVICE_NO_RESOURCES",
  sDescription =    "The target device has insufficient resources to complete the operation.");
fAddWindowsDefine("ERROR_DATA_CHECKSUM_ERROR",
  sDescription =    "A data integrity checksum error occurred. Data in the file stream is corrupt.");
fAddWindowsDefine("ERROR_INTERMIXED_KERNEL_EA_OPERATION",
  sDescription =    "An attempt was made to modify both a KERNEL and normal Extended Attribute (EA) in the same operation.");
fAddWindowsDefine("ERROR_FILE_LEVEL_TRIM_NOT_SUPPORTED",
  sDescription =    "Device does not support file-level TRIM.");
fAddWindowsDefine("ERROR_OFFSET_ALIGNMENT_VIOLATION",
  sDescription =    "The command specified a data offset that does not align to the device's granularity/alignment.");
fAddWindowsDefine("ERROR_INVALID_FIELD_IN_PARAMETER_LIST",
  sDescription =    "The command specified an invalid field in its parameter list.");
fAddWindowsDefine("ERROR_OPERATION_IN_PROGRESS",
  sDescription =    "An operation is currently in progress with the device.");
fAddWindowsDefine("ERROR_BAD_DEVICE_PATH",
  sDescription =    "An attempt was made to send down the command via an invalid path to the target device.");
fAddWindowsDefine("ERROR_TOO_MANY_DESCRIPTORS",
  sDescription =    "The command specified a number of descriptors that exceeded the maximum supported by the device.");
fAddWindowsDefine("ERROR_SCRUB_DATA_DISABLED",
  sDescription =    "Scrub is disabled on the specified file.");
fAddWindowsDefine("ERROR_NOT_REDUNDANT_STORAGE",
  sDescription =    "The storage device does not provide redundancy.");
fAddWindowsDefine("ERROR_RESIDENT_FILE_NOT_SUPPORTED",
  sDescription =    "An operation is not supported on a resident file.");
fAddWindowsDefine("ERROR_COMPRESSED_FILE_NOT_SUPPORTED",
  sDescription =    "An operation is not supported on a compressed file.");
fAddWindowsDefine("ERROR_DIRECTORY_NOT_SUPPORTED",
  sDescription =    "An operation is not supported on a directory.");
fAddWindowsDefine("ERROR_NOT_READ_FROM_COPY",
  sDescription =    "The specified copy of the requested data could not be read.");
fAddWindowsDefine("ERROR_FT_WRITE_FAILURE",
  sDescription =    "The specified data could not be written to any of the copies.");
fAddWindowsDefine("ERROR_FT_DI_SCAN_REQUIRED",
  sDescription =    "One or more copies of data on this device may be out of sync. No writes may be performed until a data integrity scan is completed.");
fAddWindowsDefine("ERROR_INVALID_KERNEL_INFO_VERSION",
  sDescription =    "The supplied kernel information version is invalid.");
fAddWindowsDefine("ERROR_INVALID_PEP_INFO_VERSION",
  sDescription =    "The supplied PEP information version is invalid.");
fAddWindowsDefine("ERROR_OBJECT_NOT_EXTERNALLY_BACKED",
  sDescription =    "This object is not externally backed by any provider.");
fAddWindowsDefine("ERROR_EXTERNAL_BACKING_PROVIDER_UNKNOWN",
  sDescription =    "The external backing provider is not recognized.");
fAddWindowsDefine("ERROR_COMPRESSION_NOT_BENEFICIAL",
  sDescription =    "Compressing this object would not save space.");
fAddWindowsDefine("ERROR_STORAGE_TOPOLOGY_ID_MISMATCH",
  sDescription =    "The request failed due to a storage topology ID mismatch.");
fAddWindowsDefine("ERROR_BLOCKED_BY_PARENTAL_CONTROLS",
  sDescription =    "The operation was blocked by parental controls.");
fAddWindowsDefine("ERROR_FAIL_NOACTION_REBOOT",
  sDescription =    "No action was taken as a system reboot is required.");
fAddWindowsDefine("ERROR_FAIL_SHUTDOWN",
  sDescription =    "The shutdown operation failed.");
fAddWindowsDefine("ERROR_FAIL_RESTART",
  sDescription =    "The restart operation failed.");
fAddWindowsDefine("ERROR_MAX_SESSIONS_REACHED",
  sDescription =    "The maximum number of sessions has been reached.");
fAddWindowsDefine("ERROR_THREAD_MODE_ALREADY_BACKGROUND",
  sDescription =    "The thread is already in background processing mode.");
fAddWindowsDefine("ERROR_THREAD_MODE_NOT_BACKGROUND",
  sDescription =    "The thread is not in background processing mode.");
fAddWindowsDefine("ERROR_PROCESS_MODE_ALREADY_BACKGROUND",
  sDescription =    "The process is already in background processing mode.");
fAddWindowsDefine("ERROR_PROCESS_MODE_NOT_BACKGROUND",
  sDescription =    "The process is not in background processing mode.");
fAddWindowsDefine("ERROR_DEVICE_HARDWARE_ERROR",
  sDescription =    "The request failed due to a fatal device hardware error.");
fAddWindowsDefine("ERROR_INVALID_ADDRESS",
  sDescription =    "Attempt to access invalid address.");
fAddWindowsDefine("ERROR_USER_PROFILE_LOAD",
  sDescription =    "User profile cannot be loaded.");
fAddWindowsDefine("ERROR_ARITHMETIC_OVERFLOW",
  sDescription =    "Arithmetic result exceeded 32 bits.");
fAddWindowsDefine("ERROR_PIPE_CONNECTED",
  sDescription =    "There is a process on other end of the pipe.");
fAddWindowsDefine("ERROR_PIPE_LISTENING",
  sDescription =    "Waiting for a process to open the other end of the pipe.");
fAddWindowsDefine("ERROR_VERIFIER_STOP",
  sDescription =    "Application verifier has found an error in the current process.");
fAddWindowsDefine("ERROR_ABIOS_ERROR",
  sDescription =    "An error occurred in the ABIOS subsystem.");
fAddWindowsDefine("ERROR_WX86_WARNING",
  sDescription =    "A warning occurred in the WX86 subsystem.");
fAddWindowsDefine("ERROR_WX86_ERROR",
  sDescription =    "An error occurred in the WX86 subsystem.");
fAddWindowsDefine("ERROR_TIMER_NOT_CANCELED",
  sDescription =    "An attempt was made to cancel or set a timer that has an associated APC and the subject thread is not the thread that originally set the timer with an associated APC routine.");
fAddWindowsDefine("ERROR_UNWIND",
  sDescription =    "Unwind exception code.");
fAddWindowsDefine("ERROR_BAD_STACK",
  sDescription =    "An invalid or unaligned stack was encountered during an unwind operation.");
fAddWindowsDefine("ERROR_INVALID_UNWIND_TARGET",
  sDescription =    "An invalid unwind target was encountered during an unwind operation.");
fAddWindowsDefine("ERROR_INVALID_PORT_ATTRIBUTES",
  sDescription =    "Invalid Object Attributes specified to NtCreatePort or invalid Port Attributes specified to NtConnectPort");
fAddWindowsDefine("ERROR_PORT_MESSAGE_TOO_LONG",
  sDescription =    "Length of message passed to NtRequestPort or NtRequestWaitReplyPort was longer than the maximum message allowed by the port.");
fAddWindowsDefine("ERROR_INVALID_QUOTA_LOWER",
  sDescription =    "An attempt was made to lower a quota limit below the current usage.");
fAddWindowsDefine("ERROR_DEVICE_ALREADY_ATTACHED",
  sDescription =    "An attempt was made to attach to a device that was already attached to another device.");
fAddWindowsDefine("ERROR_INSTRUCTION_MISALIGNMENT",
  sDescription =    "An attempt was made to execute an instruction at an unaligned address and the host system does not support unaligned instruction references.");
fAddWindowsDefine("ERROR_PROFILING_NOT_STARTED",
  sDescription =    "Profiling not started.");
fAddWindowsDefine("ERROR_PROFILING_NOT_STOPPED",
  sDescription =    "Profiling not stopped.");
fAddWindowsDefine("ERROR_COULD_NOT_INTERPRET",
  sDescription =    "The passed ACL did not contain the minimum required information.");
fAddWindowsDefine("ERROR_PROFILING_AT_LIMIT",
  sDescription =    "The number of active profiling objects is at the maximum and no more may be started.");
fAddWindowsDefine("ERROR_CANT_WAIT",
  sDescription =    "Used to indicate that an operation cannot continue without blocking for I/O.");
fAddWindowsDefine("ERROR_CANT_TERMINATE_SELF",
  sDescription =    "Indicates that a thread attempted to terminate itself by default (called NtTerminateThread with NULL) and it was the last thread in the current process.");
fAddWindowsDefine("ERROR_UNEXPECTED_MM_CREATE_ERR",
  sDescription =    "If an MM error is returned which is not defined in the standard FsRtl filter, it is converted to one of the following errors which is guaranteed to be in the filter. In this case information is lost, however, the filter correctly handles the exception.");
fAddWindowsDefine("ERROR_UNEXPECTED_MM_MAP_ERROR",
  sDescription =    "If an MM error is returned which is not defined in the standard FsRtl filter, it is converted to one of the following errors which is guaranteed to be in the filter. In this case information is lost, however, the filter correctly handles the exception.");
fAddWindowsDefine("ERROR_UNEXPECTED_MM_EXTEND_ERR",
  sDescription =    "If an MM error is returned which is not defined in the standard FsRtl filter, it is converted to one of the following errors which is guaranteed to be in the filter. In this case information is lost, however, the filter correctly handles the exception.");
fAddWindowsDefine("ERROR_BAD_FUNCTION_TABLE",
  sDescription =    "A malformed function table was encountered during an unwind operation.");
fAddWindowsDefine("ERROR_NO_GUID_TRANSLATION",
  sDescription =    "Indicates that an attempt was made to assign protection to a file system file or directory and one of the SIDs in the security descriptor could not be translated into a GUID that could be stored by the file system. This causes the protection attempt to fail, which may cause a file creation attempt to fail.");
fAddWindowsDefine("ERROR_INVALID_LDT_SIZE",
  sDescription =    "Indicates that an attempt was made to grow an LDT by setting its size, or that the size was not an even number of selectors.");
fAddWindowsDefine("ERROR_INVALID_LDT_OFFSET",
  sDescription =    "Indicates that the starting value for the LDT information was not an integral multiple of the selector size.");
fAddWindowsDefine("ERROR_INVALID_LDT_DESCRIPTOR",
  sDescription =    "Indicates that the user supplied an invalid descriptor when trying to set up Ldt descriptors.");
fAddWindowsDefine("ERROR_TOO_MANY_THREADS",
  sDescription =    "Indicates a process has too many threads to perform the requested action. For example, assignment of a primary token may only be performed when a process has zero or one threads.");
fAddWindowsDefine("ERROR_THREAD_NOT_IN_PROCESS",
  sDescription =    "An attempt was made to operate on a thread within a specific process, but the thread specified is not in the process specified.");
fAddWindowsDefine("ERROR_PAGEFILE_QUOTA_EXCEEDED",
  sDescription =    "Page file quota was exceeded.");
fAddWindowsDefine("ERROR_LOGON_SERVER_CONFLICT",
  sDescription =    "The Netlogon service cannot start because another Netlogon service running in the domain conflicts with the specified role.");
fAddWindowsDefine("ERROR_SYNCHRONIZATION_REQUIRED",
  sDescription =    "The SAM database on a Windows Server is significantly out of synchronization with the copy on the Domain Controller. A complete synchronization is required.");
fAddWindowsDefine("ERROR_NET_OPEN_FAILED",
  sDescription =    "The NtCreateFile API failed. This error should never be returned to an application, it is a place holder for the Windows Lan Manager Redirector to use in its internal error mapping routines.");
fAddWindowsDefine("ERROR_IO_PRIVILEGE_FAILED",
  sDescription =    "The I/O permissions for the process could not be changed.");
fAddWindowsDefine("ERROR_CONTROL_C_EXIT",
  sDescription =    "The application terminated as a result of a CTRL+C.");
fAddWindowsDefine("ERROR_MISSING_SYSTEMFILE",
  sDescription =    "The required system file %hs is bad or missing.");
fAddWindowsDefine("ERROR_UNHANDLED_EXCEPTION",
  sDescription =    "The exception %s (0x%08lx) occurred in the application at location 0x%08lx.");
fAddWindowsDefine("ERROR_APP_INIT_FAILURE",
  sDescription =    "The application was unable to start correctly (0x%lx). Click OK to close the application.");
fAddWindowsDefine("ERROR_PAGEFILE_CREATE_FAILED",
  sDescription =    "The creation of the paging file %hs failed (%lx). The requested size was %ld.");
fAddWindowsDefine("ERROR_INVALID_IMAGE_HASH",
  sDescription =    "Windows cannot verify the digital signature for this file. A recent hardware or software change might have installed a file that is signed incorrectly or damaged, or that might be malicious software from an unknown source.");
fAddWindowsDefine("ERROR_NO_PAGEFILE",
  sDescription =    "No paging file was specified in the system configuration.");
fAddWindowsDefine("ERROR_ILLEGAL_FLOAT_CONTEXT",
  sDescription =    "A real-mode application issued a floating-point instruction and floating-point hardware is not present.");
fAddWindowsDefine("ERROR_NO_EVENT_PAIR",
  sDescription =    "An event pair synchronization operation was performed using the thread specific client/server event pair object, but no event pair object was associated with the thread.");
fAddWindowsDefine("ERROR_DOMAIN_CTRLR_CONFIG_ERROR",
  sDescription =    "A Windows Server has an incorrect configuration.");
fAddWindowsDefine("ERROR_ILLEGAL_CHARACTER",
  sDescription =    "An illegal character was encountered. For a multi-byte character set this includes a lead byte without a succeeding trail byte. For the Unicode character set this includes the characters 0xFFFF and 0xFFFE.");
fAddWindowsDefine("ERROR_UNDEFINED_CHARACTER",
  sDescription =    "The Unicode character is not defined in the Unicode character set installed on the system.");
fAddWindowsDefine("ERROR_FLOPPY_VOLUME",
  sDescription =    "The paging file cannot be created on a floppy diskette.");
fAddWindowsDefine("ERROR_BIOS_FAILED_TO_CONNECT_INTERRUPT",
  sDescription =    "The system BIOS failed to connect a system interrupt to the device or bus for which the device is connected.");
fAddWindowsDefine("ERROR_BACKUP_CONTROLLER",
  sDescription =    "This operation is only allowed for the Primary Domain Controller of the domain.");
fAddWindowsDefine("ERROR_MUTANT_LIMIT_EXCEEDED",
  sDescription =    "An attempt was made to acquire a mutant such that its maximum count would have been exceeded.");
fAddWindowsDefine("ERROR_FS_DRIVER_REQUIRED",
  sDescription =    "A volume has been accessed for which a file system driver is required that has not yet been loaded.");
fAddWindowsDefine("ERROR_CANNOT_LOAD_REGISTRY_FILE",
  sDescription =    "The registry cannot load the hive (file): %hs or its log or alternate. It is corrupt, absent, or not writable.");
fAddWindowsDefine("ERROR_DEBUG_ATTACH_FAILED",
  sDescription =    "An unexpected failure occurred while processing a DebugActiveProcess API request. You may choose OK to terminate the process, or Cancel to ignore the error.");
fAddWindowsDefine("ERROR_SYSTEM_PROCESS_TERMINATED",
  sDescription =    "The %hs system process terminated unexpectedly with a status of 0x%08x (0x%08x 0x%08x). The system has been shut down.");
fAddWindowsDefine("ERROR_DATA_NOT_ACCEPTED",
  sDescription =    "The TDI client could not handle the data received during an indication.");
fAddWindowsDefine("ERROR_VDM_HARD_ERROR",
  sDescription =    "NTVDM encountered a hard error.");
fAddWindowsDefine("ERROR_DRIVER_CANCEL_TIMEOUT",
  sDescription =    "The driver %hs failed to complete a cancelled I/O request in the allotted time.");
fAddWindowsDefine("ERROR_REPLY_MESSAGE_MISMATCH",
  sDescription =    "An attempt was made to reply to an LPC message, but the thread specified by the client ID in the message was not waiting on that message.");
fAddWindowsDefine("ERROR_LOST_WRITEBEHIND_DATA",
  sDescription =    "Windows was unable to save all the data for the file %hs. The data has been lost. This error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.");
fAddWindowsDefine("ERROR_CLIENT_SERVER_PARAMETERS_INVALID",
  sDescription =    "The parameter(s) passed to the server in the client/server shared memory window were invalid. Too much data may have been put in the shared memory window.");
fAddWindowsDefine("ERROR_NOT_TINY_STREAM",
  sDescription =    "The stream is not a tiny stream.");
fAddWindowsDefine("ERROR_STACK_OVERFLOW_READ",
  sDescription =    "The request must be handled by the stack overflow code.");
fAddWindowsDefine("ERROR_CONVERT_TO_LARGE",
  sDescription =    "Internal OFS status codes indicating how an allocation operation is handled. Either it is retried after the containing onode is moved or the extent stream is converted to a large stream.");
fAddWindowsDefine("ERROR_FOUND_OUT_OF_SCOPE",
  sDescription =    "The attempt to find the object found an object matching by ID on the volume but it is out of the scope of the handle used for the operation.");
fAddWindowsDefine("ERROR_ALLOCATE_BUCKET",
  sDescription =    "The bucket array must be grown. Retry transaction after doing so.");
fAddWindowsDefine("ERROR_MARSHALL_OVERFLOW",
  sDescription =    "The user/kernel marshalling buffer has overflowed.");
fAddWindowsDefine("ERROR_INVALID_VARIANT",
  sDescription =    "The supplied variant structure contains invalid data.");
fAddWindowsDefine("ERROR_BAD_COMPRESSION_BUFFER",
  sDescription =    "The specified buffer contains ill-formed data.");
fAddWindowsDefine("ERROR_AUDIT_FAILED",
  sDescription =    "An attempt to generate a security audit failed.");
fAddWindowsDefine("ERROR_TIMER_RESOLUTION_NOT_SET",
  sDescription =    "The timer resolution was not previously set by the current process.");
fAddWindowsDefine("ERROR_INSUFFICIENT_LOGON_INFO",
  sDescription =    "There is insufficient account information to log you on.");
fAddWindowsDefine("ERROR_BAD_DLL_ENTRYPOINT",
  sDescription =    "The dynamic link library %hs is not written correctly. The stack pointer has been left in an inconsistent state. The entrypoint should be declared as WINAPI or STDCALL. Select YES to fail the DLL load. Select NO to continue execution. Selecting NO may cause the application to operate incorrectly.");
fAddWindowsDefine("ERROR_BAD_SERVICE_ENTRYPOINT",
  sDescription =    "The %hs service is not written correctly. The stack pointer has been left in an inconsistent state. The callback entrypoint should be declared as WINAPI or STDCALL. Selecting OK will cause the service to continue operation. However, the service process may operate incorrectly.");
fAddWindowsDefine("ERROR_IP_ADDRESS_CONFLICT1",
  sDescription =    "There is an IP address conflict with another system on the network");
fAddWindowsDefine("ERROR_IP_ADDRESS_CONFLICT2",
  sDescription =    "There is an IP address conflict with another system on the network");
fAddWindowsDefine("ERROR_REGISTRY_QUOTA_LIMIT",
  sDescription =    "The system has reached the maximum size allowed for the system part of the registry. Additional storage requests will be ignored.");
fAddWindowsDefine("ERROR_NO_CALLBACK_ACTIVE",
  sDescription =    "A callback return system service cannot be executed when no callback is active.");
fAddWindowsDefine("ERROR_PWD_TOO_SHORT",
  sDescription =    "The password provided is too short to meet the policy of your user account. Please choose a longer password.");
fAddWindowsDefine("ERROR_PWD_TOO_RECENT",
  sDescription =    "The policy of your user account does not allow you to change passwords too frequently. This is done to prevent users from changing back to a familiar, but potentially discovered, password. If you feel your password has been compromised then please contact your administrator immediately to have a new one assigned.");
fAddWindowsDefine("ERROR_PWD_HISTORY_CONFLICT",
  sDescription =    "You have attempted to change your password to one that you have used in the past. The policy of your user account does not allow this. Please select a password that you have not previously used.");
fAddWindowsDefine("ERROR_UNSUPPORTED_COMPRESSION",
  sDescription =    "The specified compression format is unsupported.");
fAddWindowsDefine("ERROR_INVALID_HW_PROFILE",
  sDescription =    "The specified hardware profile configuration is invalid.");
fAddWindowsDefine("ERROR_INVALID_PLUGPLAY_DEVICE_PATH",
  sDescription =    "The specified Plug and Play registry device path is invalid.");
fAddWindowsDefine("ERROR_QUOTA_LIST_INCONSISTENT",
  sDescription =    "The specified quota list is internally inconsistent with its descriptor.");
fAddWindowsDefine("ERROR_EVALUATION_EXPIRATION",
  sDescription =    "The evaluation period for this installation of Windows has expired. This system will shutdown in 1 hour. To restore access to this installation of Windows, please upgrade this installation using a licensed distribution of this product.");
fAddWindowsDefine("ERROR_ILLEGAL_DLL_RELOCATION",
  sDescription =    "The system DLL %hs was relocated in memory. The application will not run properly. The relocation occurred because the DLL %hs occupied an address range reserved for Windows system DLLs. The vendor supplying the DLL should be contacted for a new DLL.");
fAddWindowsDefine("ERROR_DLL_INIT_FAILED_LOGOFF",
  sDescription =    "The application failed to initialize because the window station is shutting down.");
fAddWindowsDefine("ERROR_VALIDATE_CONTINUE",
  sDescription =    "The validation process needs to continue on to the next step.");
fAddWindowsDefine("ERROR_NO_MORE_MATCHES",
  sDescription =    "There are no more matches for the current index enumeration.");
fAddWindowsDefine("ERROR_RANGE_LIST_CONFLICT",
  sDescription =    "The range could not be added to the range list because of a conflict.");
fAddWindowsDefine("ERROR_SERVER_SID_MISMATCH",
  sDescription =    "The server process is running under a SID different than that required by client.");
fAddWindowsDefine("ERROR_CANT_ENABLE_DENY_ONLY",
  sDescription =    "A group marked use for deny only cannot be enabled.");
fAddWindowsDefine("ERROR_FLOAT_MULTIPLE_FAULTS",
  sDescription =    "Multiple floating point faults.");
fAddWindowsDefine("ERROR_FLOAT_MULTIPLE_TRAPS",
  sDescription =    "Multiple floating point traps.");
fAddWindowsDefine("ERROR_NOINTERFACE",
  sDescription =    "The requested interface is not supported.");
fAddWindowsDefine("ERROR_DRIVER_FAILED_SLEEP",
  sDescription =    "The driver %hs does not support standby mode. Updating this driver may allow the system to go to standby mode.");
fAddWindowsDefine("ERROR_CORRUPT_SYSTEM_FILE",
  sDescription =    "The system file %1 has become corrupt and has been replaced.");
fAddWindowsDefine("ERROR_COMMITMENT_MINIMUM",
  sDescription =    "Your system is low on virtual memory. Windows is increasing the size of your virtual memory paging file. During this process, memory requests for some applications may be denied. For more information, see Help.");
fAddWindowsDefine("ERROR_PNP_RESTART_ENUMERATION",
  sDescription =    "A device was removed so enumeration must be restarted.");
fAddWindowsDefine("ERROR_SYSTEM_IMAGE_BAD_SIGNATURE",
  sDescription =    "The system image %s is not properly signed. The file has been replaced with the signed file. The system has been shut down.");
fAddWindowsDefine("ERROR_PNP_REBOOT_REQUIRED",
  sDescription =    "Device will not start without a reboot.");
fAddWindowsDefine("ERROR_INSUFFICIENT_POWER",
  sDescription =    "There is not enough power to complete the requested operation.");
fAddWindowsDefine("ERROR_MULTIPLE_FAULT_VIOLATION",
  sDescription =    "ERROR_MULTIPLE_FAULT_VIOLATION");
fAddWindowsDefine("ERROR_SYSTEM_SHUTDOWN",
  sDescription =    "The system is in the process of shutting down.");
fAddWindowsDefine("ERROR_PORT_NOT_SET",
  sDescription =    "An attempt to remove a processes DebugPort was made, but a port was not already associated with the process.");
fAddWindowsDefine("ERROR_DS_VERSION_CHECK_FAILURE",
  sDescription =    "This version of Windows is not compatible with the behavior version of directory forest, domain or domain controller.");
fAddWindowsDefine("ERROR_RANGE_NOT_FOUND",
  sDescription =    "The specified range could not be found in the range list.");
fAddWindowsDefine("ERROR_NOT_SAFE_MODE_DRIVER",
  sDescription =    "The driver was not loaded because the system is booting into safe mode.");
fAddWindowsDefine("ERROR_FAILED_DRIVER_ENTRY",
  sDescription =    "The driver was not loaded because it failed it's initialization call.");
fAddWindowsDefine("ERROR_DEVICE_ENUMERATION_ERROR",
  sDescription =    "The \"%hs\" encountered an error while applying power or reading the device configuration. This may be caused by a failure of your hardware or by a poor connection.");
fAddWindowsDefine("ERROR_MOUNT_POINT_NOT_RESOLVED",
  sDescription =    "The create operation failed because the name contained at least one mount point which resolves to a volume to which the specified device object is not attached.");
fAddWindowsDefine("ERROR_INVALID_DEVICE_OBJECT_PARAMETER",
  sDescription =    "The device object parameter is either not a valid device object or is not attached to the volume specified by the file name.");
fAddWindowsDefine("ERROR_MCA_OCCURED",
  sDescription =    "A Machine Check Error has occurred. Please check the system eventlog for additional information.");
fAddWindowsDefine("ERROR_DRIVER_DATABASE_ERROR",
  sDescription =    "There was error [%2] processing the driver database.");
fAddWindowsDefine("ERROR_SYSTEM_HIVE_TOO_LARGE",
  sDescription =    "System hive size has exceeded its limit.");
fAddWindowsDefine("ERROR_DRIVER_FAILED_PRIOR_UNLOAD",
  sDescription =    "The driver could not be loaded because a previous version of the driver is still in memory.");
fAddWindowsDefine("ERROR_VOLSNAP_PREPARE_HIBERNATE",
  sDescription =    "Please wait while the Volume Shadow Copy Service prepares volume %hs for hibernation.");
fAddWindowsDefine("ERROR_HIBERNATION_FAILURE",
  sDescription =    "The system has failed to hibernate (The error code is %hs). Hibernation will be disabled until the system is restarted.");
fAddWindowsDefine("ERROR_PWD_TOO_LONG",
  sDescription =    "The password provided is too long to meet the policy of your user account. Please choose a shorter password.");
fAddWindowsDefine("ERROR_FILE_SYSTEM_LIMITATION",
  sDescription =    "The requested operation could not be completed due to a file system limitation");
fAddWindowsDefine("ERROR_ASSERTION_FAILURE",
  sDescription =    "An assertion failure has occurred.");
fAddWindowsDefine("ERROR_ACPI_ERROR",
  sDescription =    "An error occurred in the ACPI subsystem.");
fAddWindowsDefine("ERROR_WOW_ASSERTION",
  sDescription =    "WOW Assertion Error.");
fAddWindowsDefine("ERROR_PNP_BAD_MPS_TABLE",
  sDescription =    "A device is missing in the system BIOS MPS table. This device will not be used. Please contact your system vendor for system BIOS update.");
fAddWindowsDefine("ERROR_PNP_TRANSLATION_FAILED",
  sDescription =    "A translator failed to translate resources.");
fAddWindowsDefine("ERROR_PNP_IRQ_TRANSLATION_FAILED",
  sDescription =    "A IRQ translator failed to translate resources.");
fAddWindowsDefine("ERROR_PNP_INVALID_ID",
  sDescription =    "Driver %2 returned invalid ID for a child device (%3).");
fAddWindowsDefine("ERROR_WAKE_SYSTEM_DEBUGGER",
  sDescription =    "the system debugger was awakened by an interrupt.");
fAddWindowsDefine("ERROR_HANDLES_CLOSED",
  sDescription =    "Handles to objects have been automatically closed as a result of the requested operation.");
fAddWindowsDefine("ERROR_EXTRANEOUS_INFORMATION",
  sDescription =    "The specified access control list (ACL) contained more information than was expected.");
fAddWindowsDefine("ERROR_RXACT_COMMIT_NECESSARY",
  sDescription =    "This warning level status indicates that the transaction state already exists for the registry sub-tree, but that a transaction commit was previously aborted. The commit has NOT been completed, but has not been rolled back either (so it may still be committed if desired).");
fAddWindowsDefine("ERROR_MEDIA_CHECK",
  sDescription =    "The media may have changed.");
fAddWindowsDefine("ERROR_GUID_SUBSTITUTION_MADE",
  sDescription =    "During the translation of a global identifier (GUID) to a Windows security ID (SID), no administratively-defined GUID prefix was found. A substitute prefix was used, which will not compromise system security. However, this may provide a more restrictive access than intended.");
fAddWindowsDefine("ERROR_STOPPED_ON_SYMLINK",
  sDescription =    "The create operation stopped after reaching a symbolic link");
fAddWindowsDefine("ERROR_LONGJUMP",
  sDescription =    "A long jump has been executed.");
fAddWindowsDefine("ERROR_PLUGPLAY_QUERY_VETOED",
  sDescription =    "The Plug and Play query operation was not successful.");
fAddWindowsDefine("ERROR_UNWIND_CONSOLIDATE",
  sDescription =    "A frame consolidation has been executed.");
fAddWindowsDefine("ERROR_REGISTRY_HIVE_RECOVERED",
  sDescription =    "Registry hive (file): %hs was corrupted and it has been recovered. Some data might have been lost.");
fAddWindowsDefine("ERROR_DLL_MIGHT_BE_INSECURE",
  sDescription =    "The application is attempting to run executable code from the module %hs. This may be insecure. An alternative, %hs, is available. Should the application use the secure module %hs?");
fAddWindowsDefine("ERROR_DLL_MIGHT_BE_INCOMPATIBLE",
  sDescription =    "The application is loading executable code from the module %hs. This is secure, but may be incompatible with previous releases of the operating system. An alternative, %hs, is available. Should the application use the secure module %hs?");
fAddWindowsDefine("ERROR_DBG_EXCEPTION_NOT_HANDLED",
  sDescription =    "Debugger did not handle the exception.");
fAddWindowsDefine("ERROR_DBG_REPLY_LATER",
  sDescription =    "Debugger will reply later.");
fAddWindowsDefine("ERROR_DBG_UNABLE_TO_PROVIDE_HANDLE",
  sDescription =    "Debugger cannot provide handle.");
fAddWindowsDefine("ERROR_DBG_TERMINATE_THREAD",
  sDescription =    "Debugger terminated thread.");
fAddWindowsDefine("ERROR_DBG_TERMINATE_PROCESS",
  sDescription =    "Debugger terminated process.");
fAddWindowsDefine("ERROR_DBG_CONTROL_C",
  sDescription =    "Debugger got control C.");
fAddWindowsDefine("ERROR_DBG_PRINTEXCEPTION_C",
  sDescription =    "Debugger printed exception on control C.");
fAddWindowsDefine("ERROR_DBG_RIPEXCEPTION",
  sDescription =    "Debugger received RIP exception.");
fAddWindowsDefine("ERROR_DBG_CONTROL_BREAK",
  sDescription =    "Debugger received control break.");
fAddWindowsDefine("ERROR_DBG_COMMAND_EXCEPTION",
  sDescription =    "Debugger command communication exception.");
fAddWindowsDefine("ERROR_OBJECT_NAME_EXISTS",
  sDescription =    "An attempt was made to create an object and the object name already existed.");
fAddWindowsDefine("ERROR_THREAD_WAS_SUSPENDED",
  sDescription =    "A thread termination occurred while the thread was suspended. The thread was resumed, and termination proceeded.");
fAddWindowsDefine("ERROR_IMAGE_NOT_AT_BASE",
  sDescription =    "An image file could not be mapped at the address specified in the image file. Local fixups must be performed on this image.");
fAddWindowsDefine("ERROR_RXACT_STATE_CREATED",
  sDescription =    "This informational level status indicates that a specified registry sub-tree transaction state did not yet exist and had to be created.");
fAddWindowsDefine("ERROR_SEGMENT_NOTIFICATION",
  sDescription =    "A virtual DOS machine (VDM) is loading, unloading, or moving an MS-DOS or Win16 program segment image. An exception is raised so a debugger can load, unload or track symbols and breakpoints within these 16-bit segments.");
fAddWindowsDefine("ERROR_BAD_CURRENT_DIRECTORY",
  sDescription =    "The process cannot switch to the startup current directory %hs. Select OK to set current directory to %hs, or select CANCEL to exit.");
fAddWindowsDefine("ERROR_FT_READ_RECOVERY_FROM_BACKUP",
  sDescription =    "To satisfy a read request, the NT fault-tolerant file system successfully read the requested data from a redundant copy. This was done because the file system encountered a failure on a member of the fault-tolerant volume, but was unable to reassign the failing area of the device.");
fAddWindowsDefine("ERROR_FT_WRITE_RECOVERY",
  sDescription =    "To satisfy a write request, the NT fault-tolerant file system successfully wrote a redundant copy of the information. This was done because the file system encountered a failure on a member of the fault-tolerant volume, but was not able to reassign the failing area of the device.");
fAddWindowsDefine("ERROR_IMAGE_MACHINE_TYPE_MISMATCH",
  sDescription =    "The image file %hs is valid, but is for a machine type other than the current machine. Select OK to continue, or CANCEL to fail the DLL load.");
fAddWindowsDefine("ERROR_RECEIVE_PARTIAL",
  sDescription =    "The network transport returned partial data to its client. The remaining data will be sent later.");
fAddWindowsDefine("ERROR_RECEIVE_EXPEDITED",
  sDescription =    "The network transport returned data to its client that was marked as expedited by the remote system.");
fAddWindowsDefine("ERROR_RECEIVE_PARTIAL_EXPEDITED",
  sDescription =    "The network transport returned partial data to its client and this data was marked as expedited by the remote system. The remaining data will be sent later.");
fAddWindowsDefine("ERROR_EVENT_DONE",
  sDescription =    "The TDI indication has completed successfully.");
fAddWindowsDefine("ERROR_EVENT_PENDING",
  sDescription =    "The TDI indication has entered the pending state.");
fAddWindowsDefine("ERROR_CHECKING_FILE_SYSTEM",
  sDescription =    "Checking file system on %wZ");
fAddWindowsDefine("ERROR_FATAL_APP_EXIT",
  sDescription =    "%hs");
fAddWindowsDefine("ERROR_PREDEFINED_HANDLE",
  sDescription =    "The specified registry key is referenced by a predefined handle.");
fAddWindowsDefine("ERROR_WAS_UNLOCKED",
  sDescription =    "The page protection of a locked page was changed to 'No Access' and the page was unlocked from memory and from the process.");
fAddWindowsDefine("ERROR_SERVICE_NOTIFICATION",
  sDescription =    "%hs");
fAddWindowsDefine("ERROR_WAS_LOCKED",
  sDescription =    "One of the pages to lock was already locked.");
fAddWindowsDefine("ERROR_LOG_HARD_ERROR",
  sDescription =    "Application popup: %1 : %2");
fAddWindowsDefine("ERROR_ALREADY_WIN32",
  sDescription =    "ERROR_ALREADY_WIN32");
fAddWindowsDefine("ERROR_IMAGE_MACHINE_TYPE_MISMATCH_EXE",
  sDescription =    "The image file %hs is valid, but is for a machine type other than the current machine.");
fAddWindowsDefine("ERROR_NO_YIELD_PERFORMED",
  sDescription =    "A yield execution was performed and no thread was available to run.");
fAddWindowsDefine("ERROR_TIMER_RESUME_IGNORED",
  sDescription =    "The resumable flag to a timer API was ignored.");
fAddWindowsDefine("ERROR_ARBITRATION_UNHANDLED",
  sDescription =    "The arbiter has deferred arbitration of these resources to its parent");
fAddWindowsDefine("ERROR_CARDBUS_NOT_SUPPORTED",
  sDescription =    "The inserted CardBus device cannot be started because of a configuration error on \"%hs\".");
fAddWindowsDefine("ERROR_MP_PROCESSOR_MISMATCH",
  sDescription =    "The CPUs in this multiprocessor system are not all the same revision level. To use all processors the operating system restricts itself to the features of the least capable processor in the system. Should problems occur with this system, contact the CPU manufacturer to see if this mix of processors is supported.");
fAddWindowsDefine("ERROR_HIBERNATED",
  sDescription =    "The system was put into hibernation.");
fAddWindowsDefine("ERROR_RESUME_HIBERNATION",
  sDescription =    "The system was resumed from hibernation.");
fAddWindowsDefine("ERROR_FIRMWARE_UPDATED",
  sDescription =    "Windows has detected that the system firmware (BIOS) was updated [previous firmware date = %2, current firmware date %3].");
fAddWindowsDefine("ERROR_DRIVERS_LEAKING_LOCKED_PAGES",
  sDescription =    "A device driver is leaking locked I/O pages causing system degradation. The system has automatically enabled tracking code in order to try and catch the culprit.");
fAddWindowsDefine("ERROR_WAKE_SYSTEM",
  sDescription =    "The system has awoken");
fAddWindowsDefine("ERROR_WAIT_1",
  sDescription =    "ERROR_WAIT_1");
fAddWindowsDefine("ERROR_WAIT_2",
  sDescription =    "ERROR_WAIT_2");
fAddWindowsDefine("ERROR_WAIT_3",
  sDescription =    "ERROR_WAIT_3");
fAddWindowsDefine("ERROR_WAIT_63",
  sDescription =    "ERROR_WAIT_63");
fAddWindowsDefine("ERROR_ABANDONED_WAIT_0",
  sDescription =    "ERROR_ABANDONED_WAIT_0");
fAddWindowsDefine("ERROR_ABANDONED_WAIT_63",
  sDescription =    "ERROR_ABANDONED_WAIT_63");
fAddWindowsDefine("ERROR_USER_APC",
  sDescription =    "ERROR_USER_APC");
fAddWindowsDefine("ERROR_KERNEL_APC",
  sDescription =    "ERROR_KERNEL_APC");
fAddWindowsDefine("ERROR_ALERTED",
  sDescription =    "ERROR_ALERTED");
fAddWindowsDefine("ERROR_ELEVATION_REQUIRED",
  sDescription =    "The requested operation requires elevation.");
fAddWindowsDefine("ERROR_REPARSE",
  sDescription =    "A reparse should be performed by the Object Manager since the name of the file resulted in a symbolic link.");
fAddWindowsDefine("ERROR_OPLOCK_BREAK_IN_PROGRESS",
  sDescription =    "An open/create operation completed while an oplock break is underway.");
fAddWindowsDefine("ERROR_VOLUME_MOUNTED",
  sDescription =    "A new volume has been mounted by a file system.");
fAddWindowsDefine("ERROR_RXACT_COMMITTED",
  sDescription =    "This success level status indicates that the transaction state already exists for the registry sub-tree, but that a transaction commit was previously aborted. The commit has now been completed.");
fAddWindowsDefine("ERROR_NOTIFY_CLEANUP",
  sDescription =    "This indicates that a notify change request has been completed due to closing the handle which made the notify change request.");
fAddWindowsDefine("ERROR_PRIMARY_TRANSPORT_CONNECT_FAILED",
  sDescription =    "An attempt was made to connect to the remote server %hs on the primary transport, but the connection failed. The computer WAS able to connect on a secondary transport.");
fAddWindowsDefine("ERROR_PAGE_FAULT_TRANSITION",
  sDescription =    "Page fault was a transition fault.");
fAddWindowsDefine("ERROR_PAGE_FAULT_DEMAND_ZERO",
  sDescription =    "Page fault was a demand zero fault.");
fAddWindowsDefine("ERROR_PAGE_FAULT_COPY_ON_WRITE",
  sDescription =    "Page fault was a demand zero fault.");
fAddWindowsDefine("ERROR_PAGE_FAULT_GUARD_PAGE",
  sDescription =    "Page fault was a demand zero fault.");
fAddWindowsDefine("ERROR_PAGE_FAULT_PAGING_FILE",
  sDescription =    "Page fault was satisfied by reading from a secondary storage device.");
fAddWindowsDefine("ERROR_CACHE_PAGE_LOCKED",
  sDescription =    "Cached page was locked during operation.");
fAddWindowsDefine("ERROR_CRASH_DUMP",
  sDescription =    "Crash dump exists in paging file.");
fAddWindowsDefine("ERROR_BUFFER_ALL_ZEROS",
  sDescription =    "Specified buffer contains all zeros.");
fAddWindowsDefine("ERROR_REPARSE_OBJECT",
  sDescription =    "A reparse should be performed by the Object Manager since the name of the file resulted in a symbolic link.");
fAddWindowsDefine("ERROR_RESOURCE_REQUIREMENTS_CHANGED",
  sDescription =    "The device has succeeded a query-stop and its resource requirements have changed.");
fAddWindowsDefine("ERROR_TRANSLATION_COMPLETE",
  sDescription =    "The translator has translated these resources into the global space and no further translations should be performed.");
fAddWindowsDefine("ERROR_NOTHING_TO_TERMINATE",
  sDescription =    "A process being terminated has no threads to terminate.");
fAddWindowsDefine("ERROR_PROCESS_NOT_IN_JOB",
  sDescription =    "The specified process is not part of a job.");
fAddWindowsDefine("ERROR_PROCESS_IN_JOB",
  sDescription =    "The specified process is part of a job.");
fAddWindowsDefine("ERROR_VOLSNAP_HIBERNATE_READY",
  sDescription =    "The system is now ready for hibernation.");
fAddWindowsDefine("ERROR_FSFILTER_OP_COMPLETED_SUCCESSFULLY",
  sDescription =    "A file system or file system filter driver has successfully completed an FsFilter operation.");
fAddWindowsDefine("ERROR_INTERRUPT_VECTOR_ALREADY_CONNECTED",
  sDescription =    "The specified interrupt vector was already connected.");
fAddWindowsDefine("ERROR_INTERRUPT_STILL_CONNECTED",
  sDescription =    "The specified interrupt vector is still connected.");
fAddWindowsDefine("ERROR_WAIT_FOR_OPLOCK",
  sDescription =    "An operation is blocked waiting for an oplock.");
fAddWindowsDefine("ERROR_DBG_EXCEPTION_HANDLED",
  sDescription =    "Debugger handled exception");
fAddWindowsDefine("ERROR_DBG_CONTINUE",
  sDescription =    "Debugger continued");
fAddWindowsDefine("ERROR_CALLBACK_POP_STACK",
  sDescription =    "An exception occurred in a user mode callback and the kernel callback frame should be removed.");
fAddWindowsDefine("ERROR_COMPRESSION_DISABLED",
  sDescription =    "Compression is disabled for this volume.");
fAddWindowsDefine("ERROR_CANTFETCHBACKWARDS",
  sDescription =    "The data provider cannot fetch backwards through a result set.");
fAddWindowsDefine("ERROR_CANTSCROLLBACKWARDS",
  sDescription =    "The data provider cannot scroll backwards through a result set.");
fAddWindowsDefine("ERROR_ROWSNOTRELEASED",
  sDescription =    "The data provider requires that previously fetched data is released before asking for more data.");
fAddWindowsDefine("ERROR_BAD_ACCESSOR_FLAGS",
  sDescription =    "The data provider was not able to interpret the flags set for a column binding in an accessor.");
fAddWindowsDefine("ERROR_ERRORS_ENCOUNTERED",
  sDescription =    "One or more errors occurred while processing the request.");
fAddWindowsDefine("ERROR_NOT_CAPABLE",
  sDescription =    "The implementation is not capable of performing the request.");
fAddWindowsDefine("ERROR_REQUEST_OUT_OF_SEQUENCE",
  sDescription =    "The client of a component requested an operation which is not valid given the state of the component instance.");
fAddWindowsDefine("ERROR_VERSION_PARSE_ERROR",
  sDescription =    "A version number could not be parsed.");
fAddWindowsDefine("ERROR_BADSTARTPOSITION",
  sDescription =    "The iterator's start position is invalid.");
fAddWindowsDefine("ERROR_MEMORY_HARDWARE",
  sDescription =    "The hardware has reported an uncorrectable memory error.");
fAddWindowsDefine("ERROR_DISK_REPAIR_DISABLED",
  sDescription =    "The attempted operation required self healing to be enabled.");
fAddWindowsDefine("ERROR_INSUFFICIENT_RESOURCE_FOR_SPECIFIED_SHARED_SECTION_SIZE",
  sDescription =    "The Desktop heap encountered an error while allocating session memory. There is more information in the system event log.");
fAddWindowsDefine("ERROR_SYSTEM_POWERSTATE_TRANSITION",
  sDescription =    "The system power state is transitioning from %2 to %3.");
fAddWindowsDefine("ERROR_SYSTEM_POWERSTATE_COMPLEX_TRANSITION",
  sDescription =    "The system power state is transitioning from %2 to %3 but could enter %4.");
fAddWindowsDefine("ERROR_MCA_EXCEPTION",
  sDescription =    "A thread is getting dispatched with MCA EXCEPTION because of MCA.");
fAddWindowsDefine("ERROR_ACCESS_AUDIT_BY_POLICY",
  sDescription =    "Access to %1 is monitored by policy rule %2.");
fAddWindowsDefine("ERROR_ACCESS_DISABLED_NO_SAFER_UI_BY_POLICY",
  sDescription =    "Access to %1 has been restricted by your Administrator by policy rule %2.");
fAddWindowsDefine("ERROR_ABANDON_HIBERFILE",
  sDescription =    "A valid hibernation file has been invalidated and should be abandoned.");
fAddWindowsDefine("ERROR_LOST_WRITEBEHIND_DATA_NETWORK_DISCONNECTED",
  sDescription =    "Windows was unable to save all the data for the file %hs; the data has been lost. This error may be caused by network connectivity issues. Please try to save this file elsewhere.");
fAddWindowsDefine("ERROR_LOST_WRITEBEHIND_DATA_NETWORK_SERVER_ERROR",
  sDescription =    "Windows was unable to save all the data for the file %hs; the data has been lost. This error was returned by the server on which the file exists. Please try to save this file elsewhere.");
fAddWindowsDefine("ERROR_LOST_WRITEBEHIND_DATA_LOCAL_DISK_ERROR",
  sDescription =    "Windows was unable to save all the data for the file %hs; the data has been lost. This error may be caused if the device has been removed or the media is write-protected.");
fAddWindowsDefine("ERROR_BAD_MCFG_TABLE",
  sDescription =    "The resources required for this device conflict with the MCFG table.");
fAddWindowsDefine("ERROR_DISK_REPAIR_REDIRECTED",
  sDescription =    "The volume repair could not be performed while it is online. Please schedule to take the volume offline so that it can be repaired.");
fAddWindowsDefine("ERROR_DISK_REPAIR_UNSUCCESSFUL",
  sDescription =    "The volume repair was not successful.");
fAddWindowsDefine("ERROR_CORRUPT_LOG_OVERFULL",
  sDescription =    "One of the volume corruption logs is full. Further corruptions that may be detected won't be logged.");
fAddWindowsDefine("ERROR_CORRUPT_LOG_CORRUPTED",
  sDescription =    "One of the volume corruption logs is internally corrupted and needs to be recreated. The volume may contain undetected corruptions and must be scanned.");
fAddWindowsDefine("ERROR_CORRUPT_LOG_UNAVAILABLE",
  sDescription =    "One of the volume corruption logs is unavailable for being operated on.");
fAddWindowsDefine("ERROR_CORRUPT_LOG_DELETED_FULL",
  sDescription =    "One of the volume corruption logs was deleted while still having corruption records in them. The volume contains detected corruptions and must be scanned.");
fAddWindowsDefine("ERROR_CORRUPT_LOG_CLEARED",
  sDescription =    "One of the volume corruption logs was cleared by chkdsk and no longer contains real corruptions.");
fAddWindowsDefine("ERROR_ORPHAN_NAME_EXHAUSTED",
  sDescription =    "Orphaned files exist on the volume but could not be recovered because no more new names could be created in the recovery directory. Files must be moved from the recovery directory.");
fAddWindowsDefine("ERROR_OPLOCK_SWITCHED_TO_NEW_HANDLE",
  sDescription =    "The oplock that was associated with this handle is now associated with a different handle.");
fAddWindowsDefine("ERROR_CANNOT_GRANT_REQUESTED_OPLOCK",
  sDescription =    "An oplock of the requested level cannot be granted. An oplock of a lower level may be available.");
fAddWindowsDefine("ERROR_CANNOT_BREAK_OPLOCK",
  sDescription =    "The operation did not complete successfully because it would cause an oplock to be broken. The caller has requested that existing oplocks not be broken.");
fAddWindowsDefine("ERROR_OPLOCK_HANDLE_CLOSED",
  sDescription =    "The handle with which this oplock was associated has been closed. The oplock is now broken.");
fAddWindowsDefine("ERROR_NO_ACE_CONDITION",
  sDescription =    "The specified access control entry (ACE) does not contain a condition.");
fAddWindowsDefine("ERROR_INVALID_ACE_CONDITION",
  sDescription =    "The specified access control entry (ACE) contains an invalid condition.");
fAddWindowsDefine("ERROR_FILE_HANDLE_REVOKED",
  sDescription =    "Access to the specified file handle has been revoked.");
fAddWindowsDefine("ERROR_IMAGE_AT_DIFFERENT_BASE",
  sDescription =    "An image file was mapped at a different address from the one specified in the image file but fixups will still be automatically performed on the image.");
fAddWindowsDefine("ERROR_ENCRYPTED_IO_NOT_POSSIBLE",
  sDescription =    "The read or write operation to an encrypted file could not be completed because the file has not been opened for data access.");
fAddWindowsDefine("ERROR_FILE_METADATA_OPTIMIZATION_IN_PROGRESS",
  sDescription =    "File metadata optimization is already in progress.");
fAddWindowsDefine("ERROR_QUOTA_ACTIVITY",
  sDescription =    "The requested operation failed due to quota operation is still in progress.");
fAddWindowsDefine("ERROR_HANDLE_REVOKED",
  sDescription =    "Access to the specified handle has been revoked.");
fAddWindowsDefine("ERROR_EA_ACCESS_DENIED",
  sDescription =    "Access to the extended attribute was denied.");
fAddWindowsDefine("ERROR_OPERATION_ABORTED",
  sDescription =    "The I/O operation has been aborted because of either a thread exit or an application request.");
fAddWindowsDefine("ERROR_IO_INCOMPLETE",
  sDescription =    "Overlapped I/O event is not in a signaled state.");
fAddWindowsDefine("ERROR_IO_PENDING",
  sDescription =    "Overlapped I/O operation is in progress.");
fAddWindowsDefine("ERROR_NOACCESS",
  sDescription =    "Invalid access to memory location.");
fAddWindowsDefine("ERROR_SWAPERROR",
  sDescription =    "Error performing inpage operation.");
fAddWindowsDefine("ERROR_STACK_OVERFLOW",
  sDescription =    "Recursion too deep; the stack overflowed.");
fAddWindowsDefine("ERROR_INVALID_MESSAGE",
  sDescription =    "The window cannot act on the sent message.");
fAddWindowsDefine("ERROR_CAN_NOT_COMPLETE",
  sDescription =    "Cannot complete this function.");
fAddWindowsDefine("ERROR_INVALID_FLAGS",
  sDescription =    "Invalid flags.");
fAddWindowsDefine("ERROR_UNRECOGNIZED_VOLUME",
  sDescription =    "The volume does not contain a recognized file system. Please make sure that all required file system drivers are loaded and that the volume is not corrupted.");
fAddWindowsDefine("ERROR_FILE_INVALID",
  sDescription =    "The volume for a file has been externally altered so that the opened file is no longer valid.");
fAddWindowsDefine("ERROR_FULLSCREEN_MODE",
  sDescription =    "The requested operation cannot be performed in full-screen mode.");
fAddWindowsDefine("ERROR_NO_TOKEN",
  sDescription =    "An attempt was made to reference a token that does not exist.");
fAddWindowsDefine("ERROR_BADDB",
  sDescription =    "The configuration registry database is corrupt.");
fAddWindowsDefine("ERROR_BADKEY",
  sDescription =    "The configuration registry key is invalid.");
fAddWindowsDefine("ERROR_CANTOPEN",
  sDescription =    "The configuration registry key could not be opened.");
fAddWindowsDefine("ERROR_CANTREAD",
  sDescription =    "The configuration registry key could not be read.");
fAddWindowsDefine("ERROR_CANTWRITE",
  sDescription =    "The configuration registry key could not be written.");
fAddWindowsDefine("ERROR_REGISTRY_RECOVERED",
  sDescription =    "One of the files in the registry database had to be recovered by use of a log or alternate copy. The recovery was successful.");
fAddWindowsDefine("ERROR_REGISTRY_CORRUPT",
  sDescription =    "The registry is corrupted. The structure of one of the files containing registry data is corrupted, or the system's memory image of the file is corrupted, or the file could not be recovered because the alternate copy or log was absent or corrupted.");
fAddWindowsDefine("ERROR_REGISTRY_IO_FAILED",
  sDescription =    "An I/O operation initiated by the registry failed unrecoverably. The registry could not read in, or write out, or flush, one of the files that contain the system's image of the registry.");
fAddWindowsDefine("ERROR_NOT_REGISTRY_FILE",
  sDescription =    "The system has attempted to load or restore a file into the registry, but the specified file is not in a registry file format.");
fAddWindowsDefine("ERROR_KEY_DELETED",
  sDescription =    "Illegal operation attempted on a registry key that has been marked for deletion.");
fAddWindowsDefine("ERROR_NO_LOG_SPACE",
  sDescription =    "System could not allocate the required space in a registry log.");
fAddWindowsDefine("ERROR_KEY_HAS_CHILDREN",
  sDescription =    "Cannot create a symbolic link in a registry key that already has subkeys or values.");
fAddWindowsDefine("ERROR_CHILD_MUST_BE_VOLATILE",
  sDescription =    "Cannot create a stable subkey under a volatile parent key.");
fAddWindowsDefine("ERROR_NOTIFY_ENUM_DIR",
  sDescription =    "A notify change request is being completed and the information is not being returned in the caller's buffer. The caller now needs to enumerate the files to find the changes.");
fAddWindowsDefine("ERROR_DEPENDENT_SERVICES_RUNNING",
  sDescription =    "A stop control has been sent to a service that other running services are dependent on.");
fAddWindowsDefine("ERROR_INVALID_SERVICE_CONTROL",
  sDescription =    "The requested control is not valid for this service.");
fAddWindowsDefine("ERROR_SERVICE_REQUEST_TIMEOUT",
  sDescription =    "The service did not respond to the start or control request in a timely fashion.");
fAddWindowsDefine("ERROR_SERVICE_NO_THREAD",
  sDescription =    "A thread could not be created for the service.");
fAddWindowsDefine("ERROR_SERVICE_DATABASE_LOCKED",
  sDescription =    "The service database is locked.");
fAddWindowsDefine("ERROR_SERVICE_ALREADY_RUNNING",
  sDescription =    "An instance of the service is already running.");
fAddWindowsDefine("ERROR_INVALID_SERVICE_ACCOUNT",
  sDescription =    "The account name is invalid or does not exist, or the password is invalid for the account name specified.");
fAddWindowsDefine("ERROR_SERVICE_DISABLED",
  sDescription =    "The service cannot be started, either because it is disabled or because it has no enabled devices associated with it.");
fAddWindowsDefine("ERROR_CIRCULAR_DEPENDENCY",
  sDescription =    "Circular service dependency was specified.");
fAddWindowsDefine("ERROR_SERVICE_DOES_NOT_EXIST",
  sDescription =    "The specified service does not exist as an installed service.");
fAddWindowsDefine("ERROR_SERVICE_CANNOT_ACCEPT_CTRL",
  sDescription =    "The service cannot accept control messages at this time.");
fAddWindowsDefine("ERROR_SERVICE_NOT_ACTIVE",
  sDescription =    "The service has not been started.");
fAddWindowsDefine("ERROR_FAILED_SERVICE_CONTROLLER_CONNECT",
  sDescription =    "The service process could not connect to the service controller.");
fAddWindowsDefine("ERROR_EXCEPTION_IN_SERVICE",
  sDescription =    "An exception occurred in the service when handling the control request.");
fAddWindowsDefine("ERROR_DATABASE_DOES_NOT_EXIST",
  sDescription =    "The database specified does not exist.");
fAddWindowsDefine("ERROR_SERVICE_SPECIFIC_ERROR",
  sDescription =    "The service has returned a service-specific error code.");
fAddWindowsDefine("ERROR_PROCESS_ABORTED",
  sDescription =    "The process terminated unexpectedly.");
fAddWindowsDefine("ERROR_SERVICE_DEPENDENCY_FAIL",
  sDescription =    "The dependency service or group failed to start.");
fAddWindowsDefine("ERROR_SERVICE_LOGON_FAILED",
  sDescription =    "The service did not start due to a logon failure.");
fAddWindowsDefine("ERROR_SERVICE_START_HANG",
  sDescription =    "After starting, the service hung in a start-pending state.");
fAddWindowsDefine("ERROR_INVALID_SERVICE_LOCK",
  sDescription =    "The specified service database lock is invalid.");
fAddWindowsDefine("ERROR_SERVICE_MARKED_FOR_DELETE",
  sDescription =    "The specified service has been marked for deletion.");
fAddWindowsDefine("ERROR_SERVICE_EXISTS",
  sDescription =    "The specified service already exists.");
fAddWindowsDefine("ERROR_ALREADY_RUNNING_LKG",
  sDescription =    "The system is currently running with the last-known-good configuration.");
fAddWindowsDefine("ERROR_SERVICE_DEPENDENCY_DELETED",
  sDescription =    "The dependency service does not exist or has been marked for deletion.");
fAddWindowsDefine("ERROR_BOOT_ALREADY_ACCEPTED",
  sDescription =    "The current boot has already been accepted for use as the last-known-good control set.");
fAddWindowsDefine("ERROR_SERVICE_NEVER_STARTED",
  sDescription =    "No attempts to start the service have been made since the last boot.");
fAddWindowsDefine("ERROR_DUPLICATE_SERVICE_NAME",
  sDescription =    "The name is already in use as either a service name or a service display name.");
fAddWindowsDefine("ERROR_DIFFERENT_SERVICE_ACCOUNT",
  sDescription =    "The account specified for this service is different from the account specified for other services running in the same process.");
fAddWindowsDefine("ERROR_CANNOT_DETECT_DRIVER_FAILURE",
  sDescription =    "Failure actions can only be set for Win32 services, not for drivers.");
fAddWindowsDefine("ERROR_CANNOT_DETECT_PROCESS_ABORT",
  sDescription =    "This service runs in the same process as the service control manager. Therefore, the service control manager cannot take action if this service's process terminates unexpectedly.");
fAddWindowsDefine("ERROR_NO_RECOVERY_PROGRAM",
  sDescription =    "No recovery program has been configured for this service.");
fAddWindowsDefine("ERROR_SERVICE_NOT_IN_EXE",
  sDescription =    "The executable program that this service is configured to run in does not implement the service.");
fAddWindowsDefine("ERROR_NOT_SAFEBOOT_SERVICE",
  sDescription =    "This service cannot be started in Safe Mode");
fAddWindowsDefine("ERROR_END_OF_MEDIA",
  sDescription =    "The physical end of the tape has been reached.");
fAddWindowsDefine("ERROR_FILEMARK_DETECTED",
  sDescription =    "A tape access reached a filemark.");
fAddWindowsDefine("ERROR_BEGINNING_OF_MEDIA",
  sDescription =    "The beginning of the tape or a partition was encountered.");
fAddWindowsDefine("ERROR_SETMARK_DETECTED",
  sDescription =    "A tape access reached the end of a set of files.");
fAddWindowsDefine("ERROR_NO_DATA_DETECTED",
  sDescription =    "No more data is on the tape.");
fAddWindowsDefine("ERROR_PARTITION_FAILURE",
  sDescription =    "Tape could not be partitioned.");
fAddWindowsDefine("ERROR_INVALID_BLOCK_LENGTH",
  sDescription =    "When accessing a new tape of a multivolume partition, the current block size is incorrect.");
fAddWindowsDefine("ERROR_DEVICE_NOT_PARTITIONED",
  sDescription =    "Tape partition information could not be found when loading a tape.");
fAddWindowsDefine("ERROR_UNABLE_TO_LOCK_MEDIA",
  sDescription =    "Unable to lock the media eject mechanism.");
fAddWindowsDefine("ERROR_UNABLE_TO_UNLOAD_MEDIA",
  sDescription =    "Unable to unload the media.");
fAddWindowsDefine("ERROR_MEDIA_CHANGED",
  sDescription =    "The media in the drive may have changed.");
fAddWindowsDefine("ERROR_BUS_RESET",
  sDescription =    "The I/O bus was reset.");
fAddWindowsDefine("ERROR_NO_MEDIA_IN_DRIVE",
  sDescription =    "No media in drive.");
fAddWindowsDefine("ERROR_NO_UNICODE_TRANSLATION",
  sDescription =    "No mapping for the Unicode character exists in the target multi-byte code page.");
fAddWindowsDefine("ERROR_DLL_INIT_FAILED",
  sDescription =    "A dynamic link library (DLL) initialization routine failed.");
fAddWindowsDefine("ERROR_SHUTDOWN_IN_PROGRESS",
  sDescription =    "A system shutdown is in progress.");
fAddWindowsDefine("ERROR_NO_SHUTDOWN_IN_PROGRESS",
  sDescription =    "Unable to abort the system shutdown because no shutdown was in progress.");
fAddWindowsDefine("ERROR_IO_DEVICE",
  sDescription =    "The request could not be performed because of an I/O device error.");
fAddWindowsDefine("ERROR_SERIAL_NO_DEVICE",
  sDescription =    "No serial device was successfully initialized. The serial driver will unload.");
fAddWindowsDefine("ERROR_IRQ_BUSY",
  sDescription =    "Unable to open a device that was sharing an interrupt request (IRQ) with other devices. At least one other device that uses that IRQ was already opened.");
fAddWindowsDefine("ERROR_MORE_WRITES",
  sDescription =    "A serial I/O operation was completed by another write to the serial port. (The IOCTL_SERIAL_XOFF_COUNTER reached zero.)");
fAddWindowsDefine("ERROR_COUNTER_TIMEOUT",
  sDescription =    "A serial I/O operation completed because the timeout period expired. (The IOCTL_SERIAL_XOFF_COUNTER did not reach zero.)");
fAddWindowsDefine("ERROR_FLOPPY_ID_MARK_NOT_FOUND",
  sDescription =    "No ID address mark was found on the floppy disk.");
fAddWindowsDefine("ERROR_FLOPPY_WRONG_CYLINDER",
  sDescription =    "Mismatch between the floppy disk sector ID field and the floppy disk controller track address.");
fAddWindowsDefine("ERROR_FLOPPY_UNKNOWN_ERROR",
  sDescription =    "The floppy disk controller reported an error that is not recognized by the floppy disk driver.");
fAddWindowsDefine("ERROR_FLOPPY_BAD_REGISTERS",
  sDescription =    "The floppy disk controller returned inconsistent results in its registers.");
fAddWindowsDefine("ERROR_DISK_RECALIBRATE_FAILED",
  sDescription =    "While accessing the hard disk, a recalibrate operation failed, even after retries.");
fAddWindowsDefine("ERROR_DISK_OPERATION_FAILED",
  sDescription =    "While accessing the hard disk, a disk operation failed even after retries.");
fAddWindowsDefine("ERROR_DISK_RESET_FAILED",
  sDescription =    "While accessing the hard disk, a disk controller reset was needed, but even that failed.");
fAddWindowsDefine("ERROR_EOM_OVERFLOW",
  sDescription =    "Physical end of tape encountered.");
fAddWindowsDefine("ERROR_NOT_ENOUGH_SERVER_MEMORY",
  sDescription =    "Not enough server storage is available to process this command.");
fAddWindowsDefine("ERROR_POSSIBLE_DEADLOCK",
  sDescription =    "A potential deadlock condition has been detected.");
fAddWindowsDefine("ERROR_MAPPED_ALIGNMENT",
  sDescription =    "The base address or the file offset specified does not have the proper alignment.");
fAddWindowsDefine("ERROR_SET_POWER_STATE_VETOED",
  sDescription =    "An attempt to change the system power state was vetoed by another application or driver.");
fAddWindowsDefine("ERROR_SET_POWER_STATE_FAILED",
  sDescription =    "The system BIOS failed an attempt to change the system power state.");
fAddWindowsDefine("ERROR_TOO_MANY_LINKS",
  sDescription =    "An attempt was made to create more links on a file than the file system supports.");
fAddWindowsDefine("ERROR_OLD_WIN_VERSION",
  sDescription =    "The specified program requires a newer version of Windows.");
fAddWindowsDefine("ERROR_APP_WRONG_OS",
  sDescription =    "The specified program is not a Windows or MS-DOS program.");
fAddWindowsDefine("ERROR_SINGLE_INSTANCE_APP",
  sDescription =    "Cannot start more than one instance of the specified program.");
fAddWindowsDefine("ERROR_RMODE_APP",
  sDescription =    "The specified program was written for an earlier version of Windows.");
fAddWindowsDefine("ERROR_INVALID_DLL",
  sDescription =    "One of the library files needed to run this application is damaged.");
fAddWindowsDefine("ERROR_NO_ASSOCIATION",
  sDescription =    "No application is associated with the specified file for this operation.");
fAddWindowsDefine("ERROR_DDE_FAIL",
  sDescription =    "An error occurred in sending the command to the application.");
fAddWindowsDefine("ERROR_DLL_NOT_FOUND",
  sDescription =    "One of the library files needed to run this application cannot be found.");
fAddWindowsDefine("ERROR_NO_MORE_USER_HANDLES",
  sDescription =    "The current process has used all of its system allowance of handles for Window Manager objects.");
fAddWindowsDefine("ERROR_MESSAGE_SYNC_ONLY",
  sDescription =    "The message can be used only with synchronous operations.");
fAddWindowsDefine("ERROR_SOURCE_ELEMENT_EMPTY",
  sDescription =    "The indicated source element has no media.");
fAddWindowsDefine("ERROR_DESTINATION_ELEMENT_FULL",
  sDescription =    "The indicated destination element already contains media.");
fAddWindowsDefine("ERROR_ILLEGAL_ELEMENT_ADDRESS",
  sDescription =    "The indicated element does not exist.");
fAddWindowsDefine("ERROR_MAGAZINE_NOT_PRESENT",
  sDescription =    "The indicated element is part of a magazine that is not present.");
fAddWindowsDefine("ERROR_DEVICE_REINITIALIZATION_NEEDED",
  sDescription =    "The indicated device requires reinitialization due to hardware errors.");
fAddWindowsDefine("ERROR_DEVICE_REQUIRES_CLEANING",
  sDescription =    "The device has indicated that cleaning is required before further operations are attempted.");
fAddWindowsDefine("ERROR_DEVICE_DOOR_OPEN",
  sDescription =    "The device has indicated that its door is open.");
fAddWindowsDefine("ERROR_DEVICE_NOT_CONNECTED",
  sDescription =    "The device is not connected.");
fAddWindowsDefine("ERROR_NOT_FOUND",
  sDescription =    "Element not found.");
fAddWindowsDefine("ERROR_NO_MATCH",
  sDescription =    "There was no match for the specified key in the index.");
fAddWindowsDefine("ERROR_SET_NOT_FOUND",
  sDescription =    "The property set specified does not exist on the object.");
fAddWindowsDefine("ERROR_POINT_NOT_FOUND",
  sDescription =    "The point passed to GetMouseMovePoints is not in the buffer.");
fAddWindowsDefine("ERROR_NO_TRACKING_SERVICE",
  sDescription =    "The tracking (workstation) service is not running.");
fAddWindowsDefine("ERROR_NO_VOLUME_ID",
  sDescription =    "The Volume ID could not be found.");
fAddWindowsDefine("ERROR_UNABLE_TO_REMOVE_REPLACED",
  sDescription =    "Unable to remove the file to be replaced.");
fAddWindowsDefine("ERROR_UNABLE_TO_MOVE_REPLACEMENT",
  sDescription =    "Unable to move the replacement file to the file to be replaced. The file to be replaced has retained its original name.");
fAddWindowsDefine("ERROR_UNABLE_TO_MOVE_REPLACEMENT_2",
  sDescription =    "Unable to move the replacement file to the file to be replaced. The file to be replaced has been renamed using the backup name.");
fAddWindowsDefine("ERROR_JOURNAL_DELETE_IN_PROGRESS",
  sDescription =    "The volume change journal is being deleted.");
fAddWindowsDefine("ERROR_JOURNAL_NOT_ACTIVE",
  sDescription =    "The volume change journal is not active.");
fAddWindowsDefine("ERROR_POTENTIAL_FILE_FOUND",
  sDescription =    "A file was found, but it may not be the correct file.");
fAddWindowsDefine("ERROR_JOURNAL_ENTRY_DELETED",
  sDescription =    "The journal entry has been deleted from the journal.");
fAddWindowsDefine("ERROR_SHUTDOWN_IS_SCHEDULED",
  sDescription =    "A system shutdown has already been scheduled.");
fAddWindowsDefine("ERROR_SHUTDOWN_USERS_LOGGED_ON",
  sDescription =    "The system shutdown cannot be initiated because there are other users logged on to the computer.");
fAddWindowsDefine("ERROR_BAD_DEVICE",
  sDescription =    "The specified device name is invalid.");
fAddWindowsDefine("ERROR_CONNECTION_UNAVAIL",
  sDescription =    "The device is not currently connected but it is a remembered connection.");
fAddWindowsDefine("ERROR_DEVICE_ALREADY_REMEMBERED",
  sDescription =    "The local device name has a remembered connection to another network resource.");
fAddWindowsDefine("ERROR_NO_NET_OR_BAD_PATH",
  sDescription =    "The network path was either typed incorrectly, does not exist, or the network provider is not currently available. Please try retyping the path or contact your network administrator.");
fAddWindowsDefine("ERROR_BAD_PROVIDER",
  sDescription =    "The specified network provider name is invalid.");
fAddWindowsDefine("ERROR_CANNOT_OPEN_PROFILE",
  sDescription =    "Unable to open the network connection profile.");
fAddWindowsDefine("ERROR_BAD_PROFILE",
  sDescription =    "The network connection profile is corrupted.");
fAddWindowsDefine("ERROR_NOT_CONTAINER",
  sDescription =    "Cannot enumerate a noncontainer.");
fAddWindowsDefine("ERROR_EXTENDED_ERROR",
  sDescription =    "An extended error has occurred.");
fAddWindowsDefine("ERROR_INVALID_GROUPNAME",
  sDescription =    "The format of the specified group name is invalid.");
fAddWindowsDefine("ERROR_INVALID_COMPUTERNAME",
  sDescription =    "The format of the specified computer name is invalid.");
fAddWindowsDefine("ERROR_INVALID_EVENTNAME",
  sDescription =    "The format of the specified event name is invalid.");
fAddWindowsDefine("ERROR_INVALID_DOMAINNAME",
  sDescription =    "The format of the specified domain name is invalid.");
fAddWindowsDefine("ERROR_INVALID_SERVICENAME",
  sDescription =    "The format of the specified service name is invalid.");
fAddWindowsDefine("ERROR_INVALID_NETNAME",
  sDescription =    "The format of the specified network name is invalid.");
fAddWindowsDefine("ERROR_INVALID_SHARENAME",
  sDescription =    "The format of the specified share name is invalid.");
fAddWindowsDefine("ERROR_INVALID_PASSWORDNAME",
  sDescription =    "The format of the specified password is invalid.");
fAddWindowsDefine("ERROR_INVALID_MESSAGENAME",
  sDescription =    "The format of the specified message name is invalid.");
fAddWindowsDefine("ERROR_INVALID_MESSAGEDEST",
  sDescription =    "The format of the specified message destination is invalid.");
fAddWindowsDefine("ERROR_SESSION_CREDENTIAL_CONFLICT",
  sDescription =    "Multiple connections to a server or shared resource by the same user, using more than one user name, are not allowed. Disconnect all previous connections to the server or shared resource and try again.");
fAddWindowsDefine("ERROR_REMOTE_SESSION_LIMIT_EXCEEDED",
  sDescription =    "An attempt was made to establish a session to a network server, but there are already too many sessions established to that server.");
fAddWindowsDefine("ERROR_DUP_DOMAINNAME",
  sDescription =    "The workgroup or domain name is already in use by another computer on the network.");
fAddWindowsDefine("ERROR_NO_NETWORK",
  sDescription =    "The network is not present or not started.");
fAddWindowsDefine("ERROR_CANCELLED",
  sDescription =    "The operation was canceled by the user.");
fAddWindowsDefine("ERROR_USER_MAPPED_FILE",
  sDescription =    "The requested operation cannot be performed on a file with a user-mapped section open.");
fAddWindowsDefine("ERROR_CONNECTION_REFUSED",
  sDescription =    "The remote computer refused the network connection.");
fAddWindowsDefine("ERROR_GRACEFUL_DISCONNECT",
  sDescription =    "The network connection was gracefully closed.");
fAddWindowsDefine("ERROR_ADDRESS_ALREADY_ASSOCIATED",
  sDescription =    "The network transport endpoint already has an address associated with it.");
fAddWindowsDefine("ERROR_ADDRESS_NOT_ASSOCIATED",
  sDescription =    "An address has not yet been associated with the network endpoint.");
fAddWindowsDefine("ERROR_CONNECTION_INVALID",
  sDescription =    "An operation was attempted on a nonexistent network connection.");
fAddWindowsDefine("ERROR_CONNECTION_ACTIVE",
  sDescription =    "An invalid operation was attempted on an active network connection.");
fAddWindowsDefine("ERROR_NETWORK_UNREACHABLE",
  sDescription =    "The network location cannot be reached. For information about network troubleshooting, see Windows Help.");
fAddWindowsDefine("ERROR_HOST_UNREACHABLE",
  sDescription =    "The network location cannot be reached. For information about network troubleshooting, see Windows Help.");
fAddWindowsDefine("ERROR_PROTOCOL_UNREACHABLE",
  sDescription =    "The network location cannot be reached. For information about network troubleshooting, see Windows Help.");
fAddWindowsDefine("ERROR_PORT_UNREACHABLE",
  sDescription =    "No service is operating at the destination network endpoint on the remote system.");
fAddWindowsDefine("ERROR_REQUEST_ABORTED",
  sDescription =    "The request was aborted.");
fAddWindowsDefine("ERROR_CONNECTION_ABORTED",
  sDescription =    "The network connection was aborted by the local system.");
fAddWindowsDefine("ERROR_RETRY",
  sDescription =    "The operation could not be completed. A retry should be performed.");
fAddWindowsDefine("ERROR_CONNECTION_COUNT_LIMIT",
  sDescription =    "A connection to the server could not be made because the limit on the number of concurrent connections for this account has been reached.");
fAddWindowsDefine("ERROR_LOGIN_TIME_RESTRICTION",
  sDescription =    "Attempting to log in during an unauthorized time of day for this account.");
fAddWindowsDefine("ERROR_LOGIN_WKSTA_RESTRICTION",
  sDescription =    "The account is not authorized to log in from this station.");
fAddWindowsDefine("ERROR_INCORRECT_ADDRESS",
  sDescription =    "The network address could not be used for the operation requested.");
fAddWindowsDefine("ERROR_ALREADY_REGISTERED",
  sDescription =    "The service is already registered.");
fAddWindowsDefine("ERROR_SERVICE_NOT_FOUND",
  sDescription =    "The specified service does not exist.");
fAddWindowsDefine("ERROR_NOT_AUTHENTICATED",
  sDescription =    "The operation being requested was not performed because the user has not been authenticated.");
fAddWindowsDefine("ERROR_NOT_LOGGED_ON",
  sDescription =    "The operation being requested was not performed because the user has not logged on to the network. The specified service does not exist.");
fAddWindowsDefine("ERROR_CONTINUE",
  sDescription =    "Continue with work in progress.");
fAddWindowsDefine("ERROR_ALREADY_INITIALIZED",
  sDescription =    "An attempt was made to perform an initialization operation when initialization has already been completed.");
fAddWindowsDefine("ERROR_NO_MORE_DEVICES",
  sDescription =    "No more local devices.");
fAddWindowsDefine("ERROR_NO_SUCH_SITE",
  sDescription =    "The specified site does not exist.");
fAddWindowsDefine("ERROR_DOMAIN_CONTROLLER_EXISTS",
  sDescription =    "A domain controller with the specified name already exists.");
fAddWindowsDefine("ERROR_ONLY_IF_CONNECTED",
  sDescription =    "This operation is supported only when you are connected to the server.");
fAddWindowsDefine("ERROR_OVERRIDE_NOCHANGES",
  sDescription =    "The group policy framework should call the extension even if there are no changes.");
fAddWindowsDefine("ERROR_BAD_USER_PROFILE",
  sDescription =    "The specified user does not have a valid profile.");
fAddWindowsDefine("ERROR_NOT_SUPPORTED_ON_SBS",
  sDescription =    "This operation is not supported on a computer running Windows Server 2003 for Small Business Server");
fAddWindowsDefine("ERROR_SERVER_SHUTDOWN_IN_PROGRESS",
  sDescription =    "The server machine is shutting down.");
fAddWindowsDefine("ERROR_HOST_DOWN",
  sDescription =    "The remote system is not available. For information about network troubleshooting, see Windows Help.");
fAddWindowsDefine("ERROR_NON_ACCOUNT_SID",
  sDescription =    "The security identifier provided is not from an account domain.");
fAddWindowsDefine("ERROR_NON_DOMAIN_SID",
  sDescription =    "The security identifier provided does not have a domain component.");
fAddWindowsDefine("ERROR_APPHELP_BLOCK",
  sDescription =    "AppHelp dialog canceled thus preventing the application from starting.");
fAddWindowsDefine("ERROR_ACCESS_DISABLED_BY_POLICY",
  sDescription =    "This program is blocked by group policy. For more information, contact your system administrator.");
fAddWindowsDefine("ERROR_REG_NAT_CONSUMPTION",
  sDescription =    "A program attempt to use an invalid register value. Normally caused by an uninitialized register. This error is Itanium specific.");
fAddWindowsDefine("ERROR_CSCSHARE_OFFLINE",
  sDescription =    "The share is currently offline or does not exist.");
fAddWindowsDefine("ERROR_PKINIT_FAILURE",
  sDescription =    "The Kerberos protocol encountered an error while validating the KDC certificate during smartcard logon. There is more information in the system event log.");
fAddWindowsDefine("ERROR_SMARTCARD_SUBSYSTEM_FAILURE",
  sDescription =    "The Kerberos protocol encountered an error while attempting to utilize the smartcard subsystem.");
fAddWindowsDefine("ERROR_DOWNGRADE_DETECTED",
  sDescription =    "The system cannot contact a domain controller to service the authentication request. Please try again later.");
fAddWindowsDefine("ERROR_MACHINE_LOCKED",
  sDescription =    "The machine is locked and cannot be shut down without the force option.");
fAddWindowsDefine("ERROR_CALLBACK_SUPPLIED_INVALID_DATA",
  sDescription =    "An application-defined callback gave invalid data when called.");
fAddWindowsDefine("ERROR_SYNC_FOREGROUND_REFRESH_REQUIRED",
  sDescription =    "The group policy framework should call the extension in the synchronous foreground policy refresh.");
fAddWindowsDefine("ERROR_DRIVER_BLOCKED",
  sDescription =    "This driver has been blocked from loading");
fAddWindowsDefine("ERROR_INVALID_IMPORT_OF_NON_DLL",
  sDescription =    "A dynamic link library (DLL) referenced a module that was neither a DLL nor the process's executable image.");
fAddWindowsDefine("ERROR_ACCESS_DISABLED_WEBBLADE",
  sDescription =    "Windows cannot open this program since it has been disabled.");
fAddWindowsDefine("ERROR_ACCESS_DISABLED_WEBBLADE_TAMPER",
  sDescription =    "Windows cannot open this program because the license enforcement system has been tampered with or become corrupted.");
fAddWindowsDefine("ERROR_RECOVERY_FAILURE",
  sDescription =    "A transaction recover failed.");
fAddWindowsDefine("ERROR_ALREADY_FIBER",
  sDescription =    "The current thread has already been converted to a fiber.");
fAddWindowsDefine("ERROR_ALREADY_THREAD",
  sDescription =    "The current thread has already been converted from a fiber.");
fAddWindowsDefine("ERROR_STACK_BUFFER_OVERRUN",
  sDescription =    "The system detected an overrun of a stack-based buffer in this application. This overrun could potentially allow a malicious user to gain control of this application.");
fAddWindowsDefine("ERROR_PARAMETER_QUOTA_EXCEEDED",
  sDescription =    "Data present in one of the parameters is more than the function can operate on.");
fAddWindowsDefine("ERROR_DEBUGGER_INACTIVE",
  sDescription =    "An attempt to do an operation on a debug object failed because the object is in the process of being deleted.");
fAddWindowsDefine("ERROR_DELAY_LOAD_FAILED",
  sDescription =    "An attempt to delay-load a .dll or get a function address in a delay-loaded .dll failed.");
fAddWindowsDefine("ERROR_VDM_DISALLOWED",
  sDescription =    "%1 is a 16-bit application. You do not have permissions to execute 16-bit applications. Check your permissions with your system administrator.");
fAddWindowsDefine("ERROR_UNIDENTIFIED_ERROR",
  sDescription =    "Insufficient information exists to identify the cause of failure.");
fAddWindowsDefine("ERROR_INVALID_CRUNTIME_PARAMETER",
  sDescription =    "The parameter passed to a C runtime function is incorrect.");
fAddWindowsDefine("ERROR_BEYOND_VDL",
  sDescription =    "The operation occurred beyond the valid data length of the file.");
fAddWindowsDefine("ERROR_INCOMPATIBLE_SERVICE_SID_TYPE",
  sDescription =    "The service start failed since one or more services in the same process have an incompatible service SID type setting. A service with restricted service SID type can only coexist in the same process with other services with a restricted SID type. If the service SID type for this service was just configured, the hosting process must be restarted in order to start this service.");
fAddWindowsDefine("ERROR_DRIVER_PROCESS_TERMINATED",
  sDescription =    "The process hosting the driver for this device has been terminated.");
fAddWindowsDefine("ERROR_IMPLEMENTATION_LIMIT",
  sDescription =    "An operation attempted to exceed an implementation-defined limit.");
fAddWindowsDefine("ERROR_PROCESS_IS_PROTECTED",
  sDescription =    "Either the target process, or the target thread's containing process, is a protected process.");
fAddWindowsDefine("ERROR_SERVICE_NOTIFY_CLIENT_LAGGING",
  sDescription =    "The service notification client is lagging too far behind the current state of services in the machine.");
fAddWindowsDefine("ERROR_DISK_QUOTA_EXCEEDED",
  sDescription =    "The requested file operation failed because the storage quota was exceeded. To free up disk space, move files to a different location or delete unnecessary files. For more information, contact your system administrator.");
fAddWindowsDefine("ERROR_CONTENT_BLOCKED",
  sDescription =    "The requested file operation failed because the storage policy blocks that type of file. For more information, contact your system administrator.");
fAddWindowsDefine("ERROR_INCOMPATIBLE_SERVICE_PRIVILEGE",
  sDescription =    "A privilege that the service requires to function properly does not exist in the service account configuration. You may use the Services Microsoft Management Console (MMC) snap-in (services.msc) and the Local Security Settings MMC snap-in (secpol.msc) to view the service configuration and the account configuration.");
fAddWindowsDefine("ERROR_APP_HANG",
  sDescription =    "A thread involved in this operation appears to be unresponsive.");
fAddWindowsDefine("ERROR_INVALID_LABEL",
  sDescription =    "Indicates a particular Security ID may not be assigned as the label of an object.");
fAddWindowsDefine("ERROR_NOT_ALL_ASSIGNED",
  sDescription =    "Not all privileges or groups referenced are assigned to the caller.");
fAddWindowsDefine("ERROR_SOME_NOT_MAPPED",
  sDescription =    "Some mapping between account names and security IDs was not done.");
fAddWindowsDefine("ERROR_NO_QUOTAS_FOR_ACCOUNT",
  sDescription =    "No system quota limits are specifically set for this account.");
fAddWindowsDefine("ERROR_LOCAL_USER_SESSION_KEY",
  sDescription =    "No encryption key is available. A well-known encryption key was returned.");
fAddWindowsDefine("ERROR_NULL_LM_PASSWORD",
  sDescription =    "The password is too complex to be converted to a LAN Manager password. The LAN Manager password returned is a NULL string.");
fAddWindowsDefine("ERROR_UNKNOWN_REVISION",
  sDescription =    "The revision level is unknown.");
fAddWindowsDefine("ERROR_REVISION_MISMATCH",
  sDescription =    "Indicates two revision levels are incompatible.");
fAddWindowsDefine("ERROR_INVALID_OWNER",
  sDescription =    "This security ID may not be assigned as the owner of this object.");
fAddWindowsDefine("ERROR_INVALID_PRIMARY_GROUP",
  sDescription =    "This security ID may not be assigned as the primary group of an object.");
fAddWindowsDefine("ERROR_NO_IMPERSONATION_TOKEN",
  sDescription =    "An attempt has been made to operate on an impersonation token by a thread that is not currently impersonating a client.");
fAddWindowsDefine("ERROR_CANT_DISABLE_MANDATORY",
  sDescription =    "The group may not be disabled.");
fAddWindowsDefine("ERROR_NO_LOGON_SERVERS",
  sDescription =    "There are currently no logon servers available to service the logon request.");
fAddWindowsDefine("ERROR_NO_SUCH_LOGON_SESSION",
  sDescription =    "A specified logon session does not exist. It may already have been terminated.");
fAddWindowsDefine("ERROR_NO_SUCH_PRIVILEGE",
  sDescription =    "A specified privilege does not exist.");
fAddWindowsDefine("ERROR_PRIVILEGE_NOT_HELD",
  sDescription =    "A required privilege is not held by the client.");
fAddWindowsDefine("ERROR_INVALID_ACCOUNT_NAME",
  sDescription =    "The name provided is not a properly formed account name.");
fAddWindowsDefine("ERROR_USER_EXISTS",
  sDescription =    "The specified account already exists.");
fAddWindowsDefine("ERROR_NO_SUCH_USER",
  sDescription =    "The specified account does not exist.");
fAddWindowsDefine("ERROR_GROUP_EXISTS",
  sDescription =    "The specified group already exists.");
fAddWindowsDefine("ERROR_NO_SUCH_GROUP",
  sDescription =    "The specified group does not exist.");
fAddWindowsDefine("ERROR_MEMBER_IN_GROUP",
  sDescription =    "Either the specified user account is already a member of the specified group, or the specified group cannot be deleted because it contains a member.");
fAddWindowsDefine("ERROR_MEMBER_NOT_IN_GROUP",
  sDescription =    "The specified user account is not a member of the specified group account.");
fAddWindowsDefine("ERROR_LAST_ADMIN",
  sDescription =    "This operation is disallowed as it could result in an administration account being disabled, deleted or unable to logon.");
fAddWindowsDefine("ERROR_WRONG_PASSWORD",
  sDescription =    "Unable to update the password. The value provided as the current password is incorrect.");
fAddWindowsDefine("ERROR_ILL_FORMED_PASSWORD",
  sDescription =    "Unable to update the password. The value provided for the new password contains values that are not allowed in passwords.");
fAddWindowsDefine("ERROR_PASSWORD_RESTRICTION",
  sDescription =    "Unable to update the password. The value provided for the new password does not meet the length, complexity, or history requirements of the domain.");
fAddWindowsDefine("ERROR_LOGON_FAILURE",
  sDescription =    "The user name or password is incorrect.");
fAddWindowsDefine("ERROR_ACCOUNT_RESTRICTION",
  sDescription =    "Account restrictions are preventing this user from signing in. For example: blank passwords aren't allowed, sign-in times are limited, or a policy restriction has been enforced.");
fAddWindowsDefine("ERROR_INVALID_LOGON_HOURS",
  sDescription =    "Your account has time restrictions that keep you from signing in right now.");
fAddWindowsDefine("ERROR_INVALID_WORKSTATION",
  sDescription =    "This user isn't allowed to sign in to this computer.");
fAddWindowsDefine("ERROR_PASSWORD_EXPIRED",
  sDescription =    "The password for this account has expired.");
fAddWindowsDefine("ERROR_ACCOUNT_DISABLED",
  sDescription =    "This user can't sign in because this account is currently disabled.");
fAddWindowsDefine("ERROR_NONE_MAPPED",
  sDescription =    "No mapping between account names and security IDs was done.");
fAddWindowsDefine("ERROR_TOO_MANY_LUIDS_REQUESTED",
  sDescription =    "Too many local user identifiers (LUIDs) were requested at one time.");
fAddWindowsDefine("ERROR_LUIDS_EXHAUSTED",
  sDescription =    "No more local user identifiers (LUIDs) are available.");
fAddWindowsDefine("ERROR_INVALID_SUB_AUTHORITY",
  sDescription =    "The subauthority part of a security ID is invalid for this particular use.");
fAddWindowsDefine("ERROR_INVALID_ACL",
  sDescription =    "The access control list (ACL) structure is invalid.");
fAddWindowsDefine("ERROR_INVALID_SID",
  sDescription =    "The security ID structure is invalid.");
fAddWindowsDefine("ERROR_INVALID_SECURITY_DESCR",
  sDescription =    "The security descriptor structure is invalid.");
fAddWindowsDefine("ERROR_BAD_INHERITANCE_ACL",
  sDescription =    "The inherited access control list (ACL) or access control entry (ACE) could not be built.");
fAddWindowsDefine("ERROR_SERVER_DISABLED",
  sDescription =    "The server is currently disabled.");
fAddWindowsDefine("ERROR_SERVER_NOT_DISABLED",
  sDescription =    "The server is currently enabled.");
fAddWindowsDefine("ERROR_INVALID_ID_AUTHORITY",
  sDescription =    "The value provided was an invalid value for an identifier authority.");
fAddWindowsDefine("ERROR_ALLOTTED_SPACE_EXCEEDED",
  sDescription =    "No more memory is available for security information updates.");
fAddWindowsDefine("ERROR_INVALID_GROUP_ATTRIBUTES",
  sDescription =    "The specified attributes are invalid, or incompatible with the attributes for the group as a whole.");
fAddWindowsDefine("ERROR_BAD_IMPERSONATION_LEVEL",
  sDescription =    "Either a required impersonation level was not provided, or the provided impersonation level is invalid.");
fAddWindowsDefine("ERROR_CANT_OPEN_ANONYMOUS",
  sDescription =    "Cannot open an anonymous level security token.");
fAddWindowsDefine("ERROR_BAD_VALIDATION_CLASS",
  sDescription =    "The validation information class requested was invalid.");
fAddWindowsDefine("ERROR_BAD_TOKEN_TYPE",
  sDescription =    "The type of the token is inappropriate for its attempted use.");
fAddWindowsDefine("ERROR_NO_SECURITY_ON_OBJECT",
  sDescription =    "Unable to perform a security operation on an object that has no associated security.");
fAddWindowsDefine("ERROR_CANT_ACCESS_DOMAIN_INFO",
  sDescription =    "Configuration information could not be read from the domain controller, either because the machine is unavailable, or access has been denied.");
fAddWindowsDefine("ERROR_INVALID_SERVER_STATE",
  sDescription =    "The security account manager (SAM) or local security authority (LSA) server was in the wrong state to perform the security operation.");
fAddWindowsDefine("ERROR_INVALID_DOMAIN_STATE",
  sDescription =    "The domain was in the wrong state to perform the security operation.");
fAddWindowsDefine("ERROR_INVALID_DOMAIN_ROLE",
  sDescription =    "This operation is only allowed for the Primary Domain Controller of the domain.");
fAddWindowsDefine("ERROR_NO_SUCH_DOMAIN",
  sDescription =    "The specified domain either does not exist or could not be contacted.");
fAddWindowsDefine("ERROR_DOMAIN_EXISTS",
  sDescription =    "The specified domain already exists.");
fAddWindowsDefine("ERROR_DOMAIN_LIMIT_EXCEEDED",
  sDescription =    "An attempt was made to exceed the limit on the number of domains per server.");
fAddWindowsDefine("ERROR_INTERNAL_DB_CORRUPTION",
  sDescription =    "Unable to complete the requested operation because of either a catastrophic media failure or a data structure corruption on the disk.");
fAddWindowsDefine("ERROR_INTERNAL_ERROR",
  sDescription =    "An internal error occurred.");
fAddWindowsDefine("ERROR_GENERIC_NOT_MAPPED",
  sDescription =    "Generic access types were contained in an access mask which should already be mapped to nongeneric types.");
fAddWindowsDefine("ERROR_BAD_DESCRIPTOR_FORMAT",
  sDescription =    "A security descriptor is not in the right format (absolute or self-relative).");
fAddWindowsDefine("ERROR_NOT_LOGON_PROCESS",
  sDescription =    "The requested action is restricted for use by logon processes only. The calling process has not registered as a logon process.");
fAddWindowsDefine("ERROR_LOGON_SESSION_EXISTS",
  sDescription =    "Cannot start a new logon session with an ID that is already in use.");
fAddWindowsDefine("ERROR_NO_SUCH_PACKAGE",
  sDescription =    "A specified authentication package is unknown.");
fAddWindowsDefine("ERROR_BAD_LOGON_SESSION_STATE",
  sDescription =    "The logon session is not in a state that is consistent with the requested operation.");
fAddWindowsDefine("ERROR_LOGON_SESSION_COLLISION",
  sDescription =    "The logon session ID is already in use.");
fAddWindowsDefine("ERROR_INVALID_LOGON_TYPE",
  sDescription =    "A logon request contained an invalid logon type value.");
fAddWindowsDefine("ERROR_CANNOT_IMPERSONATE",
  sDescription =    "Unable to impersonate using a named pipe until data has been read from that pipe.");
fAddWindowsDefine("ERROR_RXACT_INVALID_STATE",
  sDescription =    "The transaction state of a registry subtree is incompatible with the requested operation.");
fAddWindowsDefine("ERROR_RXACT_COMMIT_FAILURE",
  sDescription =    "An internal security database corruption has been encountered.");
fAddWindowsDefine("ERROR_SPECIAL_ACCOUNT",
  sDescription =    "Cannot perform this operation on built-in accounts.");
fAddWindowsDefine("ERROR_SPECIAL_GROUP",
  sDescription =    "Cannot perform this operation on this built-in special group.");
fAddWindowsDefine("ERROR_SPECIAL_USER",
  sDescription =    "Cannot perform this operation on this built-in special user.");
fAddWindowsDefine("ERROR_MEMBERS_PRIMARY_GROUP",
  sDescription =    "The user cannot be removed from a group because the group is currently the user's primary group.");
fAddWindowsDefine("ERROR_TOKEN_ALREADY_IN_USE",
  sDescription =    "The token is already in use as a primary token.");
fAddWindowsDefine("ERROR_NO_SUCH_ALIAS",
  sDescription =    "The specified local group does not exist.");
fAddWindowsDefine("ERROR_MEMBER_NOT_IN_ALIAS",
  sDescription =    "The specified account name is not a member of the group.");
fAddWindowsDefine("ERROR_MEMBER_IN_ALIAS",
  sDescription =    "The specified account name is already a member of the group.");
fAddWindowsDefine("ERROR_ALIAS_EXISTS",
  sDescription =    "The specified local group already exists.");
fAddWindowsDefine("ERROR_LOGON_NOT_GRANTED",
  sDescription =    "Logon failure: the user has not been granted the requested logon type at this computer.");
fAddWindowsDefine("ERROR_TOO_MANY_SECRETS",
  sDescription =    "The maximum number of secrets that may be stored in a single system has been exceeded.");
fAddWindowsDefine("ERROR_SECRET_TOO_LONG",
  sDescription =    "The length of a secret exceeds the maximum length allowed.");
fAddWindowsDefine("ERROR_INTERNAL_DB_ERROR",
  sDescription =    "The local security authority database contains an internal inconsistency.");
fAddWindowsDefine("ERROR_TOO_MANY_CONTEXT_IDS",
  sDescription =    "During a logon attempt, the user's security context accumulated too many security IDs.");
fAddWindowsDefine("ERROR_LOGON_TYPE_NOT_GRANTED",
  sDescription =    "Logon failure: the user has not been granted the requested logon type at this computer.");
fAddWindowsDefine("ERROR_NT_CROSS_ENCRYPTION_REQUIRED",
  sDescription =    "A cross-encrypted password is necessary to change a user password.");
fAddWindowsDefine("ERROR_NO_SUCH_MEMBER",
  sDescription =    "A member could not be added to or removed from the local group because the member does not exist.");
fAddWindowsDefine("ERROR_INVALID_MEMBER",
  sDescription =    "A new member could not be added to a local group because the member has the wrong account type.");
fAddWindowsDefine("ERROR_TOO_MANY_SIDS",
  sDescription =    "Too many security IDs have been specified.");
fAddWindowsDefine("ERROR_LM_CROSS_ENCRYPTION_REQUIRED",
  sDescription =    "A cross-encrypted password is necessary to change this user password.");
fAddWindowsDefine("ERROR_NO_INHERITANCE",
  sDescription =    "Indicates an ACL contains no inheritable components.");
fAddWindowsDefine("ERROR_FILE_CORRUPT",
  sDescription =    "The file or directory is corrupted and unreadable.");
fAddWindowsDefine("ERROR_DISK_CORRUPT",
  sDescription =    "The disk structure is corrupted and unreadable.");
fAddWindowsDefine("ERROR_NO_USER_SESSION_KEY",
  sDescription =    "There is no user session key for the specified logon session.");
fAddWindowsDefine("ERROR_LICENSE_QUOTA_EXCEEDED",
  sDescription =    "The service being accessed is licensed for a particular number of connections. No more connections can be made to the service at this time because there are already as many connections as the service can accept.");
fAddWindowsDefine("ERROR_WRONG_TARGET_NAME",
  sDescription =    "The target account name is incorrect.");
fAddWindowsDefine("ERROR_MUTUAL_AUTH_FAILED",
  sDescription =    "Mutual Authentication failed. The server's password is out of date at the domain controller.");
fAddWindowsDefine("ERROR_TIME_SKEW",
  sDescription =    "There is a time and/or date difference between the client and server.");
fAddWindowsDefine("ERROR_CURRENT_DOMAIN_NOT_ALLOWED",
  sDescription =    "This operation cannot be performed on the current domain.");
fAddWindowsDefine("ERROR_INVALID_WINDOW_HANDLE",
  sDescription =    "Invalid window handle.");
fAddWindowsDefine("ERROR_INVALID_MENU_HANDLE",
  sDescription =    "Invalid menu handle.");
fAddWindowsDefine("ERROR_INVALID_CURSOR_HANDLE",
  sDescription =    "Invalid cursor handle.");
fAddWindowsDefine("ERROR_INVALID_ACCEL_HANDLE",
  sDescription =    "Invalid accelerator table handle.");
fAddWindowsDefine("ERROR_INVALID_HOOK_HANDLE",
  sDescription =    "Invalid hook handle.");
fAddWindowsDefine("ERROR_INVALID_DWP_HANDLE",
  sDescription =    "Invalid handle to a multiple-window position structure.");
fAddWindowsDefine("ERROR_TLW_WITH_WSCHILD",
  sDescription =    "Cannot create a top-level child window.");
fAddWindowsDefine("ERROR_CANNOT_FIND_WND_CLASS",
  sDescription =    "Cannot find window class.");
fAddWindowsDefine("ERROR_WINDOW_OF_OTHER_THREAD",
  sDescription =    "Invalid window; it belongs to other thread.");
fAddWindowsDefine("ERROR_HOTKEY_ALREADY_REGISTERED",
  sDescription =    "Hot key is already registered.");
fAddWindowsDefine("ERROR_CLASS_ALREADY_EXISTS",
  sDescription =    "Class already exists.");
fAddWindowsDefine("ERROR_CLASS_DOES_NOT_EXIST",
  sDescription =    "Class does not exist.");
fAddWindowsDefine("ERROR_CLASS_HAS_WINDOWS",
  sDescription =    "Class still has open windows.");
fAddWindowsDefine("ERROR_INVALID_INDEX",
  sDescription =    "Invalid index.");
fAddWindowsDefine("ERROR_INVALID_ICON_HANDLE",
  sDescription =    "Invalid icon handle.");
fAddWindowsDefine("ERROR_PRIVATE_DIALOG_INDEX",
  sDescription =    "Using private DIALOG window words.");
fAddWindowsDefine("ERROR_LISTBOX_ID_NOT_FOUND",
  sDescription =    "The list box identifier was not found.");
fAddWindowsDefine("ERROR_NO_WILDCARD_CHARACTERS",
  sDescription =    "No wildcards were found.");
fAddWindowsDefine("ERROR_CLIPBOARD_NOT_OPEN",
  sDescription =    "Thread does not have a clipboard open.");
fAddWindowsDefine("ERROR_HOTKEY_NOT_REGISTERED",
  sDescription =    "Hot key is not registered.");
fAddWindowsDefine("ERROR_WINDOW_NOT_DIALOG",
  sDescription =    "The window is not a valid dialog window.");
fAddWindowsDefine("ERROR_CONTROL_ID_NOT_FOUND",
  sDescription =    "Control ID not found.");
fAddWindowsDefine("ERROR_INVALID_COMBOBOX_MESSAGE",
  sDescription =    "Invalid message for a combo box because it does not have an edit control.");
fAddWindowsDefine("ERROR_WINDOW_NOT_COMBOBOX",
  sDescription =    "The window is not a combo box.");
fAddWindowsDefine("ERROR_INVALID_EDIT_HEIGHT",
  sDescription =    "Height must be less than 256.");
fAddWindowsDefine("ERROR_DC_NOT_FOUND",
  sDescription =    "Invalid device context (DC) handle.");
fAddWindowsDefine("ERROR_INVALID_HOOK_FILTER",
  sDescription =    "Invalid hook procedure type.");
fAddWindowsDefine("ERROR_INVALID_FILTER_PROC",
  sDescription =    "Invalid hook procedure.");
fAddWindowsDefine("ERROR_HOOK_NEEDS_HMOD",
  sDescription =    "Cannot set nonlocal hook without a module handle.");
fAddWindowsDefine("ERROR_GLOBAL_ONLY_HOOK",
  sDescription =    "This hook procedure can only be set globally.");
fAddWindowsDefine("ERROR_JOURNAL_HOOK_SET",
  sDescription =    "The journal hook procedure is already installed.");
fAddWindowsDefine("ERROR_HOOK_NOT_INSTALLED",
  sDescription =    "The hook procedure is not installed.");
fAddWindowsDefine("ERROR_INVALID_LB_MESSAGE",
  sDescription =    "Invalid message for single-selection list box.");
fAddWindowsDefine("ERROR_SETCOUNT_ON_BAD_LB",
  sDescription =    "LB_SETCOUNT sent to non-lazy list box.");
fAddWindowsDefine("ERROR_LB_WITHOUT_TABSTOPS",
  sDescription =    "This list box does not support tab stops.");
fAddWindowsDefine("ERROR_DESTROY_OBJECT_OF_OTHER_THREAD",
  sDescription =    "Cannot destroy object created by another thread.");
fAddWindowsDefine("ERROR_CHILD_WINDOW_MENU",
  sDescription =    "Child windows cannot have menus.");
fAddWindowsDefine("ERROR_NO_SYSTEM_MENU",
  sDescription =    "The window does not have a system menu.");
fAddWindowsDefine("ERROR_INVALID_MSGBOX_STYLE",
  sDescription =    "Invalid message box style.");
fAddWindowsDefine("ERROR_INVALID_SPI_VALUE",
  sDescription =    "Invalid system-wide (SPI_*) parameter.");
fAddWindowsDefine("ERROR_SCREEN_ALREADY_LOCKED",
  sDescription =    "Screen already locked.");
fAddWindowsDefine("ERROR_HWNDS_HAVE_DIFF_PARENT",
  sDescription =    "All handles to windows in a multiple-window position structure must have the same parent.");
fAddWindowsDefine("ERROR_NOT_CHILD_WINDOW",
  sDescription =    "The window is not a child window.");
fAddWindowsDefine("ERROR_INVALID_GW_COMMAND",
  sDescription =    "Invalid GW_* command.");
fAddWindowsDefine("ERROR_INVALID_THREAD_ID",
  sDescription =    "Invalid thread identifier.");
fAddWindowsDefine("ERROR_NON_MDICHILD_WINDOW",
  sDescription =    "Cannot process a message from a window that is not a multiple document interface (MDI) window.");
fAddWindowsDefine("ERROR_POPUP_ALREADY_ACTIVE",
  sDescription =    "Popup menu already active.");
fAddWindowsDefine("ERROR_NO_SCROLLBARS",
  sDescription =    "The window does not have scroll bars.");
fAddWindowsDefine("ERROR_INVALID_SCROLLBAR_RANGE",
  sDescription =    "Scroll bar range cannot be greater than MAXLONG.");
fAddWindowsDefine("ERROR_INVALID_SHOWWIN_COMMAND",
  sDescription =    "Cannot show or remove the window in the way specified.");
fAddWindowsDefine("ERROR_NO_SYSTEM_RESOURCES",
  sDescription =    "Insufficient system resources exist to complete the requested service.");
fAddWindowsDefine("ERROR_NONPAGED_SYSTEM_RESOURCES",
  sDescription =    "Insufficient system resources exist to complete the requested service.");
fAddWindowsDefine("ERROR_PAGED_SYSTEM_RESOURCES",
  sDescription =    "Insufficient system resources exist to complete the requested service.");
fAddWindowsDefine("ERROR_WORKING_SET_QUOTA",
  sDescription =    "Insufficient quota to complete the requested service.");
fAddWindowsDefine("ERROR_PAGEFILE_QUOTA",
  sDescription =    "Insufficient quota to complete the requested service.");
fAddWindowsDefine("ERROR_COMMITMENT_LIMIT",
  sDescription =    "The paging file is too small for this operation to complete.");
fAddWindowsDefine("ERROR_MENU_ITEM_NOT_FOUND",
  sDescription =    "A menu item was not found.");
fAddWindowsDefine("ERROR_INVALID_KEYBOARD_HANDLE",
  sDescription =    "Invalid keyboard layout handle.");
fAddWindowsDefine("ERROR_HOOK_TYPE_NOT_ALLOWED",
  sDescription =    "Hook type not allowed.");
fAddWindowsDefine("ERROR_REQUIRES_INTERACTIVE_WINDOWSTATION",
  sDescription =    "This operation requires an interactive window station.");
fAddWindowsDefine("ERROR_TIMEOUT",
  sDescription =    "This operation returned because the timeout period expired.");
fAddWindowsDefine("ERROR_INVALID_MONITOR_HANDLE",
  sDescription =    "Invalid monitor handle.");
fAddWindowsDefine("ERROR_INCORRECT_SIZE",
  sDescription =    "Incorrect size argument.");
fAddWindowsDefine("ERROR_SYMLINK_CLASS_DISABLED",
  sDescription =    "The symbolic link cannot be followed because its type is disabled.");
fAddWindowsDefine("ERROR_SYMLINK_NOT_SUPPORTED",
  sDescription =    "This application does not support the current operation on symbolic links.");
fAddWindowsDefine("ERROR_XML_PARSE_ERROR",
  sDescription =    "Windows was unable to parse the requested XML data.");
fAddWindowsDefine("ERROR_XMLDSIG_ERROR",
  sDescription =    "An error was encountered while processing an XML digital signature.");
fAddWindowsDefine("ERROR_RESTART_APPLICATION",
  sDescription =    "This application must be restarted.");
fAddWindowsDefine("ERROR_WRONG_COMPARTMENT",
  sDescription =    "The caller made the connection request in the wrong routing compartment.");
fAddWindowsDefine("ERROR_AUTHIP_FAILURE",
  sDescription =    "There was an AuthIP failure when attempting to connect to the remote host.");
fAddWindowsDefine("ERROR_NO_NVRAM_RESOURCES",
  sDescription =    "Insufficient NVRAM resources exist to complete the requested service. A reboot might be required.");
fAddWindowsDefine("ERROR_NOT_GUI_PROCESS",
  sDescription =    "Unable to finish the requested operation because the specified process is not a GUI process.");
fAddWindowsDefine("ERROR_EVENTLOG_FILE_CORRUPT",
  sDescription =    "The event log file is corrupted.");
fAddWindowsDefine("ERROR_EVENTLOG_CANT_START",
  sDescription =    "No event log file could be opened, so the event logging service did not start.");
fAddWindowsDefine("ERROR_LOG_FILE_FULL",
  sDescription =    "The event log file is full.");
fAddWindowsDefine("ERROR_EVENTLOG_FILE_CHANGED",
  sDescription =    "The event log file has changed between read operations.");
fAddWindowsDefine("ERROR_INVALID_TASK_NAME",
  sDescription =    "The specified task name is invalid.");
fAddWindowsDefine("ERROR_INVALID_TASK_INDEX",
  sDescription =    "The specified task index is invalid.");
fAddWindowsDefine("ERROR_THREAD_ALREADY_IN_TASK",
  sDescription =    "The specified thread is already joining a task.");
fAddWindowsDefine("ERROR_INSTALL_SERVICE_FAILURE",
  sDescription =    "The Windows Installer Service could not be accessed. This can occur if the Windows Installer is not correctly installed. Contact your support personnel for assistance.");
fAddWindowsDefine("ERROR_INSTALL_USEREXIT",
  sDescription =    "User cancelled installation.");
fAddWindowsDefine("ERROR_INSTALL_FAILURE",
  sDescription =    "Fatal error during installation.");
fAddWindowsDefine("ERROR_INSTALL_SUSPEND",
  sDescription =    "Installation suspended, incomplete.");
fAddWindowsDefine("ERROR_UNKNOWN_PRODUCT",
  sDescription =    "This action is only valid for products that are currently installed.");
fAddWindowsDefine("ERROR_UNKNOWN_FEATURE",
  sDescription =    "Feature ID not registered.");
fAddWindowsDefine("ERROR_UNKNOWN_COMPONENT",
  sDescription =    "Component ID not registered.");
fAddWindowsDefine("ERROR_UNKNOWN_PROPERTY",
  sDescription =    "Unknown property.");
fAddWindowsDefine("ERROR_INVALID_HANDLE_STATE",
  sDescription =    "Handle is in an invalid state.");
fAddWindowsDefine("ERROR_BAD_CONFIGURATION",
  sDescription =    "The configuration data for this product is corrupt. Contact your support personnel.");
fAddWindowsDefine("ERROR_INDEX_ABSENT",
  sDescription =    "Component qualifier not present.");
fAddWindowsDefine("ERROR_INSTALL_SOURCE_ABSENT",
  sDescription =    "The installation source for this product is not available. Verify that the source exists and that you can access it.");
fAddWindowsDefine("ERROR_INSTALL_PACKAGE_VERSION",
  sDescription =    "This installation package cannot be installed by the Windows Installer service. You must install a Windows service pack that contains a newer version of the Windows Installer service.");
fAddWindowsDefine("ERROR_PRODUCT_UNINSTALLED",
  sDescription =    "Product is uninstalled.");
fAddWindowsDefine("ERROR_BAD_QUERY_SYNTAX",
  sDescription =    "SQL query syntax invalid or unsupported.");
fAddWindowsDefine("ERROR_INVALID_FIELD",
  sDescription =    "Record field does not exist.");
fAddWindowsDefine("ERROR_DEVICE_REMOVED",
  sDescription =    "The device has been removed.");
fAddWindowsDefine("ERROR_INSTALL_ALREADY_RUNNING",
  sDescription =    "Another installation is already in progress. Complete that installation before proceeding with this install.");
fAddWindowsDefine("ERROR_INSTALL_PACKAGE_OPEN_FAILED",
  sDescription =    "This installation package could not be opened. Verify that the package exists and that you can access it, or contact the application vendor to verify that this is a valid Windows Installer package.");
fAddWindowsDefine("ERROR_INSTALL_PACKAGE_INVALID",
  sDescription =    "This installation package could not be opened. Contact the application vendor to verify that this is a valid Windows Installer package.");
fAddWindowsDefine("ERROR_INSTALL_UI_FAILURE",
  sDescription =    "There was an error starting the Windows Installer service user interface. Contact your support personnel.");
fAddWindowsDefine("ERROR_INSTALL_LOG_FAILURE",
  sDescription =    "Error opening installation log file. Verify that the specified log file location exists and that you can write to it.");
fAddWindowsDefine("ERROR_INSTALL_LANGUAGE_UNSUPPORTED",
  sDescription =    "The language of this installation package is not supported by your system.");
fAddWindowsDefine("ERROR_INSTALL_TRANSFORM_FAILURE",
  sDescription =    "Error applying transforms. Verify that the specified transform paths are valid.");
fAddWindowsDefine("ERROR_INSTALL_PACKAGE_REJECTED",
  sDescription =    "This installation is forbidden by system policy. Contact your system administrator.");
fAddWindowsDefine("ERROR_FUNCTION_NOT_CALLED",
  sDescription =    "Function could not be executed.");
fAddWindowsDefine("ERROR_FUNCTION_FAILED",
  sDescription =    "Function failed during execution.");
fAddWindowsDefine("ERROR_INVALID_TABLE",
  sDescription =    "Invalid or unknown table specified.");
fAddWindowsDefine("ERROR_DATATYPE_MISMATCH",
  sDescription =    "Data supplied is of wrong type.");
fAddWindowsDefine("ERROR_UNSUPPORTED_TYPE",
  sDescription =    "Data of this type is not supported.");
fAddWindowsDefine("ERROR_CREATE_FAILED",
  sDescription =    "The Windows Installer service failed to start. Contact your support personnel.");
fAddWindowsDefine("ERROR_INSTALL_TEMP_UNWRITABLE",
  sDescription =    "The Temp folder is on a drive that is full or is inaccessible. Free up space on the drive or verify that you have write permission on the Temp folder.");
fAddWindowsDefine("ERROR_INSTALL_PLATFORM_UNSUPPORTED",
  sDescription =    "This installation package is not supported by this processor type. Contact your product vendor.");
fAddWindowsDefine("ERROR_INSTALL_NOTUSED",
  sDescription =    "Component not used on this computer.");
fAddWindowsDefine("ERROR_PATCH_PACKAGE_OPEN_FAILED",
  sDescription =    "This update package could not be opened. Verify that the update package exists and that you can access it, or contact the application vendor to verify that this is a valid Windows Installer update package.");
fAddWindowsDefine("ERROR_PATCH_PACKAGE_INVALID",
  sDescription =    "This update package could not be opened. Contact the application vendor to verify that this is a valid Windows Installer update package.");
fAddWindowsDefine("ERROR_PATCH_PACKAGE_UNSUPPORTED",
  sDescription =    "This update package cannot be processed by the Windows Installer service. You must install a Windows service pack that contains a newer version of the Windows Installer service.");
fAddWindowsDefine("ERROR_PRODUCT_VERSION",
  sDescription =    "Another version of this product is already installed. Installation of this version cannot continue. To configure or remove the existing version of this product, use Add/Remove Programs on the Control Panel.");
fAddWindowsDefine("ERROR_INVALID_COMMAND_LINE",
  sDescription =    "Invalid command line argument. Consult the Windows Installer SDK for detailed command line help.");
fAddWindowsDefine("ERROR_INSTALL_REMOTE_DISALLOWED",
  sDescription =    "Only administrators have permission to add, remove, or configure server software during a Terminal services remote session. If you want to install or configure software on the server, contact your network administrator.");
fAddWindowsDefine("ERROR_SUCCESS_REBOOT_INITIATED",
  sDescription =    "The requested operation completed successfully. The system will be restarted so the changes can take effect.");
fAddWindowsDefine("ERROR_PATCH_TARGET_NOT_FOUND",
  sDescription =    "The upgrade cannot be installed by the Windows Installer service because the program to be upgraded may be missing, or the upgrade may update a different version of the program. Verify that the program to be upgraded exists on your computer and that you have the correct upgrade.");
fAddWindowsDefine("ERROR_PATCH_PACKAGE_REJECTED",
  sDescription =    "The update package is not permitted by software restriction policy.");
fAddWindowsDefine("ERROR_INSTALL_TRANSFORM_REJECTED",
  sDescription =    "One or more customizations are not permitted by software restriction policy.");
fAddWindowsDefine("ERROR_INSTALL_REMOTE_PROHIBITED",
  sDescription =    "The Windows Installer does not permit installation from a Remote Desktop Connection.");
fAddWindowsDefine("ERROR_PATCH_REMOVAL_UNSUPPORTED",
  sDescription =    "Uninstallation of the update package is not supported.");
fAddWindowsDefine("ERROR_UNKNOWN_PATCH",
  sDescription =    "The update is not applied to this product.");
fAddWindowsDefine("ERROR_PATCH_NO_SEQUENCE",
  sDescription =    "No valid sequence could be found for the set of updates.");
fAddWindowsDefine("ERROR_PATCH_REMOVAL_DISALLOWED",
  sDescription =    "Update removal was disallowed by policy.");
fAddWindowsDefine("ERROR_INVALID_PATCH_XML",
  sDescription =    "The XML update data is invalid.");
fAddWindowsDefine("ERROR_PATCH_MANAGED_ADVERTISED_PRODUCT",
  sDescription =    "Windows Installer does not permit updating of managed advertised products. At least one feature of the product must be installed before applying the update.");
fAddWindowsDefine("ERROR_INSTALL_SERVICE_SAFEBOOT",
  sDescription =    "The Windows Installer service is not accessible in Safe Mode. Please try again when your computer is not in Safe Mode or you can use System Restore to return your machine to a previous good state.");
fAddWindowsDefine("ERROR_FAIL_FAST_EXCEPTION",
  sDescription =    "A fail fast exception occurred. Exception handlers will not be invoked and the process will be terminated immediately.");
fAddWindowsDefine("ERROR_INSTALL_REJECTED",
  sDescription =    "The app that you are trying to run is not supported on this version of Windows.");
fAddWindowsDefine("ERROR_DYNAMIC_CODE_BLOCKED",
  sDescription =    "The operation was blocked as the process prohibits dynamic code generation.");
fAddWindowsDefine("ERROR_NOT_SAME_OBJECT",
  sDescription =    "The objects are not identical.");
fAddWindowsDefine("RPC_S_INVALID_STRING_BINDING",
  sDescription =    "The string binding is invalid.");
fAddWindowsDefine("RPC_S_WRONG_KIND_OF_BINDING",
  sDescription =    "The binding handle is not the correct type.");
fAddWindowsDefine("RPC_S_INVALID_BINDING",
  sDescription =    "The binding handle is invalid.");
fAddWindowsDefine("RPC_S_PROTSEQ_NOT_SUPPORTED",
  sDescription =    "The RPC protocol sequence is not supported.");
fAddWindowsDefine("RPC_S_INVALID_RPC_PROTSEQ",
  sDescription =    "The RPC protocol sequence is invalid.");
fAddWindowsDefine("RPC_S_INVALID_STRING_UUID",
  sDescription =    "The string universal unique identifier (UUID) is invalid.");
fAddWindowsDefine("RPC_S_INVALID_ENDPOINT_FORMAT",
  sDescription =    "The endpoint format is invalid.");
fAddWindowsDefine("RPC_S_INVALID_NET_ADDR",
  sDescription =    "The network address is invalid.");
fAddWindowsDefine("RPC_S_NO_ENDPOINT_FOUND",
  sDescription =    "No endpoint was found.");
fAddWindowsDefine("RPC_S_INVALID_TIMEOUT",
  sDescription =    "The timeout value is invalid.");
fAddWindowsDefine("RPC_S_OBJECT_NOT_FOUND",
  sDescription =    "The object universal unique identifier (UUID) was not found.");
fAddWindowsDefine("RPC_S_ALREADY_REGISTERED",
  sDescription =    "The object universal unique identifier (UUID) has already been registered.");
fAddWindowsDefine("RPC_S_TYPE_ALREADY_REGISTERED",
  sDescription =    "The type universal unique identifier (UUID) has already been registered.");
fAddWindowsDefine("RPC_S_ALREADY_LISTENING",
  sDescription =    "The RPC server is already listening.");
fAddWindowsDefine("RPC_S_NO_PROTSEQS_REGISTERED",
  sDescription =    "No protocol sequences have been registered.");
fAddWindowsDefine("RPC_S_NOT_LISTENING",
  sDescription =    "The RPC server is not listening.");
fAddWindowsDefine("RPC_S_UNKNOWN_MGR_TYPE",
  sDescription =    "The manager type is unknown.");
fAddWindowsDefine("RPC_S_UNKNOWN_IF",
  sDescription =    "The interface is unknown.");
fAddWindowsDefine("RPC_S_NO_BINDINGS",
  sDescription =    "There are no bindings.");
fAddWindowsDefine("RPC_S_NO_PROTSEQS",
  sDescription =    "There are no protocol sequences.");
fAddWindowsDefine("RPC_S_CANT_CREATE_ENDPOINT",
  sDescription =    "The endpoint cannot be created.");
fAddWindowsDefine("RPC_S_OUT_OF_RESOURCES",
  sDescription =    "Not enough resources are available to complete this operation.");
fAddWindowsDefine("RPC_S_SERVER_UNAVAILABLE",
  sDescription =    "The RPC server is unavailable.");
fAddWindowsDefine("RPC_S_SERVER_TOO_BUSY",
  sDescription =    "The RPC server is too busy to complete this operation.");
fAddWindowsDefine("RPC_S_INVALID_NETWORK_OPTIONS",
  sDescription =    "The network options are invalid.");
fAddWindowsDefine("RPC_S_NO_CALL_ACTIVE",
  sDescription =    "There are no remote procedure calls active on this thread.");
fAddWindowsDefine("RPC_S_CALL_FAILED",
  sDescription =    "The remote procedure call failed.");
fAddWindowsDefine("RPC_S_CALL_FAILED_DNE",
  sDescription =    "The remote procedure call failed and did not execute.");
fAddWindowsDefine("RPC_S_PROTOCOL_ERROR",
  sDescription =    "A remote procedure call (RPC) protocol error occurred.");
fAddWindowsDefine("RPC_S_PROXY_ACCESS_DENIED",
  sDescription =    "Access to the HTTP proxy is denied.");
fAddWindowsDefine("RPC_S_UNSUPPORTED_TRANS_SYN",
  sDescription =    "The transfer syntax is not supported by the RPC server.");
fAddWindowsDefine("RPC_S_UNSUPPORTED_TYPE",
  sDescription =    "The universal unique identifier (UUID) type is not supported.");
fAddWindowsDefine("RPC_S_INVALID_TAG",
  sDescription =    "The tag is invalid.");
fAddWindowsDefine("RPC_S_INVALID_BOUND",
  sDescription =    "The array bounds are invalid.");
fAddWindowsDefine("RPC_S_NO_ENTRY_NAME",
  sDescription =    "The binding does not contain an entry name.");
fAddWindowsDefine("RPC_S_INVALID_NAME_SYNTAX",
  sDescription =    "The name syntax is invalid.");
fAddWindowsDefine("RPC_S_UNSUPPORTED_NAME_SYNTAX",
  sDescription =    "The name syntax is not supported.");
fAddWindowsDefine("RPC_S_UUID_NO_ADDRESS",
  sDescription =    "No network address is available to use to construct a universal unique identifier (UUID).");
fAddWindowsDefine("RPC_S_DUPLICATE_ENDPOINT",
  sDescription =    "The endpoint is a duplicate.");
fAddWindowsDefine("RPC_S_UNKNOWN_AUTHN_TYPE",
  sDescription =    "The authentication type is unknown.");
fAddWindowsDefine("RPC_S_MAX_CALLS_TOO_SMALL",
  sDescription =    "The maximum number of calls is too small.");
fAddWindowsDefine("RPC_S_STRING_TOO_LONG",
  sDescription =    "The string is too long.");
fAddWindowsDefine("RPC_S_PROTSEQ_NOT_FOUND",
  sDescription =    "The RPC protocol sequence was not found.");
fAddWindowsDefine("RPC_S_PROCNUM_OUT_OF_RANGE",
  sDescription =    "The procedure number is out of range.");
fAddWindowsDefine("RPC_S_BINDING_HAS_NO_AUTH",
  sDescription =    "The binding does not contain any authentication information.");
fAddWindowsDefine("RPC_S_UNKNOWN_AUTHN_SERVICE",
  sDescription =    "The authentication service is unknown.");
fAddWindowsDefine("RPC_S_UNKNOWN_AUTHN_LEVEL",
  sDescription =    "The authentication level is unknown.");
fAddWindowsDefine("RPC_S_INVALID_AUTH_IDENTITY",
  sDescription =    "The security context is invalid.");
fAddWindowsDefine("RPC_S_UNKNOWN_AUTHZ_SERVICE",
  sDescription =    "The authorization service is unknown.");
fAddWindowsDefine("EPT_S_INVALID_ENTRY",
  sDescription =    "The entry is invalid.");
fAddWindowsDefine("EPT_S_CANT_PERFORM_OP",
  sDescription =    "The server endpoint cannot perform the operation.");
fAddWindowsDefine("EPT_S_NOT_REGISTERED",
  sDescription =    "There are no more endpoints available from the endpoint mapper.");
fAddWindowsDefine("RPC_S_NOTHING_TO_EXPORT",
  sDescription =    "No interfaces have been exported.");
fAddWindowsDefine("RPC_S_INCOMPLETE_NAME",
  sDescription =    "The entry name is incomplete.");
fAddWindowsDefine("RPC_S_INVALID_VERS_OPTION",
  sDescription =    "The version option is invalid.");
fAddWindowsDefine("RPC_S_NO_MORE_MEMBERS",
  sDescription =    "There are no more members.");
fAddWindowsDefine("RPC_S_NOT_ALL_OBJS_UNEXPORTED",
  sDescription =    "There is nothing to unexport.");
fAddWindowsDefine("RPC_S_INTERFACE_NOT_FOUND",
  sDescription =    "The interface was not found.");
fAddWindowsDefine("RPC_S_ENTRY_ALREADY_EXISTS",
  sDescription =    "The entry already exists.");
fAddWindowsDefine("RPC_S_ENTRY_NOT_FOUND",
  sDescription =    "The entry is not found.");
fAddWindowsDefine("RPC_S_NAME_SERVICE_UNAVAILABLE",
  sDescription =    "The name service is unavailable.");
fAddWindowsDefine("RPC_S_INVALID_NAF_ID",
  sDescription =    "The network address family is invalid.");
fAddWindowsDefine("RPC_S_CANNOT_SUPPORT",
  sDescription =    "The requested operation is not supported.");
fAddWindowsDefine("RPC_S_NO_CONTEXT_AVAILABLE",
  sDescription =    "No security context is available to allow impersonation.");
fAddWindowsDefine("RPC_S_INTERNAL_ERROR",
  sDescription =    "An internal error occurred in a remote procedure call (RPC).");
fAddWindowsDefine("RPC_S_ZERO_DIVIDE",
  sDescription =    "The RPC server attempted an integer division by zero.");
fAddWindowsDefine("RPC_S_ADDRESS_ERROR",
  sDescription =    "An addressing error occurred in the RPC server.");
fAddWindowsDefine("RPC_S_FP_DIV_ZERO",
  sDescription =    "A floating-point operation at the RPC server caused a division by zero.");
fAddWindowsDefine("RPC_S_FP_UNDERFLOW",
  sDescription =    "A floating-point underflow occurred at the RPC server.");
fAddWindowsDefine("RPC_S_FP_OVERFLOW",
  sDescription =    "A floating-point overflow occurred at the RPC server.");
fAddWindowsDefine("RPC_X_NO_MORE_ENTRIES",
  sDescription =    "The list of RPC servers available for the binding of auto handles has been exhausted.");
fAddWindowsDefine("RPC_X_SS_CHAR_TRANS_OPEN_FAIL",
  sDescription =    "Unable to open the character translation table file.");
fAddWindowsDefine("RPC_X_SS_CHAR_TRANS_SHORT_FILE",
  sDescription =    "The file containing the character translation table has fewer than 512 bytes.");
fAddWindowsDefine("RPC_X_SS_IN_NULL_CONTEXT",
  sDescription =    "A null context handle was passed from the client to the host during a remote procedure call.");
fAddWindowsDefine("RPC_X_SS_CONTEXT_DAMAGED",
  sDescription =    "The context handle changed during a remote procedure call.");
fAddWindowsDefine("RPC_X_SS_HANDLES_MISMATCH",
  sDescription =    "The binding handles passed to a remote procedure call do not match.");
fAddWindowsDefine("RPC_X_SS_CANNOT_GET_CALL_HANDLE",
  sDescription =    "The stub is unable to get the remote procedure call handle.");
fAddWindowsDefine("RPC_X_NULL_REF_POINTER",
  sDescription =    "A null reference pointer was passed to the stub.");
fAddWindowsDefine("RPC_X_ENUM_VALUE_OUT_OF_RANGE",
  sDescription =    "The enumeration value is out of range.");
fAddWindowsDefine("RPC_X_BYTE_COUNT_TOO_SMALL",
  sDescription =    "The byte count is too small.");
fAddWindowsDefine("RPC_X_BAD_STUB_DATA",
  sDescription =    "The stub received bad data.");
fAddWindowsDefine("ERROR_INVALID_USER_BUFFER",
  sDescription =    "The supplied user buffer is not valid for the requested operation.");
fAddWindowsDefine("ERROR_UNRECOGNIZED_MEDIA",
  sDescription =    "The disk media is not recognized. It may not be formatted.");
fAddWindowsDefine("ERROR_NO_TRUST_LSA_SECRET",
  sDescription =    "The workstation does not have a trust secret.");
fAddWindowsDefine("ERROR_NO_TRUST_SAM_ACCOUNT",
  sDescription =    "The security database on the server does not have a computer account for this workstation trust relationship.");
fAddWindowsDefine("ERROR_TRUSTED_DOMAIN_FAILURE",
  sDescription =    "The trust relationship between the primary domain and the trusted domain failed.");
fAddWindowsDefine("ERROR_TRUSTED_RELATIONSHIP_FAILURE",
  sDescription =    "The trust relationship between this workstation and the primary domain failed.");
fAddWindowsDefine("ERROR_TRUST_FAILURE",
  sDescription =    "The network logon failed.");
fAddWindowsDefine("RPC_S_CALL_IN_PROGRESS",
  sDescription =    "A remote procedure call is already in progress for this thread.");
fAddWindowsDefine("ERROR_NETLOGON_NOT_STARTED",
  sDescription =    "An attempt was made to logon, but the network logon service was not started.");
fAddWindowsDefine("ERROR_ACCOUNT_EXPIRED",
  sDescription =    "The user's account has expired.");
fAddWindowsDefine("ERROR_REDIRECTOR_HAS_OPEN_HANDLES",
  sDescription =    "The redirector is in use and cannot be unloaded.");
fAddWindowsDefine("ERROR_PRINTER_DRIVER_ALREADY_INSTALLED",
  sDescription =    "The specified printer driver is already installed.");
fAddWindowsDefine("ERROR_UNKNOWN_PORT",
  sDescription =    "The specified port is unknown.");
fAddWindowsDefine("ERROR_UNKNOWN_PRINTER_DRIVER",
  sDescription =    "The printer driver is unknown.");
fAddWindowsDefine("ERROR_UNKNOWN_PRINTPROCESSOR",
  sDescription =    "The print processor is unknown.");
fAddWindowsDefine("ERROR_INVALID_SEPARATOR_FILE",
  sDescription =    "The specified separator file is invalid.");
fAddWindowsDefine("ERROR_INVALID_PRIORITY",
  sDescription =    "The specified priority is invalid.");
fAddWindowsDefine("ERROR_INVALID_PRINTER_NAME",
  sDescription =    "The printer name is invalid.");
fAddWindowsDefine("ERROR_PRINTER_ALREADY_EXISTS",
  sDescription =    "The printer already exists.");
fAddWindowsDefine("ERROR_INVALID_PRINTER_COMMAND",
  sDescription =    "The printer command is invalid.");
fAddWindowsDefine("ERROR_INVALID_DATATYPE",
  sDescription =    "The specified datatype is invalid.");
fAddWindowsDefine("ERROR_INVALID_ENVIRONMENT",
  sDescription =    "The environment specified is invalid.");
fAddWindowsDefine("RPC_S_NO_MORE_BINDINGS",
  sDescription =    "There are no more bindings.");
fAddWindowsDefine("ERROR_NOLOGON_INTERDOMAIN_TRUST_ACCOUNT",
  sDescription =    "The account used is an interdomain trust account. Use your global user account or local user account to access this server.");
fAddWindowsDefine("ERROR_NOLOGON_WORKSTATION_TRUST_ACCOUNT",
  sDescription =    "The account used is a computer account. Use your global user account or local user account to access this server.");
fAddWindowsDefine("ERROR_NOLOGON_SERVER_TRUST_ACCOUNT",
  sDescription =    "The account used is a server trust account. Use your global user account or local user account to access this server.");
fAddWindowsDefine("ERROR_DOMAIN_TRUST_INCONSISTENT",
  sDescription =    "The name or security ID (SID) of the domain specified is inconsistent with the trust information for that domain.");
fAddWindowsDefine("ERROR_SERVER_HAS_OPEN_HANDLES",
  sDescription =    "The server is in use and cannot be unloaded.");
fAddWindowsDefine("ERROR_RESOURCE_DATA_NOT_FOUND",
  sDescription =    "The specified image file did not contain a resource section.");
fAddWindowsDefine("ERROR_RESOURCE_TYPE_NOT_FOUND",
  sDescription =    "The specified resource type cannot be found in the image file.");
fAddWindowsDefine("ERROR_RESOURCE_NAME_NOT_FOUND",
  sDescription =    "The specified resource name cannot be found in the image file.");
fAddWindowsDefine("ERROR_RESOURCE_LANG_NOT_FOUND",
  sDescription =    "The specified resource language ID cannot be found in the image file.");
fAddWindowsDefine("ERROR_NOT_ENOUGH_QUOTA",
  sDescription =    "Not enough quota is available to process this command.");
fAddWindowsDefine("RPC_S_NO_INTERFACES",
  sDescription =    "No interfaces have been registered.");
fAddWindowsDefine("RPC_S_CALL_CANCELLED",
  sDescription =    "The remote procedure call was cancelled.");
fAddWindowsDefine("RPC_S_BINDING_INCOMPLETE",
  sDescription =    "The binding handle does not contain all required information.");
fAddWindowsDefine("RPC_S_COMM_FAILURE",
  sDescription =    "A communications failure occurred during a remote procedure call.");
fAddWindowsDefine("RPC_S_UNSUPPORTED_AUTHN_LEVEL",
  sDescription =    "The requested authentication level is not supported.");
fAddWindowsDefine("RPC_S_NO_PRINC_NAME",
  sDescription =    "No principal name registered.");
fAddWindowsDefine("RPC_S_NOT_RPC_ERROR",
  sDescription =    "The error specified is not a valid Windows RPC error code.");
fAddWindowsDefine("RPC_S_UUID_LOCAL_ONLY",
  sDescription =    "A UUID that is valid only on this computer has been allocated.");
fAddWindowsDefine("RPC_S_SEC_PKG_ERROR",
  sDescription =    "A security package specific error occurred.");
fAddWindowsDefine("RPC_S_NOT_CANCELLED",
  sDescription =    "Thread is not canceled.");
fAddWindowsDefine("RPC_X_INVALID_ES_ACTION",
  sDescription =    "Invalid operation on the encoding/decoding handle.");
fAddWindowsDefine("RPC_X_WRONG_ES_VERSION",
  sDescription =    "Incompatible version of the serializing package.");
fAddWindowsDefine("RPC_X_WRONG_STUB_VERSION",
  sDescription =    "Incompatible version of the RPC stub.");
fAddWindowsDefine("RPC_X_INVALID_PIPE_OBJECT",
  sDescription =    "The RPC pipe object is invalid or corrupted.");
fAddWindowsDefine("RPC_X_WRONG_PIPE_ORDER",
  sDescription =    "An invalid operation was attempted on an RPC pipe object.");
fAddWindowsDefine("RPC_X_WRONG_PIPE_VERSION",
  sDescription =    "Unsupported RPC pipe version.");
fAddWindowsDefine("RPC_S_COOKIE_AUTH_FAILED",
  sDescription =    "HTTP proxy server rejected the connection because the cookie authentication failed.");
fAddWindowsDefine("RPC_S_DO_NOT_DISTURB",
  sDescription =    "The RPC server is suspended, and could not be resumed for this request. The call did not execute.");
fAddWindowsDefine("RPC_S_GROUP_MEMBER_NOT_FOUND",
  sDescription =    "The group member was not found.");
fAddWindowsDefine("EPT_S_CANT_CREATE",
  sDescription =    "The endpoint mapper database entry could not be created.");
fAddWindowsDefine("RPC_S_INVALID_OBJECT",
  sDescription =    "The object universal unique identifier (UUID) is the nil UUID.");
fAddWindowsDefine("ERROR_INVALID_TIME",
  sDescription =    "The specified time is invalid.");
fAddWindowsDefine("ERROR_INVALID_FORM_NAME",
  sDescription =    "The specified form name is invalid.");
fAddWindowsDefine("ERROR_INVALID_FORM_SIZE",
  sDescription =    "The specified form size is invalid.");
fAddWindowsDefine("ERROR_ALREADY_WAITING",
  sDescription =    "The specified printer handle is already being waited on");
fAddWindowsDefine("ERROR_PRINTER_DELETED",
  sDescription =    "The specified printer has been deleted.");
fAddWindowsDefine("ERROR_INVALID_PRINTER_STATE",
  sDescription =    "The state of the printer is invalid.");
fAddWindowsDefine("ERROR_PASSWORD_MUST_CHANGE",
  sDescription =    "The user's password must be changed before signing in.");
fAddWindowsDefine("ERROR_DOMAIN_CONTROLLER_NOT_FOUND",
  sDescription =    "Could not find the domain controller for this domain.");
fAddWindowsDefine("ERROR_ACCOUNT_LOCKED_OUT",
  sDescription =    "The referenced account is currently locked out and may not be logged on to.");
fAddWindowsDefine("OR_INVALID_OXID",
  sDescription =    "The object exporter specified was not found.");
fAddWindowsDefine("OR_INVALID_OID",
  sDescription =    "The object specified was not found.");
fAddWindowsDefine("OR_INVALID_SET",
  sDescription =    "The object resolver set specified was not found.");
fAddWindowsDefine("RPC_S_SEND_INCOMPLETE",
  sDescription =    "Some data remains to be sent in the request buffer.");
fAddWindowsDefine("RPC_S_INVALID_ASYNC_HANDLE",
  sDescription =    "Invalid asynchronous remote procedure call handle.");
fAddWindowsDefine("RPC_S_INVALID_ASYNC_CALL",
  sDescription =    "Invalid asynchronous RPC call handle for this operation.");
fAddWindowsDefine("RPC_X_PIPE_CLOSED",
  sDescription =    "The RPC pipe object has already been closed.");
fAddWindowsDefine("RPC_X_PIPE_DISCIPLINE_ERROR",
  sDescription =    "The RPC call completed before all pipes were processed.");
fAddWindowsDefine("RPC_X_PIPE_EMPTY",
  sDescription =    "No more data is available from the RPC pipe.");
fAddWindowsDefine("ERROR_NO_SITENAME",
  sDescription =    "No site name is available for this machine.");
fAddWindowsDefine("ERROR_CANT_ACCESS_FILE",
  sDescription =    "The file cannot be accessed by the system.");
fAddWindowsDefine("ERROR_CANT_RESOLVE_FILENAME",
  sDescription =    "The name of the file cannot be resolved by the system.");
fAddWindowsDefine("RPC_S_ENTRY_TYPE_MISMATCH",
  sDescription =    "The entry is not of the expected type.");
fAddWindowsDefine("RPC_S_NOT_ALL_OBJS_EXPORTED",
  sDescription =    "Not all object UUIDs could be exported to the specified entry.");
fAddWindowsDefine("RPC_S_INTERFACE_NOT_EXPORTED",
  sDescription =    "Interface could not be exported to the specified entry.");
fAddWindowsDefine("RPC_S_PROFILE_NOT_ADDED",
  sDescription =    "The specified profile entry could not be added.");
fAddWindowsDefine("RPC_S_PRF_ELT_NOT_ADDED",
  sDescription =    "The specified profile element could not be added.");
fAddWindowsDefine("RPC_S_PRF_ELT_NOT_REMOVED",
  sDescription =    "The specified profile element could not be removed.");
fAddWindowsDefine("RPC_S_GRP_ELT_NOT_ADDED",
  sDescription =    "The group element could not be added.");
fAddWindowsDefine("RPC_S_GRP_ELT_NOT_REMOVED",
  sDescription =    "The group element could not be removed.");
fAddWindowsDefine("ERROR_KM_DRIVER_BLOCKED",
  sDescription =    "The printer driver is not compatible with a policy enabled on your computer that blocks NT 4.0 drivers.");
fAddWindowsDefine("ERROR_CONTEXT_EXPIRED",
  sDescription =    "The context has expired and can no longer be used.");
fAddWindowsDefine("ERROR_PER_USER_TRUST_QUOTA_EXCEEDED",
  sDescription =    "The current user's delegated trust creation quota has been exceeded.");
fAddWindowsDefine("ERROR_ALL_USER_TRUST_QUOTA_EXCEEDED",
  sDescription =    "The total delegated trust creation quota has been exceeded.");
fAddWindowsDefine("ERROR_USER_DELETE_TRUST_QUOTA_EXCEEDED",
  sDescription =    "The current user's delegated trust deletion quota has been exceeded.");
fAddWindowsDefine("ERROR_AUTHENTICATION_FIREWALL_FAILED",
  sDescription =    "The computer you are signing into is protected by an authentication firewall. The specified account is not allowed to authenticate to the computer.");
fAddWindowsDefine("ERROR_REMOTE_PRINT_CONNECTIONS_BLOCKED",
  sDescription =    "Remote connections to the Print Spooler are blocked by a policy set on your machine.");
fAddWindowsDefine("ERROR_NTLM_BLOCKED",
  sDescription =    "Authentication failed because NTLM authentication has been disabled.");
fAddWindowsDefine("ERROR_PASSWORD_CHANGE_REQUIRED",
  sDescription =    "Logon Failure: EAS policy requires that the user change their password before this operation can be performed.");
fAddWindowsDefine("ERROR_INVALID_PIXEL_FORMAT",
  sDescription =    "The pixel format is invalid.");
fAddWindowsDefine("ERROR_BAD_DRIVER",
  sDescription =    "The specified driver is invalid.");
fAddWindowsDefine("ERROR_INVALID_WINDOW_STYLE",
  sDescription =    "The window style or class attribute is invalid for this operation.");
fAddWindowsDefine("ERROR_METAFILE_NOT_SUPPORTED",
  sDescription =    "The requested metafile operation is not supported.");
fAddWindowsDefine("ERROR_TRANSFORM_NOT_SUPPORTED",
  sDescription =    "The requested transformation operation is not supported.");
fAddWindowsDefine("ERROR_CLIPPING_NOT_SUPPORTED",
  sDescription =    "The requested clipping operation is not supported.");
fAddWindowsDefine("ERROR_INVALID_CMM",
  sDescription =    "The specified color management module is invalid.");
fAddWindowsDefine("ERROR_INVALID_PROFILE",
  sDescription =    "The specified color profile is invalid.");
fAddWindowsDefine("ERROR_TAG_NOT_FOUND",
  sDescription =    "The specified tag was not found.");
fAddWindowsDefine("ERROR_TAG_NOT_PRESENT",
  sDescription =    "A required tag is not present.");
fAddWindowsDefine("ERROR_DUPLICATE_TAG",
  sDescription =    "The specified tag is already present.");
fAddWindowsDefine("ERROR_PROFILE_NOT_ASSOCIATED_WITH_DEVICE",
  sDescription =    "The specified color profile is not associated with the specified device.");
fAddWindowsDefine("ERROR_PROFILE_NOT_FOUND",
  sDescription =    "The specified color profile was not found.");
fAddWindowsDefine("ERROR_INVALID_COLORSPACE",
  sDescription =    "The specified color space is invalid.");
fAddWindowsDefine("ERROR_ICM_NOT_ENABLED",
  sDescription =    "Image Color Management is not enabled.");
fAddWindowsDefine("ERROR_DELETING_ICM_XFORM",
  sDescription =    "There was an error while deleting the color transform.");
fAddWindowsDefine("ERROR_INVALID_TRANSFORM",
  sDescription =    "The specified color transform is invalid.");
fAddWindowsDefine("ERROR_COLORSPACE_MISMATCH",
  sDescription =    "The specified transform does not match the bitmap's color space.");
fAddWindowsDefine("ERROR_INVALID_COLORINDEX",
  sDescription =    "The specified named color index is not present in the profile.");
fAddWindowsDefine("ERROR_PROFILE_DOES_NOT_MATCH_DEVICE",
  sDescription =    "The specified profile is intended for a device of a different type than the specified device.");
fAddWindowsDefine("ERROR_CONNECTED_OTHER_PASSWORD",
  sDescription =    "The network connection was made successfully, but the user had to be prompted for a password other than the one originally specified.");
fAddWindowsDefine("ERROR_CONNECTED_OTHER_PASSWORD_DEFAULT",
  sDescription =    "The network connection was made successfully using default credentials.");
fAddWindowsDefine("ERROR_BAD_USERNAME",
  sDescription =    "The specified username is invalid.");
fAddWindowsDefine("ERROR_NOT_CONNECTED",
  sDescription =    "This network connection does not exist.");
fAddWindowsDefine("ERROR_OPEN_FILES",
  sDescription =    "This network connection has files open or requests pending.");
fAddWindowsDefine("ERROR_ACTIVE_CONNECTIONS",
  sDescription =    "Active connections still exist.");
fAddWindowsDefine("ERROR_DEVICE_IN_USE",
  sDescription =    "The device is in use by an active process and cannot be disconnected.");
fAddWindowsDefine("ERROR_UNKNOWN_PRINT_MONITOR",
  sDescription =    "The specified print monitor is unknown.");
fAddWindowsDefine("ERROR_PRINTER_DRIVER_IN_USE",
  sDescription =    "The specified printer driver is currently in use.");
fAddWindowsDefine("ERROR_SPOOL_FILE_NOT_FOUND",
  sDescription =    "The spool file was not found.");
fAddWindowsDefine("ERROR_SPL_NO_STARTDOC",
  sDescription =    "A StartDocPrinter call was not issued.");
fAddWindowsDefine("ERROR_SPL_NO_ADDJOB",
  sDescription =    "An AddJob call was not issued.");
fAddWindowsDefine("ERROR_PRINT_PROCESSOR_ALREADY_INSTALLED",
  sDescription =    "The specified print processor has already been installed.");
fAddWindowsDefine("ERROR_PRINT_MONITOR_ALREADY_INSTALLED",
  sDescription =    "The specified print monitor has already been installed.");
fAddWindowsDefine("ERROR_INVALID_PRINT_MONITOR",
  sDescription =    "The specified print monitor does not have the required functions.");
fAddWindowsDefine("ERROR_PRINT_MONITOR_IN_USE",
  sDescription =    "The specified print monitor is currently in use.");
fAddWindowsDefine("ERROR_PRINTER_HAS_JOBS_QUEUED",
  sDescription =    "The requested operation is not allowed when there are jobs queued to the printer.");
fAddWindowsDefine("ERROR_SUCCESS_REBOOT_REQUIRED",
  sDescription =    "The requested operation is successful. Changes will not be effective until the system is rebooted.");
fAddWindowsDefine("ERROR_SUCCESS_RESTART_REQUIRED",
  sDescription =    "The requested operation is successful. Changes will not be effective until the service is restarted.");
fAddWindowsDefine("ERROR_PRINTER_NOT_FOUND",
  sDescription =    "No printers were found.");
fAddWindowsDefine("ERROR_PRINTER_DRIVER_WARNED",
  sDescription =    "The printer driver is known to be unreliable.");
fAddWindowsDefine("ERROR_PRINTER_DRIVER_BLOCKED",
  sDescription =    "The printer driver is known to harm the system.");
fAddWindowsDefine("ERROR_PRINTER_DRIVER_PACKAGE_IN_USE",
  sDescription =    "The specified printer driver package is currently in use.");
fAddWindowsDefine("ERROR_CORE_DRIVER_PACKAGE_NOT_FOUND",
  sDescription =    "Unable to find a core driver package that is required by the printer driver package.");
fAddWindowsDefine("ERROR_FAIL_REBOOT_REQUIRED",
  sDescription =    "The requested operation failed. A system reboot is required to roll back changes made.");
fAddWindowsDefine("ERROR_FAIL_REBOOT_INITIATED",
  sDescription =    "The requested operation failed. A system reboot has been initiated to roll back changes made.");
fAddWindowsDefine("ERROR_PRINTER_DRIVER_DOWNLOAD_NEEDED",
  sDescription =    "The specified printer driver was not found on the system and needs to be downloaded.");
fAddWindowsDefine("ERROR_PRINT_JOB_RESTART_REQUIRED",
  sDescription =    "The requested print job has failed to print. A print system update requires the job to be resubmitted.");
fAddWindowsDefine("ERROR_INVALID_PRINTER_DRIVER_MANIFEST",
  sDescription =    "The printer driver does not contain a valid manifest, or contains too many manifests.");
fAddWindowsDefine("ERROR_PRINTER_NOT_SHAREABLE",
  sDescription =    "The specified printer cannot be shared.");
fAddWindowsDefine("ERROR_REQUEST_PAUSED",
  sDescription =    "The operation was paused.");
fAddWindowsDefine("ERROR_IO_REISSUE_AS_CACHED",
  sDescription =    "Reissue the given operation as a cached IO operation");
fAddWindowsDefine("ERROR_WINS_INTERNAL",
  sDescription =    "WINS encountered an error while processing the command.");
fAddWindowsDefine("ERROR_CAN_NOT_DEL_LOCAL_WINS",
  sDescription =    "The local WINS cannot be deleted.");
fAddWindowsDefine("ERROR_STATIC_INIT",
  sDescription =    "The importation from the file failed.");
fAddWindowsDefine("ERROR_INC_BACKUP",
  sDescription =    "The backup failed. Was a full backup done before?");
fAddWindowsDefine("ERROR_FULL_BACKUP",
  sDescription =    "The backup failed. Check the directory to which you are backing the database.");
fAddWindowsDefine("ERROR_REC_NON_EXISTENT",
  sDescription =    "The name does not exist in the WINS database.");
fAddWindowsDefine("ERROR_RPL_NOT_ALLOWED",
  sDescription =    "Replication with a nonconfigured partner is not allowed.");
fAddWindowsDefine("PEERDIST_ERROR_CONTENTINFO_VERSION_UNSUPPORTED",
  sDescription =    "The version of the supplied content information is not supported.");
fAddWindowsDefine("PEERDIST_ERROR_CANNOT_PARSE_CONTENTINFO",
  sDescription =    "The supplied content information is malformed.");
fAddWindowsDefine("PEERDIST_ERROR_MISSING_DATA",
  sDescription =    "The requested data cannot be found in local or peer caches.");
fAddWindowsDefine("PEERDIST_ERROR_NO_MORE",
  sDescription =    "No more data is available or required.");
fAddWindowsDefine("PEERDIST_ERROR_NOT_INITIALIZED",
  sDescription =    "The supplied object has not been initialized.");
fAddWindowsDefine("PEERDIST_ERROR_ALREADY_INITIALIZED",
  sDescription =    "The supplied object has already been initialized.");
fAddWindowsDefine("PEERDIST_ERROR_SHUTDOWN_IN_PROGRESS",
  sDescription =    "A shutdown operation is already in progress.");
fAddWindowsDefine("PEERDIST_ERROR_INVALIDATED",
  sDescription =    "The supplied object has already been invalidated.");
fAddWindowsDefine("PEERDIST_ERROR_ALREADY_EXISTS",
  sDescription =    "An element already exists and was not replaced.");
fAddWindowsDefine("PEERDIST_ERROR_OPERATION_NOTFOUND",
  sDescription =    "Can not cancel the requested operation as it has already been completed.");
fAddWindowsDefine("PEERDIST_ERROR_ALREADY_COMPLETED",
  sDescription =    "Can not perform the reqested operation because it has already been carried out.");
fAddWindowsDefine("PEERDIST_ERROR_OUT_OF_BOUNDS",
  sDescription =    "An operation accessed data beyond the bounds of valid data.");
fAddWindowsDefine("PEERDIST_ERROR_VERSION_UNSUPPORTED",
  sDescription =    "The requested version is not supported.");
fAddWindowsDefine("PEERDIST_ERROR_INVALID_CONFIGURATION",
  sDescription =    "A configuration value is invalid.");
fAddWindowsDefine("PEERDIST_ERROR_NOT_LICENSED",
  sDescription =    "The SKU is not licensed.");
fAddWindowsDefine("PEERDIST_ERROR_SERVICE_UNAVAILABLE",
  sDescription =    "PeerDist Service is still initializing and will be available shortly.");
fAddWindowsDefine("PEERDIST_ERROR_TRUST_FAILURE",
  sDescription =    "Communication with one or more computers will be temporarily blocked due to recent errors.");
fAddWindowsDefine("ERROR_DHCP_ADDRESS_CONFLICT",
  sDescription =    "The DHCP client has obtained an IP address that is already in use on the network. The local interface will be disabled until the DHCP client can obtain a new address.");
fAddWindowsDefine("ERROR_WMI_GUID_NOT_FOUND",
  sDescription =    "The GUID passed was not recognized as valid by a WMI data provider.");
fAddWindowsDefine("ERROR_WMI_INSTANCE_NOT_FOUND",
  sDescription =    "The instance name passed was not recognized as valid by a WMI data provider.");
fAddWindowsDefine("ERROR_WMI_ITEMID_NOT_FOUND",
  sDescription =    "The data item ID passed was not recognized as valid by a WMI data provider.");
fAddWindowsDefine("ERROR_WMI_TRY_AGAIN",
  sDescription =    "The WMI request could not be completed and should be retried.");
fAddWindowsDefine("ERROR_WMI_DP_NOT_FOUND",
  sDescription =    "The WMI data provider could not be located.");
fAddWindowsDefine("ERROR_WMI_UNRESOLVED_INSTANCE_REF",
  sDescription =    "The WMI data provider references an instance set that has not been registered.");
fAddWindowsDefine("ERROR_WMI_ALREADY_ENABLED",
  sDescription =    "The WMI data block or event notification has already been enabled.");
fAddWindowsDefine("ERROR_WMI_GUID_DISCONNECTED",
  sDescription =    "The WMI data block is no longer available.");
fAddWindowsDefine("ERROR_WMI_SERVER_UNAVAILABLE",
  sDescription =    "The WMI data service is not available.");
fAddWindowsDefine("ERROR_WMI_DP_FAILED",
  sDescription =    "The WMI data provider failed to carry out the request.");
fAddWindowsDefine("ERROR_WMI_INVALID_MOF",
  sDescription =    "The WMI MOF information is not valid.");
fAddWindowsDefine("ERROR_WMI_INVALID_REGINFO",
  sDescription =    "The WMI registration information is not valid.");
fAddWindowsDefine("ERROR_WMI_ALREADY_DISABLED",
  sDescription =    "The WMI data block or event notification has already been disabled.");
fAddWindowsDefine("ERROR_WMI_READ_ONLY",
  sDescription =    "The WMI data item or data block is read only.");
fAddWindowsDefine("ERROR_WMI_SET_FAILURE",
  sDescription =    "The WMI data item or data block could not be changed.");
fAddWindowsDefine("ERROR_NOT_APPCONTAINER",
  sDescription =    "This operation is only valid in the context of an app container.");
fAddWindowsDefine("ERROR_APPCONTAINER_REQUIRED",
  sDescription =    "This application can only run in the context of an app container.");
fAddWindowsDefine("ERROR_NOT_SUPPORTED_IN_APPCONTAINER",
  sDescription =    "This functionality is not supported in the context of an app container.");
fAddWindowsDefine("ERROR_INVALID_PACKAGE_SID_LENGTH",
  sDescription =    "The length of the SID supplied is not a valid length for app container SIDs.");
fAddWindowsDefine("ERROR_INVALID_MEDIA",
  sDescription =    "The media identifier does not represent a valid medium.");
fAddWindowsDefine("ERROR_INVALID_LIBRARY",
  sDescription =    "The library identifier does not represent a valid library.");
fAddWindowsDefine("ERROR_INVALID_MEDIA_POOL",
  sDescription =    "The media pool identifier does not represent a valid media pool.");
fAddWindowsDefine("ERROR_DRIVE_MEDIA_MISMATCH",
  sDescription =    "The drive and medium are not compatible or exist in different libraries.");
fAddWindowsDefine("ERROR_MEDIA_OFFLINE",
  sDescription =    "The medium currently exists in an offline library and must be online to perform this operation.");
fAddWindowsDefine("ERROR_LIBRARY_OFFLINE",
  sDescription =    "The operation cannot be performed on an offline library.");
fAddWindowsDefine("ERROR_EMPTY",
  sDescription =    "The library, drive, or media pool is empty.");
fAddWindowsDefine("ERROR_NOT_EMPTY",
  sDescription =    "The library, drive, or media pool must be empty to perform this operation.");
fAddWindowsDefine("ERROR_MEDIA_UNAVAILABLE",
  sDescription =    "No media is currently available in this media pool or library.");
fAddWindowsDefine("ERROR_RESOURCE_DISABLED",
  sDescription =    "A resource required for this operation is disabled.");
fAddWindowsDefine("ERROR_INVALID_CLEANER",
  sDescription =    "The media identifier does not represent a valid cleaner.");
fAddWindowsDefine("ERROR_UNABLE_TO_CLEAN",
  sDescription =    "The drive cannot be cleaned or does not support cleaning.");
fAddWindowsDefine("ERROR_OBJECT_NOT_FOUND",
  sDescription =    "The object identifier does not represent a valid object.");
fAddWindowsDefine("ERROR_DATABASE_FAILURE",
  sDescription =    "Unable to read from or write to the database.");
fAddWindowsDefine("ERROR_DATABASE_FULL",
  sDescription =    "The database is full.");
fAddWindowsDefine("ERROR_MEDIA_INCOMPATIBLE",
  sDescription =    "The medium is not compatible with the device or media pool.");
fAddWindowsDefine("ERROR_RESOURCE_NOT_PRESENT",
  sDescription =    "The resource required for this operation does not exist.");
fAddWindowsDefine("ERROR_INVALID_OPERATION",
  sDescription =    "The operation identifier is not valid.");
fAddWindowsDefine("ERROR_MEDIA_NOT_AVAILABLE",
  sDescription =    "The media is not mounted or ready for use.");
fAddWindowsDefine("ERROR_DEVICE_NOT_AVAILABLE",
  sDescription =    "The device is not ready for use.");
fAddWindowsDefine("ERROR_REQUEST_REFUSED",
  sDescription =    "The operator or administrator has refused the request.");
fAddWindowsDefine("ERROR_INVALID_DRIVE_OBJECT",
  sDescription =    "The drive identifier does not represent a valid drive.");
fAddWindowsDefine("ERROR_LIBRARY_FULL",
  sDescription =    "Library is full. No slot is available for use.");
fAddWindowsDefine("ERROR_MEDIUM_NOT_ACCESSIBLE",
  sDescription =    "The transport cannot access the medium.");
fAddWindowsDefine("ERROR_UNABLE_TO_LOAD_MEDIUM",
  sDescription =    "Unable to load the medium into the drive.");
fAddWindowsDefine("ERROR_UNABLE_TO_INVENTORY_DRIVE",
  sDescription =    "Unable to retrieve the drive status.");
fAddWindowsDefine("ERROR_UNABLE_TO_INVENTORY_SLOT",
  sDescription =    "Unable to retrieve the slot status.");
fAddWindowsDefine("ERROR_UNABLE_TO_INVENTORY_TRANSPORT",
  sDescription =    "Unable to retrieve status about the transport.");
fAddWindowsDefine("ERROR_TRANSPORT_FULL",
  sDescription =    "Cannot use the transport because it is already in use.");
fAddWindowsDefine("ERROR_CONTROLLING_IEPORT",
  sDescription =    "Unable to open or close the inject/eject port.");
fAddWindowsDefine("ERROR_UNABLE_TO_EJECT_MOUNTED_MEDIA",
  sDescription =    "Unable to eject the medium because it is in a drive.");
fAddWindowsDefine("ERROR_CLEANER_SLOT_SET",
  sDescription =    "A cleaner slot is already reserved.");
fAddWindowsDefine("ERROR_CLEANER_SLOT_NOT_SET",
  sDescription =    "A cleaner slot is not reserved.");
fAddWindowsDefine("ERROR_CLEANER_CARTRIDGE_SPENT",
  sDescription =    "The cleaner cartridge has performed the maximum number of drive cleanings.");
fAddWindowsDefine("ERROR_UNEXPECTED_OMID",
  sDescription =    "Unexpected on-medium identifier.");
fAddWindowsDefine("ERROR_CANT_DELETE_LAST_ITEM",
  sDescription =    "The last remaining item in this group or resource cannot be deleted.");
fAddWindowsDefine("ERROR_MESSAGE_EXCEEDS_MAX_SIZE",
  sDescription =    "The message provided exceeds the maximum size allowed for this parameter.");
fAddWindowsDefine("ERROR_VOLUME_CONTAINS_SYS_FILES",
  sDescription =    "The volume contains system or paging files.");
fAddWindowsDefine("ERROR_INDIGENOUS_TYPE",
  sDescription =    "The media type cannot be removed from this library since at least one drive in the library reports it can support this media type.");
fAddWindowsDefine("ERROR_NO_SUPPORTING_DRIVES",
  sDescription =    "This offline media cannot be mounted on this system since no enabled drives are present which can be used.");
fAddWindowsDefine("ERROR_CLEANER_CARTRIDGE_INSTALLED",
  sDescription =    "A cleaner cartridge is present in the tape library.");
fAddWindowsDefine("ERROR_IEPORT_FULL",
  sDescription =    "Cannot use the inject/eject port because it is not empty.");
fAddWindowsDefine("ERROR_FILE_OFFLINE",
  sDescription =    "This file is currently not available for use on this computer.");
fAddWindowsDefine("ERROR_REMOTE_STORAGE_NOT_ACTIVE",
  sDescription =    "The remote storage service is not operational at this time.");
fAddWindowsDefine("ERROR_REMOTE_STORAGE_MEDIA_ERROR",
  sDescription =    "The remote storage service encountered a media error.");
fAddWindowsDefine("ERROR_NOT_A_REPARSE_POINT",
  sDescription =    "The file or directory is not a reparse point.");
fAddWindowsDefine("ERROR_REPARSE_ATTRIBUTE_CONFLICT",
  sDescription =    "The reparse point attribute cannot be set because it conflicts with an existing attribute.");
fAddWindowsDefine("ERROR_INVALID_REPARSE_DATA",
  sDescription =    "The data present in the reparse point buffer is invalid.");
fAddWindowsDefine("ERROR_REPARSE_TAG_INVALID",
  sDescription =    "The tag present in the reparse point buffer is invalid.");
fAddWindowsDefine("ERROR_REPARSE_TAG_MISMATCH",
  sDescription =    "There is a mismatch between the tag specified in the request and the tag present in the reparse point.");
fAddWindowsDefine("ERROR_APP_DATA_NOT_FOUND",
  sDescription =    "Fast Cache data not found.");
fAddWindowsDefine("ERROR_APP_DATA_EXPIRED",
  sDescription =    "Fast Cache data expired.");
fAddWindowsDefine("ERROR_APP_DATA_CORRUPT",
  sDescription =    "Fast Cache data corrupt.");
fAddWindowsDefine("ERROR_APP_DATA_LIMIT_EXCEEDED",
  sDescription =    "Fast Cache data has exceeded its max size and cannot be updated.");
fAddWindowsDefine("ERROR_APP_DATA_REBOOT_REQUIRED",
  sDescription =    "Fast Cache has been ReArmed and requires a reboot until it can be updated.");
fAddWindowsDefine("ERROR_SECUREBOOT_ROLLBACK_DETECTED",
  sDescription =    "Secure Boot detected that rollback of protected data has been attempted.");
fAddWindowsDefine("ERROR_SECUREBOOT_POLICY_VIOLATION",
  sDescription =    "The value is protected by Secure Boot policy and cannot be modified or deleted.");
fAddWindowsDefine("ERROR_SECUREBOOT_INVALID_POLICY",
  sDescription =    "The Secure Boot policy is invalid.");
fAddWindowsDefine("ERROR_SECUREBOOT_POLICY_PUBLISHER_NOT_FOUND",
  sDescription =    "A new Secure Boot policy did not contain the current publisher on its update list.");
fAddWindowsDefine("ERROR_SECUREBOOT_POLICY_NOT_SIGNED",
  sDescription =    "The Secure Boot policy is either not signed or is signed by a non-trusted signer.");
fAddWindowsDefine("ERROR_SECUREBOOT_NOT_ENABLED",
  sDescription =    "Secure Boot is not enabled on this machine.");
fAddWindowsDefine("ERROR_SECUREBOOT_FILE_REPLACED",
  sDescription =    "Secure Boot requires that certain files and drivers are not replaced by other files or drivers.");
fAddWindowsDefine("ERROR_OFFLOAD_READ_FLT_NOT_SUPPORTED",
  sDescription =    "The copy offload read operation is not supported by a filter.");
fAddWindowsDefine("ERROR_OFFLOAD_WRITE_FLT_NOT_SUPPORTED",
  sDescription =    "The copy offload write operation is not supported by a filter.");
fAddWindowsDefine("ERROR_OFFLOAD_READ_FILE_NOT_SUPPORTED",
  sDescription =    "The copy offload read operation is not supported for the file.");
fAddWindowsDefine("ERROR_OFFLOAD_WRITE_FILE_NOT_SUPPORTED",
  sDescription =    "The copy offload write operation is not supported for the file.");
fAddWindowsDefine("ERROR_VOLUME_NOT_SIS_ENABLED",
  sDescription =    "Single Instance Storage is not available on this volume.");
fAddWindowsDefine("ERROR_SYSTEM_INTEGRITY_ROLLBACK_DETECTED",
  sDescription =    "System Integrity detected that policy rollback has been attempted.");
fAddWindowsDefine("ERROR_SYSTEM_INTEGRITY_POLICY_VIOLATION",
  sDescription =    "The System Integrity policy has been violated.");
fAddWindowsDefine("ERROR_SYSTEM_INTEGRITY_INVALID_POLICY",
  sDescription =    "The System Integrity policy is invalid.");
fAddWindowsDefine("ERROR_SYSTEM_INTEGRITY_POLICY_NOT_SIGNED",
  sDescription =    "The System Integrity policy is either not signed or is signed by a non-trusted signer.");
fAddWindowsDefine("ERROR_VSM_NOT_INITIALIZED",
  sDescription =    "Virtual Secure Mode (VSM) is not initialized. The hypervisor or VSM may not be present or enabled.");
fAddWindowsDefine("ERROR_VSM_DMA_PROTECTION_NOT_IN_USE",
  sDescription =    "The hypervisor is not protecting DMA because an IOMMU is not present or not enabled in the BIOS.");
fAddWindowsDefine("ERROR_DEPENDENT_RESOURCE_EXISTS",
  sDescription =    "The operation cannot be completed because other resources are dependent on this resource.");
fAddWindowsDefine("ERROR_DEPENDENCY_NOT_FOUND",
  sDescription =    "The cluster resource dependency cannot be found.");
fAddWindowsDefine("ERROR_DEPENDENCY_ALREADY_EXISTS",
  sDescription =    "The cluster resource cannot be made dependent on the specified resource because it is already dependent.");
fAddWindowsDefine("ERROR_RESOURCE_NOT_ONLINE",
  sDescription =    "The cluster resource is not online.");
fAddWindowsDefine("ERROR_HOST_NODE_NOT_AVAILABLE",
  sDescription =    "A cluster node is not available for this operation.");
fAddWindowsDefine("ERROR_RESOURCE_NOT_AVAILABLE",
  sDescription =    "The cluster resource is not available.");
fAddWindowsDefine("ERROR_RESOURCE_NOT_FOUND",
  sDescription =    "The cluster resource could not be found.");
fAddWindowsDefine("ERROR_SHUTDOWN_CLUSTER",
  sDescription =    "The cluster is being shut down.");
fAddWindowsDefine("ERROR_CANT_EVICT_ACTIVE_NODE",
  sDescription =    "A cluster node cannot be evicted from the cluster unless the node is down or it is the last node.");
fAddWindowsDefine("ERROR_OBJECT_ALREADY_EXISTS",
  sDescription =    "The object already exists.");
fAddWindowsDefine("ERROR_OBJECT_IN_LIST",
  sDescription =    "The object is already in the list.");
fAddWindowsDefine("ERROR_GROUP_NOT_AVAILABLE",
  sDescription =    "The cluster group is not available for any new requests.");
fAddWindowsDefine("ERROR_GROUP_NOT_FOUND",
  sDescription =    "The cluster group could not be found.");
fAddWindowsDefine("ERROR_GROUP_NOT_ONLINE",
  sDescription =    "The operation could not be completed because the cluster group is not online.");
fAddWindowsDefine("ERROR_HOST_NODE_NOT_RESOURCE_OWNER",
  sDescription =    "The operation failed because either the specified cluster node is not the owner of the resource, or the node is not a possible owner of the resource.");
fAddWindowsDefine("ERROR_HOST_NODE_NOT_GROUP_OWNER",
  sDescription =    "The operation failed because either the specified cluster node is not the owner of the group, or the node is not a possible owner of the group.");
fAddWindowsDefine("ERROR_RESMON_CREATE_FAILED",
  sDescription =    "The cluster resource could not be created in the specified resource monitor.");
fAddWindowsDefine("ERROR_RESMON_ONLINE_FAILED",
  sDescription =    "The cluster resource could not be brought online by the resource monitor.");
fAddWindowsDefine("ERROR_RESOURCE_ONLINE",
  sDescription =    "The operation could not be completed because the cluster resource is online.");
fAddWindowsDefine("ERROR_QUORUM_RESOURCE",
  sDescription =    "The cluster resource could not be deleted or brought offline because it is the quorum resource.");
fAddWindowsDefine("ERROR_NOT_QUORUM_CAPABLE",
  sDescription =    "The cluster could not make the specified resource a quorum resource because it is not capable of being a quorum resource.");
fAddWindowsDefine("ERROR_CLUSTER_SHUTTING_DOWN",
  sDescription =    "The cluster software is shutting down.");
fAddWindowsDefine("ERROR_INVALID_STATE",
  sDescription =    "The group or resource is not in the correct state to perform the requested operation.");
fAddWindowsDefine("ERROR_RESOURCE_PROPERTIES_STORED",
  sDescription =    "The properties were stored but not all changes will take effect until the next time the resource is brought online.");
fAddWindowsDefine("ERROR_NOT_QUORUM_CLASS",
  sDescription =    "The cluster could not make the specified resource a quorum resource because it does not belong to a shared storage class.");
fAddWindowsDefine("ERROR_CORE_RESOURCE",
  sDescription =    "The cluster resource could not be deleted since it is a core resource.");
fAddWindowsDefine("ERROR_QUORUM_RESOURCE_ONLINE_FAILED",
  sDescription =    "The quorum resource failed to come online.");
fAddWindowsDefine("ERROR_QUORUMLOG_OPEN_FAILED",
  sDescription =    "The quorum log could not be created or mounted successfully.");
fAddWindowsDefine("ERROR_CLUSTERLOG_CORRUPT",
  sDescription =    "The cluster log is corrupt.");
fAddWindowsDefine("ERROR_CLUSTERLOG_RECORD_EXCEEDS_MAXSIZE",
  sDescription =    "The record could not be written to the cluster log since it exceeds the maximum size.");
fAddWindowsDefine("ERROR_CLUSTERLOG_EXCEEDS_MAXSIZE",
  sDescription =    "The cluster log exceeds its maximum size.");
fAddWindowsDefine("ERROR_CLUSTERLOG_CHKPOINT_NOT_FOUND",
  sDescription =    "No checkpoint record was found in the cluster log.");
fAddWindowsDefine("ERROR_CLUSTERLOG_NOT_ENOUGH_SPACE",
  sDescription =    "The minimum required disk space needed for logging is not available.");
fAddWindowsDefine("ERROR_QUORUM_OWNER_ALIVE",
  sDescription =    "The cluster node failed to take control of the quorum resource because the resource is owned by another active node.");
fAddWindowsDefine("ERROR_NETWORK_NOT_AVAILABLE",
  sDescription =    "A cluster network is not available for this operation.");
fAddWindowsDefine("ERROR_NODE_NOT_AVAILABLE",
  sDescription =    "A cluster node is not available for this operation.");
fAddWindowsDefine("ERROR_ALL_NODES_NOT_AVAILABLE",
  sDescription =    "All cluster nodes must be running to perform this operation.");
fAddWindowsDefine("ERROR_RESOURCE_FAILED",
  sDescription =    "A cluster resource failed.");
fAddWindowsDefine("ERROR_CLUSTER_INVALID_NODE",
  sDescription =    "The cluster node is not valid.");
fAddWindowsDefine("ERROR_CLUSTER_NODE_EXISTS",
  sDescription =    "The cluster node already exists.");
fAddWindowsDefine("ERROR_CLUSTER_JOIN_IN_PROGRESS",
  sDescription =    "A node is in the process of joining the cluster.");
fAddWindowsDefine("ERROR_CLUSTER_NODE_NOT_FOUND",
  sDescription =    "The cluster node was not found.");
fAddWindowsDefine("ERROR_CLUSTER_LOCAL_NODE_NOT_FOUND",
  sDescription =    "The cluster local node information was not found.");
fAddWindowsDefine("ERROR_CLUSTER_NETWORK_EXISTS",
  sDescription =    "The cluster network already exists.");
fAddWindowsDefine("ERROR_CLUSTER_NETWORK_NOT_FOUND",
  sDescription =    "The cluster network was not found.");
fAddWindowsDefine("ERROR_CLUSTER_NETINTERFACE_EXISTS",
  sDescription =    "The cluster network interface already exists.");
fAddWindowsDefine("ERROR_CLUSTER_NETINTERFACE_NOT_FOUND",
  sDescription =    "The cluster network interface was not found.");
fAddWindowsDefine("ERROR_CLUSTER_INVALID_REQUEST",
  sDescription =    "The cluster request is not valid for this object.");
fAddWindowsDefine("ERROR_CLUSTER_INVALID_NETWORK_PROVIDER",
  sDescription =    "The cluster network provider is not valid.");
fAddWindowsDefine("ERROR_CLUSTER_NODE_DOWN",
  sDescription =    "The cluster node is down.");
fAddWindowsDefine("ERROR_CLUSTER_NODE_UNREACHABLE",
  sDescription =    "The cluster node is not reachable.");
fAddWindowsDefine("ERROR_CLUSTER_NODE_NOT_MEMBER",
  sDescription =    "The cluster node is not a member of the cluster.");
fAddWindowsDefine("ERROR_CLUSTER_JOIN_NOT_IN_PROGRESS",
  sDescription =    "A cluster join operation is not in progress.");
fAddWindowsDefine("ERROR_CLUSTER_INVALID_NETWORK",
  sDescription =    "The cluster network is not valid.");
fAddWindowsDefine("ERROR_CLUSTER_NODE_UP",
  sDescription =    "The cluster node is up.");
fAddWindowsDefine("ERROR_CLUSTER_IPADDR_IN_USE",
  sDescription =    "The cluster IP address is already in use.");
fAddWindowsDefine("ERROR_CLUSTER_NODE_NOT_PAUSED",
  sDescription =    "The cluster node is not paused.");
fAddWindowsDefine("ERROR_CLUSTER_NO_SECURITY_CONTEXT",
  sDescription =    "No cluster security context is available.");
fAddWindowsDefine("ERROR_CLUSTER_NETWORK_NOT_INTERNAL",
  sDescription =    "The cluster network is not configured for internal cluster communication.");
fAddWindowsDefine("ERROR_CLUSTER_NODE_ALREADY_UP",
  sDescription =    "The cluster node is already up.");
fAddWindowsDefine("ERROR_CLUSTER_NODE_ALREADY_DOWN",
  sDescription =    "The cluster node is already down.");
fAddWindowsDefine("ERROR_CLUSTER_NETWORK_ALREADY_ONLINE",
  sDescription =    "The cluster network is already online.");
fAddWindowsDefine("ERROR_CLUSTER_NETWORK_ALREADY_OFFLINE",
  sDescription =    "The cluster network is already offline.");
fAddWindowsDefine("ERROR_CLUSTER_NODE_ALREADY_MEMBER",
  sDescription =    "The cluster node is already a member of the cluster.");
fAddWindowsDefine("ERROR_CLUSTER_LAST_INTERNAL_NETWORK",
  sDescription =    "The cluster network is the only one configured for internal cluster communication between two or more active cluster nodes. The internal communication capability cannot be removed from the network.");
fAddWindowsDefine("ERROR_CLUSTER_NETWORK_HAS_DEPENDENTS",
  sDescription =    "One or more cluster resources depend on the network to provide service to clients. The client access capability cannot be removed from the network.");
fAddWindowsDefine("ERROR_INVALID_OPERATION_ON_QUORUM",
  sDescription =    "This operation cannot currently be performed on the cluster group containing the quorum resource.");
fAddWindowsDefine("ERROR_DEPENDENCY_NOT_ALLOWED",
  sDescription =    "The cluster quorum resource is not allowed to have any dependencies.");
fAddWindowsDefine("ERROR_CLUSTER_NODE_PAUSED",
  sDescription =    "The cluster node is paused.");
fAddWindowsDefine("ERROR_NODE_CANT_HOST_RESOURCE",
  sDescription =    "The cluster resource cannot be brought online. The owner node cannot run this resource.");
fAddWindowsDefine("ERROR_CLUSTER_NODE_NOT_READY",
  sDescription =    "The cluster node is not ready to perform the requested operation.");
fAddWindowsDefine("ERROR_CLUSTER_NODE_SHUTTING_DOWN",
  sDescription =    "The cluster node is shutting down.");
fAddWindowsDefine("ERROR_CLUSTER_JOIN_ABORTED",
  sDescription =    "The cluster join operation was aborted.");
fAddWindowsDefine("ERROR_CLUSTER_INCOMPATIBLE_VERSIONS",
  sDescription =    "The node failed to join the cluster because the joining node and other nodes in the cluster have incompatible operating system versions. To get more information about operating system versions of the cluster, run the Validate a Configuration Wizard or the Test-Cluster Windows PowerShell cmdlet.");
fAddWindowsDefine("ERROR_CLUSTER_MAXNUM_OF_RESOURCES_EXCEEDED",
  sDescription =    "This resource cannot be created because the cluster has reached the limit on the number of resources it can monitor.");
fAddWindowsDefine("ERROR_CLUSTER_SYSTEM_CONFIG_CHANGED",
  sDescription =    "The system configuration changed during the cluster join or form operation. The join or form operation was aborted.");
fAddWindowsDefine("ERROR_CLUSTER_RESOURCE_TYPE_NOT_FOUND",
  sDescription =    "The specified resource type was not found.");
fAddWindowsDefine("ERROR_CLUSTER_RESTYPE_NOT_SUPPORTED",
  sDescription =    "The specified node does not support a resource of this type. This may be due to version inconsistencies or due to the absence of the resource DLL on this node.");
fAddWindowsDefine("ERROR_CLUSTER_RESNAME_NOT_FOUND",
  sDescription =    "The specified resource name is not supported by this resource DLL. This may be due to a bad (or changed) name supplied to the resource DLL.");
fAddWindowsDefine("ERROR_CLUSTER_NO_RPC_PACKAGES_REGISTERED",
  sDescription =    "No authentication package could be registered with the RPC server.");
fAddWindowsDefine("ERROR_CLUSTER_OWNER_NOT_IN_PREFLIST",
  sDescription =    "You cannot bring the group online because the owner of the group is not in the preferred list for the group. To change the owner node for the group, move the group.");
fAddWindowsDefine("ERROR_CLUSTER_DATABASE_SEQMISMATCH",
  sDescription =    "The join operation failed because the cluster database sequence number has changed or is incompatible with the locker node. This may happen during a join operation if the cluster database was changing during the join.");
fAddWindowsDefine("ERROR_RESMON_INVALID_STATE",
  sDescription =    "The resource monitor will not allow the fail operation to be performed while the resource is in its current state. This may happen if the resource is in a pending state.");
fAddWindowsDefine("ERROR_CLUSTER_GUM_NOT_LOCKER",
  sDescription =    "A non locker code got a request to reserve the lock for making global updates.");
fAddWindowsDefine("ERROR_QUORUM_DISK_NOT_FOUND",
  sDescription =    "The quorum disk could not be located by the cluster service.");
fAddWindowsDefine("ERROR_DATABASE_BACKUP_CORRUPT",
  sDescription =    "The backed up cluster database is possibly corrupt.");
fAddWindowsDefine("ERROR_CLUSTER_NODE_ALREADY_HAS_DFS_ROOT",
  sDescription =    "A DFS root already exists in this cluster node.");
fAddWindowsDefine("ERROR_RESOURCE_PROPERTY_UNCHANGEABLE",
  sDescription =    "An attempt to modify a resource property failed because it conflicts with another existing property.");
fAddWindowsDefine("ERROR_NO_ADMIN_ACCESS_POINT",
  sDescription =    "This operation is not supported on a cluster without an Administrator Access Point.");
fAddWindowsDefine("ERROR_CLUSTER_MEMBERSHIP_INVALID_STATE",
  sDescription =    "An operation was attempted that is incompatible with the current membership state of the node.");
fAddWindowsDefine("ERROR_CLUSTER_QUORUMLOG_NOT_FOUND",
  sDescription =    "The quorum resource does not contain the quorum log.");
fAddWindowsDefine("ERROR_CLUSTER_MEMBERSHIP_HALT",
  sDescription =    "The membership engine requested shutdown of the cluster service on this node.");
fAddWindowsDefine("ERROR_CLUSTER_INSTANCE_ID_MISMATCH",
  sDescription =    "The join operation failed because the cluster instance ID of the joining node does not match the cluster instance ID of the sponsor node.");
fAddWindowsDefine("ERROR_CLUSTER_NETWORK_NOT_FOUND_FOR_IP",
  sDescription =    "A matching cluster network for the specified IP address could not be found.");
fAddWindowsDefine("ERROR_CLUSTER_PROPERTY_DATA_TYPE_MISMATCH",
  sDescription =    "The actual data type of the property did not match the expected data type of the property.");
fAddWindowsDefine("ERROR_CLUSTER_EVICT_WITHOUT_CLEANUP",
  sDescription =    "The cluster node was evicted from the cluster successfully, but the node was not cleaned up. To determine what cleanup steps failed and how to recover, see the Failover Clustering application event log using Event Viewer.");
fAddWindowsDefine("ERROR_CLUSTER_PARAMETER_MISMATCH",
  sDescription =    "Two or more parameter values specified for a resource's properties are in conflict.");
fAddWindowsDefine("ERROR_NODE_CANNOT_BE_CLUSTERED",
  sDescription =    "This computer cannot be made a member of a cluster.");
fAddWindowsDefine("ERROR_CLUSTER_WRONG_OS_VERSION",
  sDescription =    "This computer cannot be made a member of a cluster because it does not have the correct version of Windows installed.");
fAddWindowsDefine("ERROR_CLUSTER_CANT_CREATE_DUP_CLUSTER_NAME",
  sDescription =    "A cluster cannot be created with the specified cluster name because that cluster name is already in use. Specify a different name for the cluster.");
fAddWindowsDefine("ERROR_CLUSCFG_ALREADY_COMMITTED",
  sDescription =    "The cluster configuration action has already been committed.");
fAddWindowsDefine("ERROR_CLUSCFG_ROLLBACK_FAILED",
  sDescription =    "The cluster configuration action could not be rolled back.");
fAddWindowsDefine("ERROR_CLUSCFG_SYSTEM_DISK_DRIVE_LETTER_CONFLICT",
  sDescription =    "The drive letter assigned to a system disk on one node conflicted with the drive letter assigned to a disk on another node.");
fAddWindowsDefine("ERROR_CLUSTER_OLD_VERSION",
  sDescription =    "One or more nodes in the cluster are running a version of Windows that does not support this operation.");
fAddWindowsDefine("ERROR_CLUSTER_MISMATCHED_COMPUTER_ACCT_NAME",
  sDescription =    "The name of the corresponding computer account doesn't match the Network Name for this resource.");
fAddWindowsDefine("ERROR_CLUSTER_NO_NET_ADAPTERS",
  sDescription =    "No network adapters are available.");
fAddWindowsDefine("ERROR_CLUSTER_POISONED",
  sDescription =    "The cluster node has been poisoned.");
fAddWindowsDefine("ERROR_CLUSTER_GROUP_MOVING",
  sDescription =    "The group is unable to accept the request since it is moving to another node.");
fAddWindowsDefine("ERROR_CLUSTER_RESOURCE_TYPE_BUSY",
  sDescription =    "The resource type cannot accept the request since is too busy performing another operation.");
fAddWindowsDefine("ERROR_RESOURCE_CALL_TIMED_OUT",
  sDescription =    "The call to the cluster resource DLL timed out.");
fAddWindowsDefine("ERROR_INVALID_CLUSTER_IPV6_ADDRESS",
  sDescription =    "The address is not valid for an IPv6 Address resource. A global IPv6 address is required, and it must match a cluster network. Compatibility addresses are not permitted.");
fAddWindowsDefine("ERROR_CLUSTER_INTERNAL_INVALID_FUNCTION",
  sDescription =    "An internal cluster error occurred. A call to an invalid function was attempted.");
fAddWindowsDefine("ERROR_CLUSTER_PARAMETER_OUT_OF_BOUNDS",
  sDescription =    "A parameter value is out of acceptable range.");
fAddWindowsDefine("ERROR_CLUSTER_PARTIAL_SEND",
  sDescription =    "A network error occurred while sending data to another node in the cluster. The number of bytes transmitted was less than required.");
fAddWindowsDefine("ERROR_CLUSTER_REGISTRY_INVALID_FUNCTION",
  sDescription =    "An invalid cluster registry operation was attempted.");
fAddWindowsDefine("ERROR_CLUSTER_INVALID_STRING_TERMINATION",
  sDescription =    "An input string of characters is not properly terminated.");
fAddWindowsDefine("ERROR_CLUSTER_INVALID_STRING_FORMAT",
  sDescription =    "An input string of characters is not in a valid format for the data it represents.");
fAddWindowsDefine("ERROR_CLUSTER_DATABASE_TRANSACTION_IN_PROGRESS",
  sDescription =    "An internal cluster error occurred. A cluster database transaction was attempted while a transaction was already in progress.");
fAddWindowsDefine("ERROR_CLUSTER_DATABASE_TRANSACTION_NOT_IN_PROGRESS",
  sDescription =    "An internal cluster error occurred. There was an attempt to commit a cluster database transaction while no transaction was in progress.");
fAddWindowsDefine("ERROR_CLUSTER_NULL_DATA",
  sDescription =    "An internal cluster error occurred. Data was not properly initialized.");
fAddWindowsDefine("ERROR_CLUSTER_PARTIAL_READ",
  sDescription =    "An error occurred while reading from a stream of data. An unexpected number of bytes was returned.");
fAddWindowsDefine("ERROR_CLUSTER_PARTIAL_WRITE",
  sDescription =    "An error occurred while writing to a stream of data. The required number of bytes could not be written.");
fAddWindowsDefine("ERROR_CLUSTER_CANT_DESERIALIZE_DATA",
  sDescription =    "An error occurred while deserializing a stream of cluster data.");
fAddWindowsDefine("ERROR_DEPENDENT_RESOURCE_PROPERTY_CONFLICT",
  sDescription =    "One or more property values for this resource are in conflict with one or more property values associated with its dependent resource(s).");
fAddWindowsDefine("ERROR_CLUSTER_NO_QUORUM",
  sDescription =    "A quorum of cluster nodes was not present to form a cluster.");
fAddWindowsDefine("ERROR_CLUSTER_INVALID_IPV6_NETWORK",
  sDescription =    "The cluster network is not valid for an IPv6 Address resource, or it does not match the configured address.");
fAddWindowsDefine("ERROR_CLUSTER_INVALID_IPV6_TUNNEL_NETWORK",
  sDescription =    "The cluster network is not valid for an IPv6 Tunnel resource. Check the configuration of the IP Address resource on which the IPv6 Tunnel resource depends.");
fAddWindowsDefine("ERROR_QUORUM_NOT_ALLOWED_IN_THIS_GROUP",
  sDescription =    "Quorum resource cannot reside in the Available Storage group.");
fAddWindowsDefine("ERROR_DEPENDENCY_TREE_TOO_COMPLEX",
  sDescription =    "The dependencies for this resource are nested too deeply.");
fAddWindowsDefine("ERROR_EXCEPTION_IN_RESOURCE_CALL",
  sDescription =    "The call into the resource DLL raised an unhandled exception.");
fAddWindowsDefine("ERROR_CLUSTER_RHS_FAILED_INITIALIZATION",
  sDescription =    "The RHS process failed to initialize.");
fAddWindowsDefine("ERROR_CLUSTER_NOT_INSTALLED",
  sDescription =    "The Failover Clustering feature is not installed on this node.");
fAddWindowsDefine("ERROR_CLUSTER_RESOURCES_MUST_BE_ONLINE_ON_THE_SAME_NODE",
  sDescription =    "The resources must be online on the same node for this operation");
fAddWindowsDefine("ERROR_CLUSTER_MAX_NODES_IN_CLUSTER",
  sDescription =    "A new node can not be added since this cluster is already at its maximum number of nodes.");
fAddWindowsDefine("ERROR_CLUSTER_TOO_MANY_NODES",
  sDescription =    "This cluster can not be created since the specified number of nodes exceeds the maximum allowed limit.");
fAddWindowsDefine("ERROR_CLUSTER_OBJECT_ALREADY_USED",
  sDescription =    "An attempt to use the specified cluster name failed because an enabled computer object with the given name already exists in the domain.");
fAddWindowsDefine("ERROR_NONCORE_GROUPS_FOUND",
  sDescription =    "This cluster cannot be destroyed. It has non-core application groups which must be deleted before the cluster can be destroyed.");
fAddWindowsDefine("ERROR_FILE_SHARE_RESOURCE_CONFLICT",
  sDescription =    "File share associated with file share witness resource cannot be hosted by this cluster or any of its nodes.");
fAddWindowsDefine("ERROR_CLUSTER_EVICT_INVALID_REQUEST",
  sDescription =    "Eviction of this node is invalid at this time. Due to quorum requirements node eviction will result in cluster shutdown. If it is the last node in the cluster, destroy cluster command should be used.");
fAddWindowsDefine("ERROR_CLUSTER_SINGLETON_RESOURCE",
  sDescription =    "Only one instance of this resource type is allowed in the cluster.");
fAddWindowsDefine("ERROR_CLUSTER_GROUP_SINGLETON_RESOURCE",
  sDescription =    "Only one instance of this resource type is allowed per resource group.");
fAddWindowsDefine("ERROR_CLUSTER_RESOURCE_PROVIDER_FAILED",
  sDescription =    "The resource failed to come online due to the failure of one or more provider resources.");
fAddWindowsDefine("ERROR_CLUSTER_RESOURCE_CONFIGURATION_ERROR",
  sDescription =    "The resource has indicated that it cannot come online on any node.");
fAddWindowsDefine("ERROR_CLUSTER_GROUP_BUSY",
  sDescription =    "The current operation cannot be performed on this group at this time.");
fAddWindowsDefine("ERROR_CLUSTER_NOT_SHARED_VOLUME",
  sDescription =    "The directory or file is not located on a cluster shared volume.");
fAddWindowsDefine("ERROR_CLUSTER_INVALID_SECURITY_DESCRIPTOR",
  sDescription =    "The Security Descriptor does not meet the requirements for a cluster.");
fAddWindowsDefine("ERROR_CLUSTER_SHARED_VOLUMES_IN_USE",
  sDescription =    "There is one or more shared volumes resources configured in the cluster. Those resources must be moved to available storage in order for operation to succeed.");
fAddWindowsDefine("ERROR_CLUSTER_USE_SHARED_VOLUMES_API",
  sDescription =    "This group or resource cannot be directly manipulated. Use shared volume APIs to perform desired operation.");
fAddWindowsDefine("ERROR_CLUSTER_BACKUP_IN_PROGRESS",
  sDescription =    "Back up is in progress. Please wait for backup completion before trying this operation again.");
fAddWindowsDefine("ERROR_NON_CSV_PATH",
  sDescription =    "The path does not belong to a cluster shared volume.");
fAddWindowsDefine("ERROR_CSV_VOLUME_NOT_LOCAL",
  sDescription =    "The cluster shared volume is not locally mounted on this node.");
fAddWindowsDefine("ERROR_CLUSTER_WATCHDOG_TERMINATING",
  sDescription =    "The cluster watchdog is terminating.");
fAddWindowsDefine("ERROR_CLUSTER_RESOURCE_VETOED_MOVE_INCOMPATIBLE_NODES",
  sDescription =    "A resource vetoed a move between two nodes because they are incompatible.");
fAddWindowsDefine("ERROR_CLUSTER_INVALID_NODE_WEIGHT",
  sDescription =    "The request is invalid either because node weight cannot be changed while the cluster is in disk-only quorum mode, or because changing the node weight would violate the minimum cluster quorum requirements.");
fAddWindowsDefine("ERROR_CLUSTER_RESOURCE_VETOED_CALL",
  sDescription =    "The resource vetoed the call.");
fAddWindowsDefine("ERROR_RESMON_SYSTEM_RESOURCES_LACKING",
  sDescription =    "Resource could not start or run because it could not reserve sufficient system resources.");
fAddWindowsDefine("ERROR_CLUSTER_RESOURCE_VETOED_MOVE_NOT_ENOUGH_RESOURCES_ON_DESTINATION",
  sDescription =    "A resource vetoed a move between two nodes because the destination currently does not have enough resources to complete the operation.");
fAddWindowsDefine("ERROR_CLUSTER_RESOURCE_VETOED_MOVE_NOT_ENOUGH_RESOURCES_ON_SOURCE",
  sDescription =    "A resource vetoed a move between two nodes because the source currently does not have enough resources to complete the operation.");
fAddWindowsDefine("ERROR_CLUSTER_GROUP_QUEUED",
  sDescription =    "The requested operation can not be completed because the group is queued for an operation.");
fAddWindowsDefine("ERROR_CLUSTER_RESOURCE_LOCKED_STATUS",
  sDescription =    "The requested operation can not be completed because a resource has locked status.");
fAddWindowsDefine("ERROR_CLUSTER_SHARED_VOLUME_FAILOVER_NOT_ALLOWED",
  sDescription =    "The resource cannot move to another node because a cluster shared volume vetoed the operation.");
fAddWindowsDefine("ERROR_CLUSTER_NODE_DRAIN_IN_PROGRESS",
  sDescription =    "A node drain is already in progress.");
fAddWindowsDefine("ERROR_CLUSTER_DISK_NOT_CONNECTED",
  sDescription =    "Clustered storage is not connected to the node.");
fAddWindowsDefine("ERROR_DISK_NOT_CSV_CAPABLE",
  sDescription =    "The disk is not configured in a way to be used with CSV. CSV disks must have at least one partition that is formatted with NTFS or REFS.");
fAddWindowsDefine("ERROR_RESOURCE_NOT_IN_AVAILABLE_STORAGE",
  sDescription =    "The resource must be part of the Available Storage group to complete this action.");
fAddWindowsDefine("ERROR_CLUSTER_SHARED_VOLUME_REDIRECTED",
  sDescription =    "CSVFS failed operation as volume is in redirected mode.");
fAddWindowsDefine("ERROR_CLUSTER_SHARED_VOLUME_NOT_REDIRECTED",
  sDescription =    "CSVFS failed operation as volume is not in redirected mode.");
fAddWindowsDefine("ERROR_CLUSTER_CANNOT_RETURN_PROPERTIES",
  sDescription =    "Cluster properties cannot be returned at this time.");
fAddWindowsDefine("ERROR_CLUSTER_RESOURCE_CONTAINS_UNSUPPORTED_DIFF_AREA_FOR_SHARED_VOLUMES",
  sDescription =    "The clustered disk resource contains software snapshot diff area that are not supported for Cluster Shared Volumes.");
fAddWindowsDefine("ERROR_CLUSTER_RESOURCE_IS_IN_MAINTENANCE_MODE",
  sDescription =    "The operation cannot be completed because the resource is in maintenance mode.");
fAddWindowsDefine("ERROR_CLUSTER_AFFINITY_CONFLICT",
  sDescription =    "The operation cannot be completed because of cluster affinity conflicts");
fAddWindowsDefine("ERROR_CLUSTER_RESOURCE_IS_REPLICA_VIRTUAL_MACHINE",
  sDescription =    "The operation cannot be completed because the resource is a replica virtual machine.");
fAddWindowsDefine("ERROR_CLUSTER_UPGRADE_INCOMPATIBLE_VERSIONS",
  sDescription =    "The Cluster Functional Level could not be increased because not all nodes in the cluster support the updated version.");
fAddWindowsDefine("ERROR_CLUSTER_UPGRADE_FIX_QUORUM_NOT_SUPPORTED",
  sDescription =    "Updating the cluster functional level failed because the cluster is running in fix quorum mode. Start additional nodes which are members of the cluster until the cluster reaches quorum and the cluster will automatically switch out of fix quorum mode, or stop and restart the cluster without the FixQuorum switch. Once the cluster is out of fix quorum mode retry the Update-ClusterFunctionalLevel PowerShell cmdlet to update the cluster functional level.");
fAddWindowsDefine("ERROR_CLUSTER_UPGRADE_RESTART_REQUIRED",
  sDescription =    "The cluster functional level has been successfully updated but not all features are available yet. Restart the cluster by using the Stop-Cluster PowerShell cmdlet followed by the Start-Cluster PowerShell cmdlet and all cluster features will be available.");
fAddWindowsDefine("ERROR_CLUSTER_UPGRADE_IN_PROGRESS",
  sDescription =    "The cluster is currently performing a version upgrade.");
fAddWindowsDefine("ERROR_CLUSTER_UPGRADE_INCOMPLETE",
  sDescription =    "The cluster did not successfully complete the version upgrade.");
fAddWindowsDefine("ERROR_CLUSTER_NODE_IN_GRACE_PERIOD",
  sDescription =    "The cluster node is in grace period.");
fAddWindowsDefine("ERROR_CLUSTER_CSV_IO_PAUSE_TIMEOUT",
  sDescription =    "The operation has failed because CSV volume was not able to recover in time specified on this file object.");
fAddWindowsDefine("ERROR_NODE_NOT_ACTIVE_CLUSTER_MEMBER",
  sDescription =    "The operation failed because the requested node is not currently part of active cluster membership.");
fAddWindowsDefine("ERROR_CLUSTER_RESOURCE_NOT_MONITORED",
  sDescription =    "The operation failed because the requested cluster resource is currently unmonitored.");
fAddWindowsDefine("ERROR_CLUSTER_RESOURCE_DOES_NOT_SUPPORT_UNMONITORED",
  sDescription =    "The operation failed because a resource does not support running in an unmonitored state.");
fAddWindowsDefine("ERROR_CLUSTER_RESOURCE_IS_REPLICATED",
  sDescription =    "The operation cannot be completed because a resource participates in replication.");
fAddWindowsDefine("ERROR_CLUSTER_NODE_ISOLATED",
  sDescription =    "The operation failed because the requested cluster node has been isolated");
fAddWindowsDefine("ERROR_CLUSTER_NODE_QUARANTINED",
  sDescription =    "The operation failed because the requested cluster node has been quarantined");
fAddWindowsDefine("ERROR_CLUSTER_DATABASE_UPDATE_CONDITION_FAILED",
  sDescription =    "The operation failed because the specified database update condition was not met");
fAddWindowsDefine("ERROR_CLUSTER_SPACE_DEGRADED",
  sDescription =    "A clustered space is in a degraded condition and the requested action cannot be completed at this time.");
fAddWindowsDefine("ERROR_CLUSTER_TOKEN_DELEGATION_NOT_SUPPORTED",
  sDescription =    "The operation failed because token delegation for this control is not supported.");
fAddWindowsDefine("ERROR_ENCRYPTION_FAILED",
  sDescription =    "The specified file could not be encrypted.");
fAddWindowsDefine("ERROR_DECRYPTION_FAILED",
  sDescription =    "The specified file could not be decrypted.");
fAddWindowsDefine("ERROR_FILE_ENCRYPTED",
  sDescription =    "The specified file is encrypted and the user does not have the ability to decrypt it.");
fAddWindowsDefine("ERROR_NO_RECOVERY_POLICY",
  sDescription =    "There is no valid encryption recovery policy configured for this system.");
fAddWindowsDefine("ERROR_NO_EFS",
  sDescription =    "The required encryption driver is not loaded for this system.");
fAddWindowsDefine("ERROR_WRONG_EFS",
  sDescription =    "The file was encrypted with a different encryption driver than is currently loaded.");
fAddWindowsDefine("ERROR_NO_USER_KEYS",
  sDescription =    "There are no EFS keys defined for the user.");
fAddWindowsDefine("ERROR_FILE_NOT_ENCRYPTED",
  sDescription =    "The specified file is not encrypted.");
fAddWindowsDefine("ERROR_NOT_EXPORT_FORMAT",
  sDescription =    "The specified file is not in the defined EFS export format.");
fAddWindowsDefine("ERROR_FILE_READ_ONLY",
  sDescription =    "The specified file is read only.");
fAddWindowsDefine("ERROR_DIR_EFS_DISALLOWED",
  sDescription =    "The directory has been disabled for encryption.");
fAddWindowsDefine("ERROR_EFS_SERVER_NOT_TRUSTED",
  sDescription =    "The server is not trusted for remote encryption operation.");
fAddWindowsDefine("ERROR_BAD_RECOVERY_POLICY",
  sDescription =    "Recovery policy configured for this system contains invalid recovery certificate.");
fAddWindowsDefine("ERROR_EFS_ALG_BLOB_TOO_BIG",
  sDescription =    "The encryption algorithm used on the source file needs a bigger key buffer than the one on the destination file.");
fAddWindowsDefine("ERROR_VOLUME_NOT_SUPPORT_EFS",
  sDescription =    "The disk partition does not support file encryption.");
fAddWindowsDefine("ERROR_EFS_DISABLED",
  sDescription =    "This machine is disabled for file encryption.");
fAddWindowsDefine("ERROR_EFS_VERSION_NOT_SUPPORT",
  sDescription =    "A newer system is required to decrypt this encrypted file.");
fAddWindowsDefine("ERROR_CS_ENCRYPTION_INVALID_SERVER_RESPONSE",
  sDescription =    "The remote server sent an invalid response for a file being opened with Client Side Encryption.");
fAddWindowsDefine("ERROR_CS_ENCRYPTION_UNSUPPORTED_SERVER",
  sDescription =    "Client Side Encryption is not supported by the remote server even though it claims to support it.");
fAddWindowsDefine("ERROR_CS_ENCRYPTION_EXISTING_ENCRYPTED_FILE",
  sDescription =    "File is encrypted and should be opened in Client Side Encryption mode.");
fAddWindowsDefine("ERROR_CS_ENCRYPTION_NEW_ENCRYPTED_FILE",
  sDescription =    "A new encrypted file is being created and a $EFS needs to be provided.");
fAddWindowsDefine("ERROR_CS_ENCRYPTION_FILE_NOT_CSE",
  sDescription =    "The SMB client requested a CSE FSCTL on a non-CSE file.");
fAddWindowsDefine("ERROR_ENCRYPTION_POLICY_DENIES_OPERATION",
  sDescription =    "The requested operation was blocked by policy. For more information, contact your system administrator.");
fAddWindowsDefine("ERROR_NO_BROWSER_SERVERS_FOUND",
  sDescription =    "The list of servers for this workgroup is not currently available");
fAddWindowsDefine("SCHED_E_SERVICE_NOT_LOCALSYSTEM",
  sDescription =    "The Task Scheduler service must be configured to run in the System account to function properly. Individual tasks may be configured to run in other accounts.");
fAddWindowsDefine("ERROR_LOG_SECTOR_INVALID",
  sDescription =    "Log service encountered an invalid log sector.");
fAddWindowsDefine("ERROR_LOG_SECTOR_PARITY_INVALID",
  sDescription =    "Log service encountered a log sector with invalid block parity.");
fAddWindowsDefine("ERROR_LOG_SECTOR_REMAPPED",
  sDescription =    "Log service encountered a remapped log sector.");
fAddWindowsDefine("ERROR_LOG_BLOCK_INCOMPLETE",
  sDescription =    "Log service encountered a partial or incomplete log block.");
fAddWindowsDefine("ERROR_LOG_INVALID_RANGE",
  sDescription =    "Log service encountered an attempt access data outside the active log range.");
fAddWindowsDefine("ERROR_LOG_BLOCKS_EXHAUSTED",
  sDescription =    "Log service user marshalling buffers are exhausted.");
fAddWindowsDefine("ERROR_LOG_READ_CONTEXT_INVALID",
  sDescription =    "Log service encountered an attempt read from a marshalling area with an invalid read context.");
fAddWindowsDefine("ERROR_LOG_RESTART_INVALID",
  sDescription =    "Log service encountered an invalid log restart area.");
fAddWindowsDefine("ERROR_LOG_BLOCK_VERSION",
  sDescription =    "Log service encountered an invalid log block version.");
fAddWindowsDefine("ERROR_LOG_BLOCK_INVALID",
  sDescription =    "Log service encountered an invalid log block.");
fAddWindowsDefine("ERROR_LOG_READ_MODE_INVALID",
  sDescription =    "Log service encountered an attempt to read the log with an invalid read mode.");
fAddWindowsDefine("ERROR_LOG_NO_RESTART",
  sDescription =    "Log service encountered a log stream with no restart area.");
fAddWindowsDefine("ERROR_LOG_METADATA_CORRUPT",
  sDescription =    "Log service encountered a corrupted metadata file.");
fAddWindowsDefine("ERROR_LOG_METADATA_INVALID",
  sDescription =    "Log service encountered a metadata file that could not be created by the log file system.");
fAddWindowsDefine("ERROR_LOG_METADATA_INCONSISTENT",
  sDescription =    "Log service encountered a metadata file with inconsistent data.");
fAddWindowsDefine("ERROR_LOG_RESERVATION_INVALID",
  sDescription =    "Log service encountered an attempt to erroneous allocate or dispose reservation space.");
fAddWindowsDefine("ERROR_LOG_CANT_DELETE",
  sDescription =    "Log service cannot delete log file or file system container.");
fAddWindowsDefine("ERROR_LOG_CONTAINER_LIMIT_EXCEEDED",
  sDescription =    "Log service has reached the maximum allowable containers allocated to a log file.");
fAddWindowsDefine("ERROR_LOG_START_OF_LOG",
  sDescription =    "Log service has attempted to read or write backward past the start of the log.");
fAddWindowsDefine("ERROR_LOG_POLICY_ALREADY_INSTALLED",
  sDescription =    "Log policy could not be installed because a policy of the same type is already present.");
fAddWindowsDefine("ERROR_LOG_POLICY_NOT_INSTALLED",
  sDescription =    "Log policy in question was not installed at the time of the request.");
fAddWindowsDefine("ERROR_LOG_POLICY_INVALID",
  sDescription =    "The installed set of policies on the log is invalid.");
fAddWindowsDefine("ERROR_LOG_POLICY_CONFLICT",
  sDescription =    "A policy on the log in question prevented the operation from completing.");
fAddWindowsDefine("ERROR_LOG_PINNED_ARCHIVE_TAIL",
  sDescription =    "Log space cannot be reclaimed because the log is pinned by the archive tail.");
fAddWindowsDefine("ERROR_LOG_RECORD_NONEXISTENT",
  sDescription =    "Log record is not a record in the log file.");
fAddWindowsDefine("ERROR_LOG_RECORDS_RESERVED_INVALID",
  sDescription =    "Number of reserved log records or the adjustment of the number of reserved log records is invalid.");
fAddWindowsDefine("ERROR_LOG_SPACE_RESERVED_INVALID",
  sDescription =    "Reserved log space or the adjustment of the log space is invalid.");
fAddWindowsDefine("ERROR_LOG_TAIL_INVALID",
  sDescription =    "An new or existing archive tail or base of the active log is invalid.");
fAddWindowsDefine("ERROR_LOG_FULL",
  sDescription =    "Log space is exhausted.");
fAddWindowsDefine("ERROR_COULD_NOT_RESIZE_LOG",
  sDescription =    "The log could not be set to the requested size.");
fAddWindowsDefine("ERROR_LOG_MULTIPLEXED",
  sDescription =    "Log is multiplexed, no direct writes to the physical log is allowed.");
fAddWindowsDefine("ERROR_LOG_DEDICATED",
  sDescription =    "The operation failed because the log is a dedicated log.");
fAddWindowsDefine("ERROR_LOG_ARCHIVE_NOT_IN_PROGRESS",
  sDescription =    "The operation requires an archive context.");
fAddWindowsDefine("ERROR_LOG_ARCHIVE_IN_PROGRESS",
  sDescription =    "Log archival is in progress.");
fAddWindowsDefine("ERROR_LOG_EPHEMERAL",
  sDescription =    "The operation requires a non-ephemeral log, but the log is ephemeral.");
fAddWindowsDefine("ERROR_LOG_NOT_ENOUGH_CONTAINERS",
  sDescription =    "The log must have at least two containers before it can be read from or written to.");
fAddWindowsDefine("ERROR_LOG_CLIENT_ALREADY_REGISTERED",
  sDescription =    "A log client has already registered on the stream.");
fAddWindowsDefine("ERROR_LOG_CLIENT_NOT_REGISTERED",
  sDescription =    "A log client has not been registered on the stream.");
fAddWindowsDefine("ERROR_LOG_FULL_HANDLER_IN_PROGRESS",
  sDescription =    "A request has already been made to handle the log full condition.");
fAddWindowsDefine("ERROR_LOG_CONTAINER_READ_FAILED",
  sDescription =    "Log service encountered an error when attempting to read from a log container.");
fAddWindowsDefine("ERROR_LOG_CONTAINER_WRITE_FAILED",
  sDescription =    "Log service encountered an error when attempting to write to a log container.");
fAddWindowsDefine("ERROR_LOG_CONTAINER_OPEN_FAILED",
  sDescription =    "Log service encountered an error when attempting open a log container.");
fAddWindowsDefine("ERROR_LOG_CONTAINER_STATE_INVALID",
  sDescription =    "Log service encountered an invalid container state when attempting a requested action.");
fAddWindowsDefine("ERROR_LOG_STATE_INVALID",
  sDescription =    "Log service is not in the correct state to perform a requested action.");
fAddWindowsDefine("ERROR_LOG_PINNED",
  sDescription =    "Log space cannot be reclaimed because the log is pinned.");
fAddWindowsDefine("ERROR_LOG_METADATA_FLUSH_FAILED",
  sDescription =    "Log metadata flush failed.");
fAddWindowsDefine("ERROR_LOG_INCONSISTENT_SECURITY",
  sDescription =    "Security on the log and its containers is inconsistent.");
fAddWindowsDefine("ERROR_LOG_APPENDED_FLUSH_FAILED",
  sDescription =    "Records were appended to the log or reservation changes were made, but the log could not be flushed.");
fAddWindowsDefine("ERROR_LOG_PINNED_RESERVATION",
  sDescription =    "The log is pinned due to reservation consuming most of the log space. Free some reserved records to make space available.");
fAddWindowsDefine("ERROR_INVALID_TRANSACTION",
  sDescription =    "The transaction handle associated with this operation is not valid.");
fAddWindowsDefine("ERROR_TRANSACTION_NOT_ACTIVE",
  sDescription =    "The requested operation was made in the context of a transaction that is no longer active.");
fAddWindowsDefine("ERROR_TRANSACTION_REQUEST_NOT_VALID",
  sDescription =    "The requested operation is not valid on the Transaction object in its current state.");
fAddWindowsDefine("ERROR_TRANSACTION_NOT_REQUESTED",
  sDescription =    "The caller has called a response API, but the response is not expected because the TM did not issue the corresponding request to the caller.");
fAddWindowsDefine("ERROR_TRANSACTION_ALREADY_ABORTED",
  sDescription =    "It is too late to perform the requested operation, since the Transaction has already been aborted.");
fAddWindowsDefine("ERROR_TRANSACTION_ALREADY_COMMITTED",
  sDescription =    "It is too late to perform the requested operation, since the Transaction has already been committed.");
fAddWindowsDefine("ERROR_TM_INITIALIZATION_FAILED",
  sDescription =    "The Transaction Manager was unable to be successfully initialized. Transacted operations are not supported.");
fAddWindowsDefine("ERROR_RESOURCEMANAGER_READ_ONLY",
  sDescription =    "The specified ResourceManager made no changes or updates to the resource under this transaction.");
fAddWindowsDefine("ERROR_TRANSACTION_NOT_JOINED",
  sDescription =    "The resource manager has attempted to prepare a transaction that it has not successfully joined.");
fAddWindowsDefine("ERROR_TRANSACTION_SUPERIOR_EXISTS",
  sDescription =    "The Transaction object already has a superior enlistment, and the caller attempted an operation that would have created a new superior. Only a single superior enlistment is allow.");
fAddWindowsDefine("ERROR_CRM_PROTOCOL_ALREADY_EXISTS",
  sDescription =    "The RM tried to register a protocol that already exists.");
fAddWindowsDefine("ERROR_TRANSACTION_PROPAGATION_FAILED",
  sDescription =    "The attempt to propagate the Transaction failed.");
fAddWindowsDefine("ERROR_CRM_PROTOCOL_NOT_FOUND",
  sDescription =    "The requested propagation protocol was not registered as a CRM.");
fAddWindowsDefine("ERROR_TRANSACTION_INVALID_MARSHALL_BUFFER",
  sDescription =    "The buffer passed in to PushTransaction or PullTransaction is not in a valid format.");
fAddWindowsDefine("ERROR_CURRENT_TRANSACTION_NOT_VALID",
  sDescription =    "The current transaction context associated with the thread is not a valid handle to a transaction object.");
fAddWindowsDefine("ERROR_TRANSACTION_NOT_FOUND",
  sDescription =    "The specified Transaction object could not be opened, because it was not found.");
fAddWindowsDefine("ERROR_RESOURCEMANAGER_NOT_FOUND",
  sDescription =    "The specified ResourceManager object could not be opened, because it was not found.");
fAddWindowsDefine("ERROR_ENLISTMENT_NOT_FOUND",
  sDescription =    "The specified Enlistment object could not be opened, because it was not found.");
fAddWindowsDefine("ERROR_TRANSACTIONMANAGER_NOT_FOUND",
  sDescription =    "The specified TransactionManager object could not be opened, because it was not found.");
fAddWindowsDefine("ERROR_TRANSACTIONMANAGER_NOT_ONLINE",
  sDescription =    "The object specified could not be created or opened, because its associated TransactionManager is not online. The TransactionManager must be brought fully Online by calling RecoverTransactionManager to recover to the end of its LogFile before objects in its Transaction or ResourceManager namespaces can be opened. In addition, errors in writing records to its LogFile can cause a TransactionManager to go offline.");
fAddWindowsDefine("ERROR_TRANSACTIONMANAGER_RECOVERY_NAME_COLLISION",
  sDescription =    "The specified TransactionManager was unable to create the objects contained in its logfile in the Ob namespace. Therefore, the TransactionManager was unable to recover.");
fAddWindowsDefine("ERROR_TRANSACTION_NOT_ROOT",
  sDescription =    "The call to create a superior Enlistment on this Transaction object could not be completed, because the Transaction object specified for the enlistment is a subordinate branch of the Transaction. Only the root of the Transaction can be enlisted on as a superior.");
fAddWindowsDefine("ERROR_TRANSACTION_OBJECT_EXPIRED",
  sDescription =    "Because the associated transaction manager or resource manager has been closed, the handle is no longer valid.");
fAddWindowsDefine("ERROR_TRANSACTION_RESPONSE_NOT_ENLISTED",
  sDescription =    "The specified operation could not be performed on this Superior enlistment, because the enlistment was not created with the corresponding completion response in the NotificationMask.");
fAddWindowsDefine("ERROR_TRANSACTION_RECORD_TOO_LONG",
  sDescription =    "The specified operation could not be performed, because the record that would be logged was too long. This can occur because of two conditions: either there are too many Enlistments on this Transaction, or the combined RecoveryInformation being logged on behalf of those Enlistments is too long.");
fAddWindowsDefine("ERROR_IMPLICIT_TRANSACTION_NOT_SUPPORTED",
  sDescription =    "Implicit transaction are not supported.");
fAddWindowsDefine("ERROR_TRANSACTION_INTEGRITY_VIOLATED",
  sDescription =    "The kernel transaction manager had to abort or forget the transaction because it blocked forward progress.");
fAddWindowsDefine("ERROR_TRANSACTIONMANAGER_IDENTITY_MISMATCH",
  sDescription =    "The TransactionManager identity that was supplied did not match the one recorded in the TransactionManager's log file.");
fAddWindowsDefine("ERROR_RM_CANNOT_BE_FROZEN_FOR_SNAPSHOT",
  sDescription =    "This snapshot operation cannot continue because a transactional resource manager cannot be frozen in its current state. Please try again.");
fAddWindowsDefine("ERROR_TRANSACTION_MUST_WRITETHROUGH",
  sDescription =    "The transaction cannot be enlisted on with the specified EnlistmentMask, because the transaction has already completed the PrePrepare phase. In order to ensure correctness, the ResourceManager must switch to a write-through mode and cease caching data within this transaction. Enlisting for only subsequent transaction phases may still succeed.");
fAddWindowsDefine("ERROR_TRANSACTION_NO_SUPERIOR",
  sDescription =    "The transaction does not have a superior enlistment.");
fAddWindowsDefine("ERROR_HEURISTIC_DAMAGE_POSSIBLE",
  sDescription =    "The attempt to commit the Transaction completed, but it is possible that some portion of the transaction tree did not commit successfully due to heuristics. Therefore it is possible that some data modified in the transaction may not have committed, resulting in transactional inconsistency. If possible, check the consistency of the associated data.");
fAddWindowsDefine("ERROR_TRANSACTIONAL_CONFLICT",
  sDescription =    "The function attempted to use a name that is reserved for use by another transaction.");
fAddWindowsDefine("ERROR_RM_NOT_ACTIVE",
  sDescription =    "Transaction support within the specified resource manager is not started or was shut down due to an error.");
fAddWindowsDefine("ERROR_RM_METADATA_CORRUPT",
  sDescription =    "The metadata of the RM has been corrupted. The RM will not function.");
fAddWindowsDefine("ERROR_DIRECTORY_NOT_RM",
  sDescription =    "The specified directory does not contain a resource manager.");
fAddWindowsDefine("ERROR_TRANSACTIONS_UNSUPPORTED_REMOTE",
  sDescription =    "The remote server or share does not support transacted file operations.");
fAddWindowsDefine("ERROR_LOG_RESIZE_INVALID_SIZE",
  sDescription =    "The requested log size is invalid.");
fAddWindowsDefine("ERROR_OBJECT_NO_LONGER_EXISTS",
  sDescription =    "The object (file, stream, link) corresponding to the handle has been deleted by a Transaction Savepoint Rollback.");
fAddWindowsDefine("ERROR_STREAM_MINIVERSION_NOT_FOUND",
  sDescription =    "The specified file miniversion was not found for this transacted file open.");
fAddWindowsDefine("ERROR_STREAM_MINIVERSION_NOT_VALID",
  sDescription =    "The specified file miniversion was found but has been invalidated. Most likely cause is a transaction savepoint rollback.");
fAddWindowsDefine("ERROR_MINIVERSION_INACCESSIBLE_FROM_SPECIFIED_TRANSACTION",
  sDescription =    "A miniversion may only be opened in the context of the transaction that created it.");
fAddWindowsDefine("ERROR_CANT_OPEN_MINIVERSION_WITH_MODIFY_INTENT",
  sDescription =    "It is not possible to open a miniversion with modify access.");
fAddWindowsDefine("ERROR_CANT_CREATE_MORE_STREAM_MINIVERSIONS",
  sDescription =    "It is not possible to create any more miniversions for this stream.");
fAddWindowsDefine("ERROR_REMOTE_FILE_VERSION_MISMATCH",
  sDescription =    "The remote server sent mismatching version number or Fid for a file opened with transactions.");
fAddWindowsDefine("ERROR_HANDLE_NO_LONGER_VALID",
  sDescription =    "The handle has been invalidated by a transaction. The most likely cause is the presence of memory mapping on a file or an open handle when the transaction ended or rolled back to savepoint.");
fAddWindowsDefine("ERROR_NO_TXF_METADATA",
  sDescription =    "There is no transaction metadata on the file.");
fAddWindowsDefine("ERROR_LOG_CORRUPTION_DETECTED",
  sDescription =    "The log data is corrupt.");
fAddWindowsDefine("ERROR_CANT_RECOVER_WITH_HANDLE_OPEN",
  sDescription =    "The file can't be recovered because there is a handle still open on it.");
fAddWindowsDefine("ERROR_RM_DISCONNECTED",
  sDescription =    "The transaction outcome is unavailable because the resource manager responsible for it has disconnected.");
fAddWindowsDefine("ERROR_ENLISTMENT_NOT_SUPERIOR",
  sDescription =    "The request was rejected because the enlistment in question is not a superior enlistment.");
fAddWindowsDefine("ERROR_RECOVERY_NOT_NEEDED",
  sDescription =    "The transactional resource manager is already consistent. Recovery is not needed.");
fAddWindowsDefine("ERROR_RM_ALREADY_STARTED",
  sDescription =    "The transactional resource manager has already been started.");
fAddWindowsDefine("ERROR_FILE_IDENTITY_NOT_PERSISTENT",
  sDescription =    "The file cannot be opened transactionally, because its identity depends on the outcome of an unresolved transaction.");
fAddWindowsDefine("ERROR_CANT_BREAK_TRANSACTIONAL_DEPENDENCY",
  sDescription =    "The operation cannot be performed because another transaction is depending on the fact that this property will not change.");
fAddWindowsDefine("ERROR_CANT_CROSS_RM_BOUNDARY",
  sDescription =    "The operation would involve a single file with two transactional resource managers and is therefore not allowed.");
fAddWindowsDefine("ERROR_TXF_DIR_NOT_EMPTY",
  sDescription =    "The $Txf directory must be empty for this operation to succeed.");
fAddWindowsDefine("ERROR_INDOUBT_TRANSACTIONS_EXIST",
  sDescription =    "The operation would leave a transactional resource manager in an inconsistent state and is therefore not allowed.");
fAddWindowsDefine("ERROR_TM_VOLATILE",
  sDescription =    "The operation could not be completed because the transaction manager does not have a log.");
fAddWindowsDefine("ERROR_ROLLBACK_TIMER_EXPIRED",
  sDescription =    "A rollback could not be scheduled because a previously scheduled rollback has already executed or been queued for execution.");
fAddWindowsDefine("ERROR_TXF_ATTRIBUTE_CORRUPT",
  sDescription =    "The transactional metadata attribute on the file or directory is corrupt and unreadable.");
fAddWindowsDefine("ERROR_EFS_NOT_ALLOWED_IN_TRANSACTION",
  sDescription =    "The encryption operation could not be completed because a transaction is active.");
fAddWindowsDefine("ERROR_TRANSACTIONAL_OPEN_NOT_ALLOWED",
  sDescription =    "This object is not allowed to be opened in a transaction.");
fAddWindowsDefine("ERROR_LOG_GROWTH_FAILED",
  sDescription =    "An attempt to create space in the transactional resource manager's log failed. The failure status has been recorded in the event log.");
fAddWindowsDefine("ERROR_TRANSACTED_MAPPING_UNSUPPORTED_REMOTE",
  sDescription =    "Memory mapping (creating a mapped section) a remote file under a transaction is not supported.");
fAddWindowsDefine("ERROR_TXF_METADATA_ALREADY_PRESENT",
  sDescription =    "Transaction metadata is already present on this file and cannot be superseded.");
fAddWindowsDefine("ERROR_TRANSACTION_SCOPE_CALLBACKS_NOT_SET",
  sDescription =    "A transaction scope could not be entered because the scope handler has not been initialized.");
fAddWindowsDefine("ERROR_TRANSACTION_REQUIRED_PROMOTION",
  sDescription =    "Promotion was required in order to allow the resource manager to enlist, but the transaction was set to disallow it.");
fAddWindowsDefine("ERROR_CANNOT_EXECUTE_FILE_IN_TRANSACTION",
  sDescription =    "This file is open for modification in an unresolved transaction and may be opened for execute only by a transacted reader.");
fAddWindowsDefine("ERROR_TRANSACTIONS_NOT_FROZEN",
  sDescription =    "The request to thaw frozen transactions was ignored because transactions had not previously been frozen.");
fAddWindowsDefine("ERROR_TRANSACTION_FREEZE_IN_PROGRESS",
  sDescription =    "Transactions cannot be frozen because a freeze is already in progress.");
fAddWindowsDefine("ERROR_NOT_SNAPSHOT_VOLUME",
  sDescription =    "The target volume is not a snapshot volume. This operation is only valid on a volume mounted as a snapshot.");
fAddWindowsDefine("ERROR_NO_SAVEPOINT_WITH_OPEN_FILES",
  sDescription =    "The savepoint operation failed because files are open on the transaction. This is not permitted.");
fAddWindowsDefine("ERROR_DATA_LOST_REPAIR",
  sDescription =    "Windows has discovered corruption in a file, and that file has since been repaired. Data loss may have occurred.");
fAddWindowsDefine("ERROR_SPARSE_NOT_ALLOWED_IN_TRANSACTION",
  sDescription =    "The sparse operation could not be completed because a transaction is active on the file.");
fAddWindowsDefine("ERROR_TM_IDENTITY_MISMATCH",
  sDescription =    "The call to create a TransactionManager object failed because the Tm Identity stored in the logfile does not match the Tm Identity that was passed in as an argument.");
fAddWindowsDefine("ERROR_FLOATED_SECTION",
  sDescription =    "I/O was attempted on a section object that has been floated as a result of a transaction ending. There is no valid data.");
fAddWindowsDefine("ERROR_CANNOT_ACCEPT_TRANSACTED_WORK",
  sDescription =    "The transactional resource manager cannot currently accept transacted work due to a transient condition such as low resources.");
fAddWindowsDefine("ERROR_CANNOT_ABORT_TRANSACTIONS",
  sDescription =    "The transactional resource manager had too many tranactions outstanding that could not be aborted. The transactional resource manger has been shut down.");
fAddWindowsDefine("ERROR_BAD_CLUSTERS",
  sDescription =    "The operation could not be completed due to bad clusters on disk.");
fAddWindowsDefine("ERROR_COMPRESSION_NOT_ALLOWED_IN_TRANSACTION",
  sDescription =    "The compression operation could not be completed because a transaction is active on the file.");
fAddWindowsDefine("ERROR_VOLUME_DIRTY",
  sDescription =    "The operation could not be completed because the volume is dirty. Please run chkdsk and try again.");
fAddWindowsDefine("ERROR_NO_LINK_TRACKING_IN_TRANSACTION",
  sDescription =    "The link tracking operation could not be completed because a transaction is active.");
fAddWindowsDefine("ERROR_OPERATION_NOT_SUPPORTED_IN_TRANSACTION",
  sDescription =    "This operation cannot be performed in a transaction.");
fAddWindowsDefine("ERROR_EXPIRED_HANDLE",
  sDescription =    "The handle is no longer properly associated with its transaction. It may have been opened in a transactional resource manager that was subsequently forced to restart. Please close the handle and open a new one.");
fAddWindowsDefine("ERROR_TRANSACTION_NOT_ENLISTED",
  sDescription =    "The specified operation could not be performed because the resource manager is not enlisted in the transaction.");
fAddWindowsDefine("ERROR_CTX_WINSTATION_NAME_INVALID",
  sDescription =    "The specified session name is invalid.");
fAddWindowsDefine("ERROR_CTX_INVALID_PD",
  sDescription =    "The specified protocol driver is invalid.");
fAddWindowsDefine("ERROR_CTX_PD_NOT_FOUND",
  sDescription =    "The specified protocol driver was not found in the system path.");
fAddWindowsDefine("ERROR_CTX_WD_NOT_FOUND",
  sDescription =    "The specified terminal connection driver was not found in the system path.");
fAddWindowsDefine("ERROR_CTX_CANNOT_MAKE_EVENTLOG_ENTRY",
  sDescription =    "A registry key for event logging could not be created for this session.");
fAddWindowsDefine("ERROR_CTX_SERVICE_NAME_COLLISION",
  sDescription =    "A service with the same name already exists on the system.");
fAddWindowsDefine("ERROR_CTX_CLOSE_PENDING",
  sDescription =    "A close operation is pending on the session.");
fAddWindowsDefine("ERROR_CTX_NO_OUTBUF",
  sDescription =    "There are no free output buffers available.");
fAddWindowsDefine("ERROR_CTX_MODEM_INF_NOT_FOUND",
  sDescription =    "The MODEM.INF file was not found.");
fAddWindowsDefine("ERROR_CTX_INVALID_MODEMNAME",
  sDescription =    "The modem name was not found in MODEM.INF.");
fAddWindowsDefine("ERROR_CTX_MODEM_RESPONSE_ERROR",
  sDescription =    "The modem did not accept the command sent to it. Verify that the configured modem name matches the attached modem.");
fAddWindowsDefine("ERROR_CTX_MODEM_RESPONSE_TIMEOUT",
  sDescription =    "The modem did not respond to the command sent to it. Verify that the modem is properly cabled and powered on.");
fAddWindowsDefine("ERROR_CTX_MODEM_RESPONSE_NO_CARRIER",
  sDescription =    "Carrier detect has failed or carrier has been dropped due to disconnect.");
fAddWindowsDefine("ERROR_CTX_MODEM_RESPONSE_NO_DIALTONE",
  sDescription =    "Dial tone not detected within the required time. Verify that the phone cable is properly attached and functional.");
fAddWindowsDefine("ERROR_CTX_MODEM_RESPONSE_BUSY",
  sDescription =    "Busy signal detected at remote site on callback.");
fAddWindowsDefine("ERROR_CTX_MODEM_RESPONSE_VOICE",
  sDescription =    "Voice detected at remote site on callback.");
fAddWindowsDefine("ERROR_CTX_TD_ERROR",
  sDescription =    "Transport driver error");
fAddWindowsDefine("ERROR_CTX_WINSTATION_NOT_FOUND",
  sDescription =    "The specified session cannot be found.");
fAddWindowsDefine("ERROR_CTX_WINSTATION_ALREADY_EXISTS",
  sDescription =    "The specified session name is already in use.");
fAddWindowsDefine("ERROR_CTX_WINSTATION_BUSY",
  sDescription =    "The task you are trying to do can't be completed because Remote Desktop Services is currently busy. Please try again in a few minutes. Other users should still be able to log on.");
fAddWindowsDefine("ERROR_CTX_BAD_VIDEO_MODE",
  sDescription =    "An attempt has been made to connect to a session whose video mode is not supported by the current client.");
fAddWindowsDefine("ERROR_CTX_GRAPHICS_INVALID",
  sDescription =    "The application attempted to enable DOS graphics mode. DOS graphics mode is not supported.");
fAddWindowsDefine("ERROR_CTX_LOGON_DISABLED",
  sDescription =    "Your interactive logon privilege has been disabled. Please contact your administrator.");
fAddWindowsDefine("ERROR_CTX_NOT_CONSOLE",
  sDescription =    "The requested operation can be performed only on the system console. This is most often the result of a driver or system DLL requiring direct console access.");
fAddWindowsDefine("ERROR_CTX_CLIENT_QUERY_TIMEOUT",
  sDescription =    "The client failed to respond to the server connect message.");
fAddWindowsDefine("ERROR_CTX_CONSOLE_DISCONNECT",
  sDescription =    "Disconnecting the console session is not supported.");
fAddWindowsDefine("ERROR_CTX_CONSOLE_CONNECT",
  sDescription =    "Reconnecting a disconnected session to the console is not supported.");
fAddWindowsDefine("ERROR_CTX_SHADOW_DENIED",
  sDescription =    "The request to control another session remotely was denied.");
fAddWindowsDefine("ERROR_CTX_WINSTATION_ACCESS_DENIED",
  sDescription =    "The requested session access is denied.");
fAddWindowsDefine("ERROR_CTX_INVALID_WD",
  sDescription =    "The specified terminal connection driver is invalid.");
fAddWindowsDefine("ERROR_CTX_SHADOW_INVALID",
  sDescription =    "The requested session cannot be controlled remotely. This may be because the session is disconnected or does not currently have a user logged on.");
fAddWindowsDefine("ERROR_CTX_SHADOW_DISABLED",
  sDescription =    "The requested session is not configured to allow remote control.");
fAddWindowsDefine("ERROR_CTX_CLIENT_LICENSE_IN_USE",
  sDescription =    "Your request to connect to this Terminal Server has been rejected. Your Terminal Server client license number is currently being used by another user. Please call your system administrator to obtain a unique license number.");
fAddWindowsDefine("ERROR_CTX_CLIENT_LICENSE_NOT_SET",
  sDescription =    "Your request to connect to this Terminal Server has been rejected. Your Terminal Server client license number has not been entered for this copy of the Terminal Server client. Please contact your system administrator.");
fAddWindowsDefine("ERROR_CTX_LICENSE_NOT_AVAILABLE",
  sDescription =    "The number of connections to this computer is limited and all connections are in use right now. Try connecting later or contact your system administrator.");
fAddWindowsDefine("ERROR_CTX_LICENSE_CLIENT_INVALID",
  sDescription =    "The client you are using is not licensed to use this system. Your logon request is denied.");
fAddWindowsDefine("ERROR_CTX_LICENSE_EXPIRED",
  sDescription =    "The system license has expired. Your logon request is denied.");
fAddWindowsDefine("ERROR_CTX_SHADOW_NOT_RUNNING",
  sDescription =    "Remote control could not be terminated because the specified session is not currently being remotely controlled.");
fAddWindowsDefine("ERROR_CTX_SHADOW_ENDED_BY_MODE_CHANGE",
  sDescription =    "The remote control of the console was terminated because the display mode was changed. Changing the display mode in a remote control session is not supported.");
fAddWindowsDefine("ERROR_ACTIVATION_COUNT_EXCEEDED",
  sDescription =    "Activation has already been reset the maximum number of times for this installation. Your activation timer will not be cleared.");
fAddWindowsDefine("ERROR_CTX_WINSTATIONS_DISABLED",
  sDescription =    "Remote logins are currently disabled.");
fAddWindowsDefine("ERROR_CTX_ENCRYPTION_LEVEL_REQUIRED",
  sDescription =    "You do not have the proper encryption level to access this Session.");
fAddWindowsDefine("ERROR_CTX_SESSION_IN_USE",
  sDescription =    "The user %s\%s is currently logged on to this computer. Only the current user or an administrator can log on to this computer.");
fAddWindowsDefine("ERROR_CTX_NO_FORCE_LOGOFF",
  sDescription =    "The user %s\%s is already logged on to the console of this computer. You do not have permission to log in at this time. To resolve this issue, contact %s\%s and have them log off.");
fAddWindowsDefine("ERROR_CTX_ACCOUNT_RESTRICTION",
  sDescription =    "Unable to log you on because of an account restriction.");
fAddWindowsDefine("ERROR_RDP_PROTOCOL_ERROR",
  sDescription =    "The RDP protocol component %2 detected an error in the protocol stream and has disconnected the client.");
fAddWindowsDefine("ERROR_CTX_CDM_CONNECT",
  sDescription =    "The Client Drive Mapping Service Has Connected on Terminal Connection.");
fAddWindowsDefine("ERROR_CTX_CDM_DISCONNECT",
  sDescription =    "The Client Drive Mapping Service Has Disconnected on Terminal Connection.");
fAddWindowsDefine("ERROR_CTX_SECURITY_LAYER_ERROR",
  sDescription =    "The Terminal Server security layer detected an error in the protocol stream and has disconnected the client.");
fAddWindowsDefine("ERROR_TS_INCOMPATIBLE_SESSIONS",
  sDescription =    "The target session is incompatible with the current session.");
fAddWindowsDefine("ERROR_TS_VIDEO_SUBSYSTEM_ERROR",
  sDescription =    "Windows can't connect to your session because a problem occurred in the Windows video subsystem. Try connecting again later, or contact the server administrator for assistance.");
fAddWindowsDefine("FRS_ERR_INVALID_API_SEQUENCE",
  sDescription =    "The file replication service API was called incorrectly.");
fAddWindowsDefine("FRS_ERR_STARTING_SERVICE",
  sDescription =    "The file replication service cannot be started.");
fAddWindowsDefine("FRS_ERR_STOPPING_SERVICE",
  sDescription =    "The file replication service cannot be stopped.");
fAddWindowsDefine("FRS_ERR_INTERNAL_API",
  sDescription =    "The file replication service API terminated the request. The event log may have more information.");
fAddWindowsDefine("FRS_ERR_INTERNAL",
  sDescription =    "The file replication service terminated the request. The event log may have more information.");
fAddWindowsDefine("FRS_ERR_SERVICE_COMM",
  sDescription =    "The file replication service cannot be contacted. The event log may have more information.");
fAddWindowsDefine("FRS_ERR_INSUFFICIENT_PRIV",
  sDescription =    "The file replication service cannot satisfy the request because the user has insufficient privileges. The event log may have more information.");
fAddWindowsDefine("FRS_ERR_AUTHENTICATION",
  sDescription =    "The file replication service cannot satisfy the request because authenticated RPC is not available. The event log may have more information.");
fAddWindowsDefine("FRS_ERR_PARENT_INSUFFICIENT_PRIV",
  sDescription =    "The file replication service cannot satisfy the request because the user has insufficient privileges on the domain controller. The event log may have more information.");
fAddWindowsDefine("FRS_ERR_PARENT_AUTHENTICATION",
  sDescription =    "The file replication service cannot satisfy the request because authenticated RPC is not available on the domain controller. The event log may have more information.");
fAddWindowsDefine("FRS_ERR_CHILD_TO_PARENT_COMM",
  sDescription =    "The file replication service cannot communicate with the file replication service on the domain controller. The event log may have more information.");
fAddWindowsDefine("FRS_ERR_PARENT_TO_CHILD_COMM",
  sDescription =    "The file replication service on the domain controller cannot communicate with the file replication service on this computer. The event log may have more information.");
fAddWindowsDefine("FRS_ERR_SYSVOL_POPULATE",
  sDescription =    "The file replication service cannot populate the system volume because of an internal error. The event log may have more information.");
fAddWindowsDefine("FRS_ERR_SYSVOL_POPULATE_TIMEOUT",
  sDescription =    "The file replication service cannot populate the system volume because of an internal timeout. The event log may have more information.");
fAddWindowsDefine("FRS_ERR_SYSVOL_IS_BUSY",
  sDescription =    "The file replication service cannot process the request. The system volume is busy with a previous request.");
fAddWindowsDefine("FRS_ERR_SYSVOL_DEMOTE",
  sDescription =    "The file replication service cannot stop replicating the system volume because of an internal error. The event log may have more information.");
fAddWindowsDefine("FRS_ERR_INVALID_SERVICE_PARAMETER",
  sDescription =    "The file replication service detected an invalid parameter.");
fAddWindowsDefine("ERROR_DS_NOT_INSTALLED",
  sDescription =    "An error occurred while installing the directory service. For more information, see the event log.");
fAddWindowsDefine("ERROR_DS_MEMBERSHIP_EVALUATED_LOCALLY",
  sDescription =    "The directory service evaluated group memberships locally.");
fAddWindowsDefine("ERROR_DS_NO_ATTRIBUTE_OR_VALUE",
  sDescription =    "The specified directory service attribute or value does not exist.");
fAddWindowsDefine("ERROR_DS_INVALID_ATTRIBUTE_SYNTAX",
  sDescription =    "The attribute syntax specified to the directory service is invalid.");
fAddWindowsDefine("ERROR_DS_ATTRIBUTE_TYPE_UNDEFINED",
  sDescription =    "The attribute type specified to the directory service is not defined.");
fAddWindowsDefine("ERROR_DS_ATTRIBUTE_OR_VALUE_EXISTS",
  sDescription =    "The specified directory service attribute or value already exists.");
fAddWindowsDefine("ERROR_DS_BUSY",
  sDescription =    "The directory service is busy.");
fAddWindowsDefine("ERROR_DS_UNAVAILABLE",
  sDescription =    "The directory service is unavailable.");
fAddWindowsDefine("ERROR_DS_NO_RIDS_ALLOCATED",
  sDescription =    "The directory service was unable to allocate a relative identifier.");
fAddWindowsDefine("ERROR_DS_NO_MORE_RIDS",
  sDescription =    "The directory service has exhausted the pool of relative identifiers.");
fAddWindowsDefine("ERROR_DS_INCORRECT_ROLE_OWNER",
  sDescription =    "The requested operation could not be performed because the directory service is not the master for that type of operation.");
fAddWindowsDefine("ERROR_DS_RIDMGR_INIT_ERROR",
  sDescription =    "The directory service was unable to initialize the subsystem that allocates relative identifiers.");
fAddWindowsDefine("ERROR_DS_OBJ_CLASS_VIOLATION",
  sDescription =    "The requested operation did not satisfy one or more constraints associated with the class of the object.");
fAddWindowsDefine("ERROR_DS_CANT_ON_NON_LEAF",
  sDescription =    "The directory service can perform the requested operation only on a leaf object.");
fAddWindowsDefine("ERROR_DS_CANT_ON_RDN",
  sDescription =    "The directory service cannot perform the requested operation on the RDN attribute of an object.");
fAddWindowsDefine("ERROR_DS_CANT_MOD_OBJ_CLASS",
  sDescription =    "The directory service detected an attempt to modify the object class of an object.");
fAddWindowsDefine("ERROR_DS_CROSS_DOM_MOVE_ERROR",
  sDescription =    "The requested cross-domain move operation could not be performed.");
fAddWindowsDefine("ERROR_DS_GC_NOT_AVAILABLE",
  sDescription =    "Unable to contact the global catalog server.");
fAddWindowsDefine("ERROR_SHARED_POLICY",
  sDescription =    "The policy object is shared and can only be modified at the root.");
fAddWindowsDefine("ERROR_POLICY_OBJECT_NOT_FOUND",
  sDescription =    "The policy object does not exist.");
fAddWindowsDefine("ERROR_POLICY_ONLY_IN_DS",
  sDescription =    "The requested policy information is only in the directory service.");
fAddWindowsDefine("ERROR_PROMOTION_ACTIVE",
  sDescription =    "A domain controller promotion is currently active.");
fAddWindowsDefine("ERROR_NO_PROMOTION_ACTIVE",
  sDescription =    "A domain controller promotion is not currently active");
fAddWindowsDefine("ERROR_DS_OPERATIONS_ERROR",
  sDescription =    "An operations error occurred.");
fAddWindowsDefine("ERROR_DS_PROTOCOL_ERROR",
  sDescription =    "A protocol error occurred.");
fAddWindowsDefine("ERROR_DS_TIMELIMIT_EXCEEDED",
  sDescription =    "The time limit for this request was exceeded.");
fAddWindowsDefine("ERROR_DS_SIZELIMIT_EXCEEDED",
  sDescription =    "The size limit for this request was exceeded.");
fAddWindowsDefine("ERROR_DS_ADMIN_LIMIT_EXCEEDED",
  sDescription =    "The administrative limit for this request was exceeded.");
fAddWindowsDefine("ERROR_DS_COMPARE_FALSE",
  sDescription =    "The compare response was false.");
fAddWindowsDefine("ERROR_DS_COMPARE_TRUE",
  sDescription =    "The compare response was true.");
fAddWindowsDefine("ERROR_DS_AUTH_METHOD_NOT_SUPPORTED",
  sDescription =    "The requested authentication method is not supported by the server.");
fAddWindowsDefine("ERROR_DS_STRONG_AUTH_REQUIRED",
  sDescription =    "A more secure authentication method is required for this server.");
fAddWindowsDefine("ERROR_DS_INAPPROPRIATE_AUTH",
  sDescription =    "Inappropriate authentication.");
fAddWindowsDefine("ERROR_DS_AUTH_UNKNOWN",
  sDescription =    "The authentication mechanism is unknown.");
fAddWindowsDefine("ERROR_DS_REFERRAL",
  sDescription =    "A referral was returned from the server.");
fAddWindowsDefine("ERROR_DS_UNAVAILABLE_CRIT_EXTENSION",
  sDescription =    "The server does not support the requested critical extension.");
fAddWindowsDefine("ERROR_DS_CONFIDENTIALITY_REQUIRED",
  sDescription =    "This request requires a secure connection.");
fAddWindowsDefine("ERROR_DS_INAPPROPRIATE_MATCHING",
  sDescription =    "Inappropriate matching.");
fAddWindowsDefine("ERROR_DS_CONSTRAINT_VIOLATION",
  sDescription =    "A constraint violation occurred.");
fAddWindowsDefine("ERROR_DS_NO_SUCH_OBJECT",
  sDescription =    "There is no such object on the server.");
fAddWindowsDefine("ERROR_DS_ALIAS_PROBLEM",
  sDescription =    "There is an alias problem.");
fAddWindowsDefine("ERROR_DS_INVALID_DN_SYNTAX",
  sDescription =    "An invalid dn syntax has been specified.");
fAddWindowsDefine("ERROR_DS_IS_LEAF",
  sDescription =    "The object is a leaf object.");
fAddWindowsDefine("ERROR_DS_ALIAS_DEREF_PROBLEM",
  sDescription =    "There is an alias dereferencing problem.");
fAddWindowsDefine("ERROR_DS_UNWILLING_TO_PERFORM",
  sDescription =    "The server is unwilling to process the request.");
fAddWindowsDefine("ERROR_DS_LOOP_DETECT",
  sDescription =    "A loop has been detected.");
fAddWindowsDefine("ERROR_DS_NAMING_VIOLATION",
  sDescription =    "There is a naming violation.");
fAddWindowsDefine("ERROR_DS_OBJECT_RESULTS_TOO_LARGE",
  sDescription =    "The result set is too large.");
fAddWindowsDefine("ERROR_DS_AFFECTS_MULTIPLE_DSAS",
  sDescription =    "The operation affects multiple DSAs");
fAddWindowsDefine("ERROR_DS_SERVER_DOWN",
  sDescription =    "The server is not operational.");
fAddWindowsDefine("ERROR_DS_LOCAL_ERROR",
  sDescription =    "A local error has occurred.");
fAddWindowsDefine("ERROR_DS_ENCODING_ERROR",
  sDescription =    "An encoding error has occurred.");
fAddWindowsDefine("ERROR_DS_DECODING_ERROR",
  sDescription =    "A decoding error has occurred.");
fAddWindowsDefine("ERROR_DS_FILTER_UNKNOWN",
  sDescription =    "The search filter cannot be recognized.");
fAddWindowsDefine("ERROR_DS_PARAM_ERROR",
  sDescription =    "One or more parameters are illegal.");
fAddWindowsDefine("ERROR_DS_NOT_SUPPORTED",
  sDescription =    "The specified method is not supported.");
fAddWindowsDefine("ERROR_DS_NO_RESULTS_RETURNED",
  sDescription =    "No results were returned.");
fAddWindowsDefine("ERROR_DS_CONTROL_NOT_FOUND",
  sDescription =    "The specified control is not supported by the server.");
fAddWindowsDefine("ERROR_DS_CLIENT_LOOP",
  sDescription =    "A referral loop was detected by the client.");
fAddWindowsDefine("ERROR_DS_REFERRAL_LIMIT_EXCEEDED",
  sDescription =    "The preset referral limit was exceeded.");
fAddWindowsDefine("ERROR_DS_SORT_CONTROL_MISSING",
  sDescription =    "The search requires a SORT control.");
fAddWindowsDefine("ERROR_DS_OFFSET_RANGE_ERROR",
  sDescription =    "The search results exceed the offset range specified.");
fAddWindowsDefine("ERROR_DS_RIDMGR_DISABLED",
  sDescription =    "The directory service detected the subsystem that allocates relative identifiers is disabled. This can occur as a protective mechanism when the system determines a significant portion of relative identifiers (RIDs) have been exhausted. Please see http://go.microsoft.com/fwlink/?LinkId=228610 for recommended diagnostic steps and the procedure to re-enable account creation.");
fAddWindowsDefine("ERROR_DS_ROOT_MUST_BE_NC",
  sDescription =    "The root object must be the head of a naming context. The root object cannot have an instantiated parent.");
fAddWindowsDefine("ERROR_DS_ADD_REPLICA_INHIBITED",
  sDescription =    "The add replica operation cannot be performed. The naming context must be writeable in order to create the replica.");
fAddWindowsDefine("ERROR_DS_ATT_NOT_DEF_IN_SCHEMA",
  sDescription =    "A reference to an attribute that is not defined in the schema occurred.");
fAddWindowsDefine("ERROR_DS_MAX_OBJ_SIZE_EXCEEDED",
  sDescription =    "The maximum size of an object has been exceeded.");
fAddWindowsDefine("ERROR_DS_OBJ_STRING_NAME_EXISTS",
  sDescription =    "An attempt was made to add an object to the directory with a name that is already in use.");
fAddWindowsDefine("ERROR_DS_NO_RDN_DEFINED_IN_SCHEMA",
  sDescription =    "An attempt was made to add an object of a class that does not have an RDN defined in the schema.");
fAddWindowsDefine("ERROR_DS_RDN_DOESNT_MATCH_SCHEMA",
  sDescription =    "An attempt was made to add an object using an RDN that is not the RDN defined in the schema.");
fAddWindowsDefine("ERROR_DS_NO_REQUESTED_ATTS_FOUND",
  sDescription =    "None of the requested attributes were found on the objects.");
fAddWindowsDefine("ERROR_DS_USER_BUFFER_TO_SMALL",
  sDescription =    "The user buffer is too small.");
fAddWindowsDefine("ERROR_DS_ATT_IS_NOT_ON_OBJ",
  sDescription =    "The attribute specified in the operation is not present on the object.");
fAddWindowsDefine("ERROR_DS_ILLEGAL_MOD_OPERATION",
  sDescription =    "Illegal modify operation. Some aspect of the modification is not permitted.");
fAddWindowsDefine("ERROR_DS_OBJ_TOO_LARGE",
  sDescription =    "The specified object is too large.");
fAddWindowsDefine("ERROR_DS_BAD_INSTANCE_TYPE",
  sDescription =    "The specified instance type is not valid.");
fAddWindowsDefine("ERROR_DS_MASTERDSA_REQUIRED",
  sDescription =    "The operation must be performed at a master DSA.");
fAddWindowsDefine("ERROR_DS_OBJECT_CLASS_REQUIRED",
  sDescription =    "The object class attribute must be specified.");
fAddWindowsDefine("ERROR_DS_MISSING_REQUIRED_ATT",
  sDescription =    "A required attribute is missing.");
fAddWindowsDefine("ERROR_DS_ATT_NOT_DEF_FOR_CLASS",
  sDescription =    "An attempt was made to modify an object to include an attribute that is not legal for its class.");
fAddWindowsDefine("ERROR_DS_ATT_ALREADY_EXISTS",
  sDescription =    "The specified attribute is already present on the object.");
fAddWindowsDefine("ERROR_DS_CANT_ADD_ATT_VALUES",
  sDescription =    "The specified attribute is not present, or has no values.");
fAddWindowsDefine("ERROR_DS_SINGLE_VALUE_CONSTRAINT",
  sDescription =    "Multiple values were specified for an attribute that can have only one value.");
fAddWindowsDefine("ERROR_DS_RANGE_CONSTRAINT",
  sDescription =    "A value for the attribute was not in the acceptable range of values.");
fAddWindowsDefine("ERROR_DS_ATT_VAL_ALREADY_EXISTS",
  sDescription =    "The specified value already exists.");
fAddWindowsDefine("ERROR_DS_CANT_REM_MISSING_ATT",
  sDescription =    "The attribute cannot be removed because it is not present on the object.");
fAddWindowsDefine("ERROR_DS_CANT_REM_MISSING_ATT_VAL",
  sDescription =    "The attribute value cannot be removed because it is not present on the object.");
fAddWindowsDefine("ERROR_DS_ROOT_CANT_BE_SUBREF",
  sDescription =    "The specified root object cannot be a subref.");
fAddWindowsDefine("ERROR_DS_NO_CHAINING",
  sDescription =    "Chaining is not permitted.");
fAddWindowsDefine("ERROR_DS_NO_CHAINED_EVAL",
  sDescription =    "Chained evaluation is not permitted.");
fAddWindowsDefine("ERROR_DS_NO_PARENT_OBJECT",
  sDescription =    "The operation could not be performed because the object's parent is either uninstantiated or deleted.");
fAddWindowsDefine("ERROR_DS_PARENT_IS_AN_ALIAS",
  sDescription =    "Having a parent that is an alias is not permitted. Aliases are leaf objects.");
fAddWindowsDefine("ERROR_DS_CANT_MIX_MASTER_AND_REPS",
  sDescription =    "The object and parent must be of the same type, either both masters or both replicas.");
fAddWindowsDefine("ERROR_DS_CHILDREN_EXIST",
  sDescription =    "The operation cannot be performed because child objects exist. This operation can only be performed on a leaf object.");
fAddWindowsDefine("ERROR_DS_OBJ_NOT_FOUND",
  sDescription =    "Directory object not found.");
fAddWindowsDefine("ERROR_DS_ALIASED_OBJ_MISSING",
  sDescription =    "The aliased object is missing.");
fAddWindowsDefine("ERROR_DS_BAD_NAME_SYNTAX",
  sDescription =    "The object name has bad syntax.");
fAddWindowsDefine("ERROR_DS_ALIAS_POINTS_TO_ALIAS",
  sDescription =    "It is not permitted for an alias to refer to another alias.");
fAddWindowsDefine("ERROR_DS_CANT_DEREF_ALIAS",
  sDescription =    "The alias cannot be dereferenced.");
fAddWindowsDefine("ERROR_DS_OUT_OF_SCOPE",
  sDescription =    "The operation is out of scope.");
fAddWindowsDefine("ERROR_DS_OBJECT_BEING_REMOVED",
  sDescription =    "The operation cannot continue because the object is in the process of being removed.");
fAddWindowsDefine("ERROR_DS_CANT_DELETE_DSA_OBJ",
  sDescription =    "The DSA object cannot be deleted.");
fAddWindowsDefine("ERROR_DS_GENERIC_ERROR",
  sDescription =    "A directory service error has occurred.");
fAddWindowsDefine("ERROR_DS_DSA_MUST_BE_INT_MASTER",
  sDescription =    "The operation can only be performed on an internal master DSA object.");
fAddWindowsDefine("ERROR_DS_CLASS_NOT_DSA",
  sDescription =    "The object must be of class DSA.");
fAddWindowsDefine("ERROR_DS_INSUFF_ACCESS_RIGHTS",
  sDescription =    "Insufficient access rights to perform the operation.");
fAddWindowsDefine("ERROR_DS_ILLEGAL_SUPERIOR",
  sDescription =    "The object cannot be added because the parent is not on the list of possible superiors.");
fAddWindowsDefine("ERROR_DS_ATTRIBUTE_OWNED_BY_SAM",
  sDescription =    "Access to the attribute is not permitted because the attribute is owned by the Security Accounts Manager (SAM).");
fAddWindowsDefine("ERROR_DS_NAME_TOO_MANY_PARTS",
  sDescription =    "The name has too many parts.");
fAddWindowsDefine("ERROR_DS_NAME_TOO_LONG",
  sDescription =    "The name is too long.");
fAddWindowsDefine("ERROR_DS_NAME_VALUE_TOO_LONG",
  sDescription =    "The name value is too long.");
fAddWindowsDefine("ERROR_DS_NAME_UNPARSEABLE",
  sDescription =    "The directory service encountered an error parsing a name.");
fAddWindowsDefine("ERROR_DS_NAME_TYPE_UNKNOWN",
  sDescription =    "The directory service cannot get the attribute type for a name.");
fAddWindowsDefine("ERROR_DS_NOT_AN_OBJECT",
  sDescription =    "The name does not identify an object; the name identifies a phantom.");
fAddWindowsDefine("ERROR_DS_SEC_DESC_TOO_SHORT",
  sDescription =    "The security descriptor is too short.");
fAddWindowsDefine("ERROR_DS_SEC_DESC_INVALID",
  sDescription =    "The security descriptor is invalid.");
fAddWindowsDefine("ERROR_DS_NO_DELETED_NAME",
  sDescription =    "Failed to create name for deleted object.");
fAddWindowsDefine("ERROR_DS_SUBREF_MUST_HAVE_PARENT",
  sDescription =    "The parent of a new subref must exist.");
fAddWindowsDefine("ERROR_DS_NCNAME_MUST_BE_NC",
  sDescription =    "The object must be a naming context.");
fAddWindowsDefine("ERROR_DS_CANT_ADD_SYSTEM_ONLY",
  sDescription =    "It is not permitted to add an attribute which is owned by the system.");
fAddWindowsDefine("ERROR_DS_CLASS_MUST_BE_CONCRETE",
  sDescription =    "The class of the object must be structural; you cannot instantiate an abstract class.");
fAddWindowsDefine("ERROR_DS_INVALID_DMD",
  sDescription =    "The schema object could not be found.");
fAddWindowsDefine("ERROR_DS_OBJ_GUID_EXISTS",
  sDescription =    "A local object with this GUID (dead or alive) already exists.");
fAddWindowsDefine("ERROR_DS_NOT_ON_BACKLINK",
  sDescription =    "The operation cannot be performed on a back link.");
fAddWindowsDefine("ERROR_DS_NO_CROSSREF_FOR_NC",
  sDescription =    "The cross reference for the specified naming context could not be found.");
fAddWindowsDefine("ERROR_DS_SHUTTING_DOWN",
  sDescription =    "The operation could not be performed because the directory service is shutting down.");
fAddWindowsDefine("ERROR_DS_UNKNOWN_OPERATION",
  sDescription =    "The directory service request is invalid.");
fAddWindowsDefine("ERROR_DS_INVALID_ROLE_OWNER",
  sDescription =    "The role owner attribute could not be read.");
fAddWindowsDefine("ERROR_DS_COULDNT_CONTACT_FSMO",
  sDescription =    "The requested FSMO operation failed. The current FSMO holder could not be contacted.");
fAddWindowsDefine("ERROR_DS_CROSS_NC_DN_RENAME",
  sDescription =    "Modification of a DN across a naming context is not permitted.");
fAddWindowsDefine("ERROR_DS_CANT_MOD_SYSTEM_ONLY",
  sDescription =    "The attribute cannot be modified because it is owned by the system.");
fAddWindowsDefine("ERROR_DS_REPLICATOR_ONLY",
  sDescription =    "Only the replicator can perform this function.");
fAddWindowsDefine("ERROR_DS_OBJ_CLASS_NOT_DEFINED",
  sDescription =    "The specified class is not defined.");
fAddWindowsDefine("ERROR_DS_OBJ_CLASS_NOT_SUBCLASS",
  sDescription =    "The specified class is not a subclass.");
fAddWindowsDefine("ERROR_DS_NAME_REFERENCE_INVALID",
  sDescription =    "The name reference is invalid.");
fAddWindowsDefine("ERROR_DS_CROSS_REF_EXISTS",
  sDescription =    "A cross reference already exists.");
fAddWindowsDefine("ERROR_DS_CANT_DEL_MASTER_CROSSREF",
  sDescription =    "It is not permitted to delete a master cross reference.");
fAddWindowsDefine("ERROR_DS_SUBTREE_NOTIFY_NOT_NC_HEAD",
  sDescription =    "Subtree notifications are only supported on NC heads.");
fAddWindowsDefine("ERROR_DS_NOTIFY_FILTER_TOO_COMPLEX",
  sDescription =    "Notification filter is too complex.");
fAddWindowsDefine("ERROR_DS_DUP_RDN",
  sDescription =    "Schema update failed: duplicate RDN.");
fAddWindowsDefine("ERROR_DS_DUP_OID",
  sDescription =    "Schema update failed: duplicate OID.");
fAddWindowsDefine("ERROR_DS_DUP_MAPI_ID",
  sDescription =    "Schema update failed: duplicate MAPI identifier.");
fAddWindowsDefine("ERROR_DS_DUP_SCHEMA_ID_GUID",
  sDescription =    "Schema update failed: duplicate schema-id GUID.");
fAddWindowsDefine("ERROR_DS_DUP_LDAP_DISPLAY_NAME",
  sDescription =    "Schema update failed: duplicate LDAP display name.");
fAddWindowsDefine("ERROR_DS_SEMANTIC_ATT_TEST",
  sDescription =    "Schema update failed: range-lower less than range upper.");
fAddWindowsDefine("ERROR_DS_SYNTAX_MISMATCH",
  sDescription =    "Schema update failed: syntax mismatch.");
fAddWindowsDefine("ERROR_DS_EXISTS_IN_MUST_HAVE",
  sDescription =    "Schema deletion failed: attribute is used in must-contain.");
fAddWindowsDefine("ERROR_DS_EXISTS_IN_MAY_HAVE",
  sDescription =    "Schema deletion failed: attribute is used in may-contain.");
fAddWindowsDefine("ERROR_DS_NONEXISTENT_MAY_HAVE",
  sDescription =    "Schema update failed: attribute in may-contain does not exist.");
fAddWindowsDefine("ERROR_DS_NONEXISTENT_MUST_HAVE",
  sDescription =    "Schema update failed: attribute in must-contain does not exist.");
fAddWindowsDefine("ERROR_DS_AUX_CLS_TEST_FAIL",
  sDescription =    "Schema update failed: class in aux-class list does not exist or is not an auxiliary class.");
fAddWindowsDefine("ERROR_DS_NONEXISTENT_POSS_SUP",
  sDescription =    "Schema update failed: class in poss-superiors does not exist.");
fAddWindowsDefine("ERROR_DS_SUB_CLS_TEST_FAIL",
  sDescription =    "Schema update failed: class in subclassof list does not exist or does not satisfy hierarchy rules.");
fAddWindowsDefine("ERROR_DS_BAD_RDN_ATT_ID_SYNTAX",
  sDescription =    "Schema update failed: Rdn-Att-Id has wrong syntax.");
fAddWindowsDefine("ERROR_DS_EXISTS_IN_AUX_CLS",
  sDescription =    "Schema deletion failed: class is used as auxiliary class.");
fAddWindowsDefine("ERROR_DS_EXISTS_IN_SUB_CLS",
  sDescription =    "Schema deletion failed: class is used as sub class.");
fAddWindowsDefine("ERROR_DS_EXISTS_IN_POSS_SUP",
  sDescription =    "Schema deletion failed: class is used as poss superior.");
fAddWindowsDefine("ERROR_DS_RECALCSCHEMA_FAILED",
  sDescription =    "Schema update failed in recalculating validation cache.");
fAddWindowsDefine("ERROR_DS_TREE_DELETE_NOT_FINISHED",
  sDescription =    "The tree deletion is not finished. The request must be made again to continue deleting the tree.");
fAddWindowsDefine("ERROR_DS_CANT_DELETE",
  sDescription =    "The requested delete operation could not be performed.");
fAddWindowsDefine("ERROR_DS_ATT_SCHEMA_REQ_ID",
  sDescription =    "Cannot read the governs class identifier for the schema record.");
fAddWindowsDefine("ERROR_DS_BAD_ATT_SCHEMA_SYNTAX",
  sDescription =    "The attribute schema has bad syntax.");
fAddWindowsDefine("ERROR_DS_CANT_CACHE_ATT",
  sDescription =    "The attribute could not be cached.");
fAddWindowsDefine("ERROR_DS_CANT_CACHE_CLASS",
  sDescription =    "The class could not be cached.");
fAddWindowsDefine("ERROR_DS_CANT_REMOVE_ATT_CACHE",
  sDescription =    "The attribute could not be removed from the cache.");
fAddWindowsDefine("ERROR_DS_CANT_REMOVE_CLASS_CACHE",
  sDescription =    "The class could not be removed from the cache.");
fAddWindowsDefine("ERROR_DS_CANT_RETRIEVE_DN",
  sDescription =    "The distinguished name attribute could not be read.");
fAddWindowsDefine("ERROR_DS_MISSING_SUPREF",
  sDescription =    "No superior reference has been configured for the directory service. The directory service is therefore unable to issue referrals to objects outside this forest.");
fAddWindowsDefine("ERROR_DS_CANT_RETRIEVE_INSTANCE",
  sDescription =    "The instance type attribute could not be retrieved.");
fAddWindowsDefine("ERROR_DS_CODE_INCONSISTENCY",
  sDescription =    "An internal error has occurred.");
fAddWindowsDefine("ERROR_DS_DATABASE_ERROR",
  sDescription =    "A database error has occurred.");
fAddWindowsDefine("ERROR_DS_GOVERNSID_MISSING",
  sDescription =    "The attribute GOVERNSID is missing.");
fAddWindowsDefine("ERROR_DS_MISSING_EXPECTED_ATT",
  sDescription =    "An expected attribute is missing.");
fAddWindowsDefine("ERROR_DS_NCNAME_MISSING_CR_REF",
  sDescription =    "The specified naming context is missing a cross reference.");
fAddWindowsDefine("ERROR_DS_SECURITY_CHECKING_ERROR",
  sDescription =    "A security checking error has occurred.");
fAddWindowsDefine("ERROR_DS_SCHEMA_NOT_LOADED",
  sDescription =    "The schema is not loaded.");
fAddWindowsDefine("ERROR_DS_SCHEMA_ALLOC_FAILED",
  sDescription =    "Schema allocation failed. Please check if the machine is running low on memory.");
fAddWindowsDefine("ERROR_DS_ATT_SCHEMA_REQ_SYNTAX",
  sDescription =    "Failed to obtain the required syntax for the attribute schema.");
fAddWindowsDefine("ERROR_DS_GCVERIFY_ERROR",
  sDescription =    "The global catalog verification failed. The global catalog is not available or does not support the operation. Some part of the directory is currently not available.");
fAddWindowsDefine("ERROR_DS_DRA_SCHEMA_MISMATCH",
  sDescription =    "The replication operation failed because of a schema mismatch between the servers involved.");
fAddWindowsDefine("ERROR_DS_CANT_FIND_DSA_OBJ",
  sDescription =    "The DSA object could not be found.");
fAddWindowsDefine("ERROR_DS_CANT_FIND_EXPECTED_NC",
  sDescription =    "The naming context could not be found.");
fAddWindowsDefine("ERROR_DS_CANT_FIND_NC_IN_CACHE",
  sDescription =    "The naming context could not be found in the cache.");
fAddWindowsDefine("ERROR_DS_CANT_RETRIEVE_CHILD",
  sDescription =    "The child object could not be retrieved.");
fAddWindowsDefine("ERROR_DS_SECURITY_ILLEGAL_MODIFY",
  sDescription =    "The modification was not permitted for security reasons.");
fAddWindowsDefine("ERROR_DS_CANT_REPLACE_HIDDEN_REC",
  sDescription =    "The operation cannot replace the hidden record.");
fAddWindowsDefine("ERROR_DS_BAD_HIERARCHY_FILE",
  sDescription =    "The hierarchy file is invalid.");
fAddWindowsDefine("ERROR_DS_BUILD_HIERARCHY_TABLE_FAILED",
  sDescription =    "The attempt to build the hierarchy table failed.");
fAddWindowsDefine("ERROR_DS_CONFIG_PARAM_MISSING",
  sDescription =    "The directory configuration parameter is missing from the registry.");
fAddWindowsDefine("ERROR_DS_COUNTING_AB_INDICES_FAILED",
  sDescription =    "The attempt to count the address book indices failed.");
fAddWindowsDefine("ERROR_DS_HIERARCHY_TABLE_MALLOC_FAILED",
  sDescription =    "The allocation of the hierarchy table failed.");
fAddWindowsDefine("ERROR_DS_INTERNAL_FAILURE",
  sDescription =    "The directory service encountered an internal failure.");
fAddWindowsDefine("ERROR_DS_UNKNOWN_ERROR",
  sDescription =    "The directory service encountered an unknown failure.");
fAddWindowsDefine("ERROR_DS_ROOT_REQUIRES_CLASS_TOP",
  sDescription =    "A root object requires a class of 'top'.");
fAddWindowsDefine("ERROR_DS_REFUSING_FSMO_ROLES",
  sDescription =    "This directory server is shutting down, and cannot take ownership of new floating single-master operation roles.");
fAddWindowsDefine("ERROR_DS_MISSING_FSMO_SETTINGS",
  sDescription =    "The directory service is missing mandatory configuration information, and is unable to determine the ownership of floating single-master operation roles.");
fAddWindowsDefine("ERROR_DS_UNABLE_TO_SURRENDER_ROLES",
  sDescription =    "The directory service was unable to transfer ownership of one or more floating single-master operation roles to other servers.");
fAddWindowsDefine("ERROR_DS_DRA_GENERIC",
  sDescription =    "The replication operation failed.");
fAddWindowsDefine("ERROR_DS_DRA_INVALID_PARAMETER",
  sDescription =    "An invalid parameter was specified for this replication operation.");
fAddWindowsDefine("ERROR_DS_DRA_BUSY",
  sDescription =    "The directory service is too busy to complete the replication operation at this time.");
fAddWindowsDefine("ERROR_DS_DRA_BAD_DN",
  sDescription =    "The distinguished name specified for this replication operation is invalid.");
fAddWindowsDefine("ERROR_DS_DRA_BAD_NC",
  sDescription =    "The naming context specified for this replication operation is invalid.");
fAddWindowsDefine("ERROR_DS_DRA_DN_EXISTS",
  sDescription =    "The distinguished name specified for this replication operation already exists.");
fAddWindowsDefine("ERROR_DS_DRA_INTERNAL_ERROR",
  sDescription =    "The replication system encountered an internal error.");
fAddWindowsDefine("ERROR_DS_DRA_INCONSISTENT_DIT",
  sDescription =    "The replication operation encountered a database inconsistency.");
fAddWindowsDefine("ERROR_DS_DRA_CONNECTION_FAILED",
  sDescription =    "The server specified for this replication operation could not be contacted.");
fAddWindowsDefine("ERROR_DS_DRA_BAD_INSTANCE_TYPE",
  sDescription =    "The replication operation encountered an object with an invalid instance type.");
fAddWindowsDefine("ERROR_DS_DRA_OUT_OF_MEM",
  sDescription =    "The replication operation failed to allocate memory.");
fAddWindowsDefine("ERROR_DS_DRA_MAIL_PROBLEM",
  sDescription =    "The replication operation encountered an error with the mail system.");
fAddWindowsDefine("ERROR_DS_DRA_REF_ALREADY_EXISTS",
  sDescription =    "The replication reference information for the target server already exists.");
fAddWindowsDefine("ERROR_DS_DRA_REF_NOT_FOUND",
  sDescription =    "The replication reference information for the target server does not exist.");
fAddWindowsDefine("ERROR_DS_DRA_OBJ_IS_REP_SOURCE",
  sDescription =    "The naming context cannot be removed because it is replicated to another server.");
fAddWindowsDefine("ERROR_DS_DRA_DB_ERROR",
  sDescription =    "The replication operation encountered a database error.");
fAddWindowsDefine("ERROR_DS_DRA_NO_REPLICA",
  sDescription =    "The naming context is in the process of being removed or is not replicated from the specified server.");
fAddWindowsDefine("ERROR_DS_DRA_ACCESS_DENIED",
  sDescription =    "Replication access was denied.");
fAddWindowsDefine("ERROR_DS_DRA_NOT_SUPPORTED",
  sDescription =    "The requested operation is not supported by this version of the directory service.");
fAddWindowsDefine("ERROR_DS_DRA_RPC_CANCELLED",
  sDescription =    "The replication remote procedure call was cancelled.");
fAddWindowsDefine("ERROR_DS_DRA_SOURCE_DISABLED",
  sDescription =    "The source server is currently rejecting replication requests.");
fAddWindowsDefine("ERROR_DS_DRA_SINK_DISABLED",
  sDescription =    "The destination server is currently rejecting replication requests.");
fAddWindowsDefine("ERROR_DS_DRA_NAME_COLLISION",
  sDescription =    "The replication operation failed due to a collision of object names.");
fAddWindowsDefine("ERROR_DS_DRA_SOURCE_REINSTALLED",
  sDescription =    "The replication source has been reinstalled.");
fAddWindowsDefine("ERROR_DS_DRA_MISSING_PARENT",
  sDescription =    "The replication operation failed because a required parent object is missing.");
fAddWindowsDefine("ERROR_DS_DRA_PREEMPTED",
  sDescription =    "The replication operation was preempted.");
fAddWindowsDefine("ERROR_DS_DRA_ABANDON_SYNC",
  sDescription =    "The replication synchronization attempt was abandoned because of a lack of updates.");
fAddWindowsDefine("ERROR_DS_DRA_SHUTDOWN",
  sDescription =    "The replication operation was terminated because the system is shutting down.");
fAddWindowsDefine("ERROR_DS_DRA_INCOMPATIBLE_PARTIAL_SET",
  sDescription =    "Synchronization attempt failed because the destination DC is currently waiting to synchronize new partial attributes from source. This condition is normal if a recent schema change modified the partial attribute set. The destination partial attribute set is not a subset of source partial attribute set.");
fAddWindowsDefine("ERROR_DS_DRA_SOURCE_IS_PARTIAL_REPLICA",
  sDescription =    "The replication synchronization attempt failed because a master replica attempted to sync from a partial replica.");
fAddWindowsDefine("ERROR_DS_DRA_EXTN_CONNECTION_FAILED",
  sDescription =    "The server specified for this replication operation was contacted, but that server was unable to contact an additional server needed to complete the operation.");
fAddWindowsDefine("ERROR_DS_INSTALL_SCHEMA_MISMATCH",
  sDescription =    "The version of the directory service schema of the source forest is not compatible with the version of directory service on this computer.");
fAddWindowsDefine("ERROR_DS_DUP_LINK_ID",
  sDescription =    "Schema update failed: An attribute with the same link identifier already exists.");
fAddWindowsDefine("ERROR_DS_NAME_ERROR_RESOLVING",
  sDescription =    "Name translation: Generic processing error.");
fAddWindowsDefine("ERROR_DS_NAME_ERROR_NOT_FOUND",
  sDescription =    "Name translation: Could not find the name or insufficient right to see name.");
fAddWindowsDefine("ERROR_DS_NAME_ERROR_NOT_UNIQUE",
  sDescription =    "Name translation: Input name mapped to more than one output name.");
fAddWindowsDefine("ERROR_DS_NAME_ERROR_NO_MAPPING",
  sDescription =    "Name translation: Input name found, but not the associated output format.");
fAddWindowsDefine("ERROR_DS_NAME_ERROR_DOMAIN_ONLY",
  sDescription =    "Name translation: Unable to resolve completely, only the domain was found.");
fAddWindowsDefine("ERROR_DS_NAME_ERROR_NO_SYNTACTICAL_MAPPING",
  sDescription =    "Name translation: Unable to perform purely syntactical mapping at the client without going out to the wire.");
fAddWindowsDefine("ERROR_DS_CONSTRUCTED_ATT_MOD",
  sDescription =    "Modification of a constructed attribute is not allowed.");
fAddWindowsDefine("ERROR_DS_WRONG_OM_OBJ_CLASS",
  sDescription =    "The OM-Object-Class specified is incorrect for an attribute with the specified syntax.");
fAddWindowsDefine("ERROR_DS_DRA_REPL_PENDING",
  sDescription =    "The replication request has been posted; waiting for reply.");
fAddWindowsDefine("ERROR_DS_DS_REQUIRED",
  sDescription =    "The requested operation requires a directory service, and none was available.");
fAddWindowsDefine("ERROR_DS_INVALID_LDAP_DISPLAY_NAME",
  sDescription =    "The LDAP display name of the class or attribute contains non-ASCII characters.");
fAddWindowsDefine("ERROR_DS_NON_BASE_SEARCH",
  sDescription =    "The requested search operation is only supported for base searches.");
fAddWindowsDefine("ERROR_DS_CANT_RETRIEVE_ATTS",
  sDescription =    "The search failed to retrieve attributes from the database.");
fAddWindowsDefine("ERROR_DS_BACKLINK_WITHOUT_LINK",
  sDescription =    "The schema update operation tried to add a backward link attribute that has no corresponding forward link.");
fAddWindowsDefine("ERROR_DS_EPOCH_MISMATCH",
  sDescription =    "Source and destination of a cross-domain move do not agree on the object's epoch number. Either source or destination does not have the latest version of the object.");
fAddWindowsDefine("ERROR_DS_SRC_NAME_MISMATCH",
  sDescription =    "Source and destination of a cross-domain move do not agree on the object's current name. Either source or destination does not have the latest version of the object.");
fAddWindowsDefine("ERROR_DS_SRC_AND_DST_NC_IDENTICAL",
  sDescription =    "Source and destination for the cross-domain move operation are identical. Caller should use local move operation instead of cross-domain move operation.");
fAddWindowsDefine("ERROR_DS_DST_NC_MISMATCH",
  sDescription =    "Source and destination for a cross-domain move are not in agreement on the naming contexts in the forest. Either source or destination does not have the latest version of the Partitions container.");
fAddWindowsDefine("ERROR_DS_NOT_AUTHORITIVE_FOR_DST_NC",
  sDescription =    "Destination of a cross-domain move is not authoritative for the destination naming context.");
fAddWindowsDefine("ERROR_DS_SRC_GUID_MISMATCH",
  sDescription =    "Source and destination of a cross-domain move do not agree on the identity of the source object. Either source or destination does not have the latest version of the source object.");
fAddWindowsDefine("ERROR_DS_CANT_MOVE_DELETED_OBJECT",
  sDescription =    "Object being moved across-domains is already known to be deleted by the destination server. The source server does not have the latest version of the source object.");
fAddWindowsDefine("ERROR_DS_PDC_OPERATION_IN_PROGRESS",
  sDescription =    "Another operation which requires exclusive access to the PDC FSMO is already in progress.");
fAddWindowsDefine("ERROR_DS_CROSS_DOMAIN_CLEANUP_REQD",
  sDescription =    "A cross-domain move operation failed such that two versions of the moved object exist - one each in the source and destination domains. The destination object needs to be removed to restore the system to a consistent state.");
fAddWindowsDefine("ERROR_DS_ILLEGAL_XDOM_MOVE_OPERATION",
  sDescription =    "This object may not be moved across domain boundaries either because cross-domain moves for this class are disallowed, or the object has some special characteristics, e.g.: trust account or restricted RID, which prevent its move.");
fAddWindowsDefine("ERROR_DS_CANT_WITH_ACCT_GROUP_MEMBERSHPS",
  sDescription =    "Can't move objects with memberships across domain boundaries as once moved, this would violate the membership conditions of the account group. Remove the object from any account group memberships and retry.");
fAddWindowsDefine("ERROR_DS_NC_MUST_HAVE_NC_PARENT",
  sDescription =    "A naming context head must be the immediate child of another naming context head, not of an interior node.");
fAddWindowsDefine("ERROR_DS_CR_IMPOSSIBLE_TO_VALIDATE",
  sDescription =    "The directory cannot validate the proposed naming context name because it does not hold a replica of the naming context above the proposed naming context. Please ensure that the domain naming master role is held by a server that is configured as a global catalog server, and that the server is up to date with its replication partners. (Applies only to Windows 2000 Domain Naming masters)");
fAddWindowsDefine("ERROR_DS_DST_DOMAIN_NOT_NATIVE",
  sDescription =    "Destination domain must be in native mode.");
fAddWindowsDefine("ERROR_DS_MISSING_INFRASTRUCTURE_CONTAINER",
  sDescription =    "The operation cannot be performed because the server does not have an infrastructure container in the domain of interest.");
fAddWindowsDefine("ERROR_DS_CANT_MOVE_ACCOUNT_GROUP",
  sDescription =    "Cross-domain move of non-empty account groups is not allowed.");
fAddWindowsDefine("ERROR_DS_CANT_MOVE_RESOURCE_GROUP",
  sDescription =    "Cross-domain move of non-empty resource groups is not allowed.");
fAddWindowsDefine("ERROR_DS_INVALID_SEARCH_FLAG",
  sDescription =    "The search flags for the attribute are invalid. The ANR bit is valid only on attributes of Unicode or Teletex strings.");
fAddWindowsDefine("ERROR_DS_NO_TREE_DELETE_ABOVE_NC",
  sDescription =    "Tree deletions starting at an object which has an NC head as a descendant are not allowed.");
fAddWindowsDefine("ERROR_DS_COULDNT_LOCK_TREE_FOR_DELETE",
  sDescription =    "The directory service failed to lock a tree in preparation for a tree deletion because the tree was in use.");
fAddWindowsDefine("ERROR_DS_COULDNT_IDENTIFY_OBJECTS_FOR_TREE_DELETE",
  sDescription =    "The directory service failed to identify the list of objects to delete while attempting a tree deletion.");
fAddWindowsDefine("ERROR_DS_SAM_INIT_FAILURE",
  sDescription =    "Security Accounts Manager initialization failed because of the following error: %1. Error Status: 0x%2. Please shutdown this system and reboot into Directory Services Restore Mode, check the event log for more detailed information.");
fAddWindowsDefine("ERROR_DS_SENSITIVE_GROUP_VIOLATION",
  sDescription =    "Only an administrator can modify the membership list of an administrative group.");
fAddWindowsDefine("ERROR_DS_CANT_MOD_PRIMARYGROUPID",
  sDescription =    "Cannot change the primary group ID of a domain controller account.");
fAddWindowsDefine("ERROR_DS_ILLEGAL_BASE_SCHEMA_MOD",
  sDescription =    "An attempt is made to modify the base schema.");
fAddWindowsDefine("ERROR_DS_NONSAFE_SCHEMA_CHANGE",
  sDescription =    "Adding a new mandatory attribute to an existing class, deleting a mandatory attribute from an existing class, or adding an optional attribute to the special class Top that is not a backlink attribute (directly or through inheritance, for example, by adding or deleting an auxiliary class) is not allowed.");
fAddWindowsDefine("ERROR_DS_SCHEMA_UPDATE_DISALLOWED",
  sDescription =    "Schema update is not allowed on this DC because the DC is not the schema FSMO Role Owner.");
fAddWindowsDefine("ERROR_DS_CANT_CREATE_UNDER_SCHEMA",
  sDescription =    "An object of this class cannot be created under the schema container. You can only create attribute-schema and class-schema objects under the schema container.");
fAddWindowsDefine("ERROR_DS_INSTALL_NO_SRC_SCH_VERSION",
  sDescription =    "The replica/child install failed to get the objectVersion attribute on the schema container on the source DC. Either the attribute is missing on the schema container or the credentials supplied do not have permission to read it.");
fAddWindowsDefine("ERROR_DS_INSTALL_NO_SCH_VERSION_IN_INIFILE",
  sDescription =    "The replica/child install failed to read the objectVersion attribute in the SCHEMA section of the file schema.ini in the system32 directory.");
fAddWindowsDefine("ERROR_DS_INVALID_GROUP_TYPE",
  sDescription =    "The specified group type is invalid.");
fAddWindowsDefine("ERROR_DS_NO_NEST_GLOBALGROUP_IN_MIXEDDOMAIN",
  sDescription =    "You cannot nest global groups in a mixed domain if the group is security-enabled.");
fAddWindowsDefine("ERROR_DS_NO_NEST_LOCALGROUP_IN_MIXEDDOMAIN",
  sDescription =    "You cannot nest local groups in a mixed domain if the group is security-enabled.");
fAddWindowsDefine("ERROR_DS_GLOBAL_CANT_HAVE_LOCAL_MEMBER",
  sDescription =    "A global group cannot have a local group as a member.");
fAddWindowsDefine("ERROR_DS_GLOBAL_CANT_HAVE_UNIVERSAL_MEMBER",
  sDescription =    "A global group cannot have a universal group as a member.");
fAddWindowsDefine("ERROR_DS_UNIVERSAL_CANT_HAVE_LOCAL_MEMBER",
  sDescription =    "A universal group cannot have a local group as a member.");
fAddWindowsDefine("ERROR_DS_GLOBAL_CANT_HAVE_CROSSDOMAIN_MEMBER",
  sDescription =    "A global group cannot have a cross-domain member.");
fAddWindowsDefine("ERROR_DS_LOCAL_CANT_HAVE_CROSSDOMAIN_LOCAL_MEMBER",
  sDescription =    "A local group cannot have another cross domain local group as a member.");
fAddWindowsDefine("ERROR_DS_HAVE_PRIMARY_MEMBERS",
  sDescription =    "A group with primary members cannot change to a security-disabled group.");
fAddWindowsDefine("ERROR_DS_STRING_SD_CONVERSION_FAILED",
  sDescription =    "The schema cache load failed to convert the string default SD on a class-schema object.");
fAddWindowsDefine("ERROR_DS_NAMING_MASTER_GC",
  sDescription =    "Only DSAs configured to be Global Catalog servers should be allowed to hold the Domain Naming Master FSMO role. (Applies only to Windows 2000 servers)");
fAddWindowsDefine("ERROR_DS_DNS_LOOKUP_FAILURE",
  sDescription =    "The DSA operation is unable to proceed because of a DNS lookup failure.");
fAddWindowsDefine("ERROR_DS_COULDNT_UPDATE_SPNS",
  sDescription =    "While processing a change to the DNS Host Name for an object, the Service Principal Name values could not be kept in sync.");
fAddWindowsDefine("ERROR_DS_CANT_RETRIEVE_SD",
  sDescription =    "The Security Descriptor attribute could not be read.");
fAddWindowsDefine("ERROR_DS_KEY_NOT_UNIQUE",
  sDescription =    "The object requested was not found, but an object with that key was found.");
fAddWindowsDefine("ERROR_DS_WRONG_LINKED_ATT_SYNTAX",
  sDescription =    "The syntax of the linked attribute being added is incorrect. Forward links can only have syntax 2.5.5.1, 2.5.5.7, and 2.5.5.14, and backlinks can only have syntax 2.5.5.1");
fAddWindowsDefine("ERROR_DS_SAM_NEED_BOOTKEY_PASSWORD",
  sDescription =    "Security Account Manager needs to get the boot password.");
fAddWindowsDefine("ERROR_DS_SAM_NEED_BOOTKEY_FLOPPY",
  sDescription =    "Security Account Manager needs to get the boot key from floppy disk.");
fAddWindowsDefine("ERROR_DS_CANT_START",
  sDescription =    "Directory Service cannot start.");
fAddWindowsDefine("ERROR_DS_INIT_FAILURE",
  sDescription =    "Directory Services could not start.");
fAddWindowsDefine("ERROR_DS_NO_PKT_PRIVACY_ON_CONNECTION",
  sDescription =    "The connection between client and server requires packet privacy or better.");
fAddWindowsDefine("ERROR_DS_SOURCE_DOMAIN_IN_FOREST",
  sDescription =    "The source domain may not be in the same forest as destination.");
fAddWindowsDefine("ERROR_DS_DESTINATION_DOMAIN_NOT_IN_FOREST",
  sDescription =    "The destination domain must be in the forest.");
fAddWindowsDefine("ERROR_DS_DESTINATION_AUDITING_NOT_ENABLED",
  sDescription =    "The operation requires that destination domain auditing be enabled.");
fAddWindowsDefine("ERROR_DS_CANT_FIND_DC_FOR_SRC_DOMAIN",
  sDescription =    "The operation couldn't locate a DC for the source domain.");
fAddWindowsDefine("ERROR_DS_SRC_OBJ_NOT_GROUP_OR_USER",
  sDescription =    "The source object must be a group or user.");
fAddWindowsDefine("ERROR_DS_SRC_SID_EXISTS_IN_FOREST",
  sDescription =    "The source object's SID already exists in destination forest.");
fAddWindowsDefine("ERROR_DS_SRC_AND_DST_OBJECT_CLASS_MISMATCH",
  sDescription =    "The source and destination object must be of the same type.");
fAddWindowsDefine("ERROR_SAM_INIT_FAILURE",
  sDescription =    "Security Accounts Manager initialization failed because of the following error: %1. Error Status: 0x%2. Click OK to shut down the system and reboot into Safe Mode. Check the event log for detailed information.");
fAddWindowsDefine("ERROR_DS_DRA_SCHEMA_INFO_SHIP",
  sDescription =    "Schema information could not be included in the replication request.");
fAddWindowsDefine("ERROR_DS_DRA_SCHEMA_CONFLICT",
  sDescription =    "The replication operation could not be completed due to a schema incompatibility.");
fAddWindowsDefine("ERROR_DS_DRA_EARLIER_SCHEMA_CONFLICT",
  sDescription =    "The replication operation could not be completed due to a previous schema incompatibility.");
fAddWindowsDefine("ERROR_DS_DRA_OBJ_NC_MISMATCH",
  sDescription =    "The replication update could not be applied because either the source or the destination has not yet received information regarding a recent cross-domain move operation.");
fAddWindowsDefine("ERROR_DS_NC_STILL_HAS_DSAS",
  sDescription =    "The requested domain could not be deleted because there exist domain controllers that still host this domain.");
fAddWindowsDefine("ERROR_DS_GC_REQUIRED",
  sDescription =    "The requested operation can be performed only on a global catalog server.");
fAddWindowsDefine("ERROR_DS_LOCAL_MEMBER_OF_LOCAL_ONLY",
  sDescription =    "A local group can only be a member of other local groups in the same domain.");
fAddWindowsDefine("ERROR_DS_NO_FPO_IN_UNIVERSAL_GROUPS",
  sDescription =    "Foreign security principals cannot be members of universal groups.");
fAddWindowsDefine("ERROR_DS_CANT_ADD_TO_GC",
  sDescription =    "The attribute is not allowed to be replicated to the GC because of security reasons.");
fAddWindowsDefine("ERROR_DS_NO_CHECKPOINT_WITH_PDC",
  sDescription =    "The checkpoint with the PDC could not be taken because there too many modifications being processed currently.");
fAddWindowsDefine("ERROR_DS_SOURCE_AUDITING_NOT_ENABLED",
  sDescription =    "The operation requires that source domain auditing be enabled.");
fAddWindowsDefine("ERROR_DS_CANT_CREATE_IN_NONDOMAIN_NC",
  sDescription =    "Security principal objects can only be created inside domain naming contexts.");
fAddWindowsDefine("ERROR_DS_INVALID_NAME_FOR_SPN",
  sDescription =    "A Service Principal Name (SPN) could not be constructed because the provided hostname is not in the necessary format.");
fAddWindowsDefine("ERROR_DS_FILTER_USES_CONTRUCTED_ATTRS",
  sDescription =    "A Filter was passed that uses constructed attributes.");
fAddWindowsDefine("ERROR_DS_UNICODEPWD_NOT_IN_QUOTES",
  sDescription =    "The unicodePwd attribute value must be enclosed in double quotes.");
fAddWindowsDefine("ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED",
  sDescription =    "Your computer could not be joined to the domain. You have exceeded the maximum number of computer accounts you are allowed to create in this domain. Contact your system administrator to have this limit reset or increased.");
fAddWindowsDefine("ERROR_DS_MUST_BE_RUN_ON_DST_DC",
  sDescription =    "For security reasons, the operation must be run on the destination DC.");
fAddWindowsDefine("ERROR_DS_SRC_DC_MUST_BE_SP4_OR_GREATER",
  sDescription =    "For security reasons, the source DC must be NT4SP4 or greater.");
fAddWindowsDefine("ERROR_DS_CANT_TREE_DELETE_CRITICAL_OBJ",
  sDescription =    "Critical Directory Service System objects cannot be deleted during tree delete operations. The tree delete may have been partially performed.");
fAddWindowsDefine("ERROR_DS_INIT_FAILURE_CONSOLE",
  sDescription =    "Directory Services could not start because of the following error: %1. Error Status: 0x%2. Please click OK to shutdown the system. You can use the recovery console to diagnose the system further.");
fAddWindowsDefine("ERROR_DS_SAM_INIT_FAILURE_CONSOLE",
  sDescription =    "Security Accounts Manager initialization failed because of the following error: %1. Error Status: 0x%2. Please click OK to shutdown the system. You can use the recovery console to diagnose the system further.");
fAddWindowsDefine("ERROR_DS_FOREST_VERSION_TOO_HIGH",
  sDescription =    "The version of the operating system is incompatible with the current AD DS forest functional level or AD LDS Configuration Set functional level. You must upgrade to a new version of the operating system before this server can become an AD DS Domain Controller or add an AD LDS Instance in this AD DS Forest or AD LDS Configuration Set.");
fAddWindowsDefine("ERROR_DS_DOMAIN_VERSION_TOO_HIGH",
  sDescription =    "The version of the operating system installed is incompatible with the current domain functional level. You must upgrade to a new version of the operating system before this server can become a domain controller in this domain.");
fAddWindowsDefine("ERROR_DS_FOREST_VERSION_TOO_LOW",
  sDescription =    "The version of the operating system installed on this server no longer supports the current AD DS Forest functional level or AD LDS Configuration Set functional level. You must raise the AD DS Forest functional level or AD LDS Configuration Set functional level before this server can become an AD DS Domain Controller or an AD LDS Instance in this Forest or Configuration Set.");
fAddWindowsDefine("ERROR_DS_DOMAIN_VERSION_TOO_LOW",
  sDescription =    "The version of the operating system installed on this server no longer supports the current domain functional level. You must raise the domain functional level before this server can become a domain controller in this domain.");
fAddWindowsDefine("ERROR_DS_INCOMPATIBLE_VERSION",
  sDescription =    "The version of the operating system installed on this server is incompatible with the functional level of the domain or forest.");
fAddWindowsDefine("ERROR_DS_LOW_DSA_VERSION",
  sDescription =    "The functional level of the domain (or forest) cannot be raised to the requested value, because there exist one or more domain controllers in the domain (or forest) that are at a lower incompatible functional level.");
fAddWindowsDefine("ERROR_DS_NO_BEHAVIOR_VERSION_IN_MIXEDDOMAIN",
  sDescription =    "The forest functional level cannot be raised to the requested value since one or more domains are still in mixed domain mode. All domains in the forest must be in native mode, for you to raise the forest functional level.");
fAddWindowsDefine("ERROR_DS_NOT_SUPPORTED_SORT_ORDER",
  sDescription =    "The sort order requested is not supported.");
fAddWindowsDefine("ERROR_DS_NAME_NOT_UNIQUE",
  sDescription =    "The requested name already exists as a unique identifier.");
fAddWindowsDefine("ERROR_DS_MACHINE_ACCOUNT_CREATED_PRENT4",
  sDescription =    "The machine account was created pre-NT4. The account needs to be recreated.");
fAddWindowsDefine("ERROR_DS_OUT_OF_VERSION_STORE",
  sDescription =    "The database is out of version store.");
fAddWindowsDefine("ERROR_DS_INCOMPATIBLE_CONTROLS_USED",
  sDescription =    "Unable to continue operation because multiple conflicting controls were used.");
fAddWindowsDefine("ERROR_DS_NO_REF_DOMAIN",
  sDescription =    "Unable to find a valid security descriptor reference domain for this partition.");
fAddWindowsDefine("ERROR_DS_RESERVED_LINK_ID",
  sDescription =    "Schema update failed: The link identifier is reserved.");
fAddWindowsDefine("ERROR_DS_LINK_ID_NOT_AVAILABLE",
  sDescription =    "Schema update failed: There are no link identifiers available.");
fAddWindowsDefine("ERROR_DS_AG_CANT_HAVE_UNIVERSAL_MEMBER",
  sDescription =    "An account group cannot have a universal group as a member.");
fAddWindowsDefine("ERROR_DS_MODIFYDN_DISALLOWED_BY_INSTANCE_TYPE",
  sDescription =    "Rename or move operations on naming context heads or read-only objects are not allowed.");
fAddWindowsDefine("ERROR_DS_NO_OBJECT_MOVE_IN_SCHEMA_NC",
  sDescription =    "Move operations on objects in the schema naming context are not allowed.");
fAddWindowsDefine("ERROR_DS_MODIFYDN_DISALLOWED_BY_FLAG",
  sDescription =    "A system flag has been set on the object and does not allow the object to be moved or renamed.");
fAddWindowsDefine("ERROR_DS_MODIFYDN_WRONG_GRANDPARENT",
  sDescription =    "This object is not allowed to change its grandparent container. Moves are not forbidden on this object, but are restricted to sibling containers.");
fAddWindowsDefine("ERROR_DS_NAME_ERROR_TRUST_REFERRAL",
  sDescription =    "Unable to resolve completely, a referral to another forest is generated.");
fAddWindowsDefine("ERROR_NOT_SUPPORTED_ON_STANDARD_SERVER",
  sDescription =    "The requested action is not supported on standard server.");
fAddWindowsDefine("ERROR_DS_CANT_ACCESS_REMOTE_PART_OF_AD",
  sDescription =    "Could not access a partition of the directory service located on a remote server. Make sure at least one server is running for the partition in question.");
fAddWindowsDefine("ERROR_DS_CR_IMPOSSIBLE_TO_VALIDATE_V2",
  sDescription =    "The directory cannot validate the proposed naming context (or partition) name because it does not hold a replica nor can it contact a replica of the naming context above the proposed naming context. Please ensure that the parent naming context is properly registered in DNS, and at least one replica of this naming context is reachable by the Domain Naming master.");
fAddWindowsDefine("ERROR_DS_THREAD_LIMIT_EXCEEDED",
  sDescription =    "The thread limit for this request was exceeded.");
fAddWindowsDefine("ERROR_DS_NOT_CLOSEST",
  sDescription =    "The Global catalog server is not in the closest site.");
fAddWindowsDefine("ERROR_DS_CANT_DERIVE_SPN_WITHOUT_SERVER_REF",
  sDescription =    "The DS cannot derive a service principal name (SPN) with which to mutually authenticate the target server because the corresponding server object in the local DS database has no serverReference attribute.");
fAddWindowsDefine("ERROR_DS_SINGLE_USER_MODE_FAILED",
  sDescription =    "The Directory Service failed to enter single user mode.");
fAddWindowsDefine("ERROR_DS_NTDSCRIPT_SYNTAX_ERROR",
  sDescription =    "The Directory Service cannot parse the script because of a syntax error.");
fAddWindowsDefine("ERROR_DS_NTDSCRIPT_PROCESS_ERROR",
  sDescription =    "The Directory Service cannot process the script because of an error.");
fAddWindowsDefine("ERROR_DS_DIFFERENT_REPL_EPOCHS",
  sDescription =    "The directory service cannot perform the requested operation because the servers involved are of different replication epochs (which is usually related to a domain rename that is in progress).");
fAddWindowsDefine("ERROR_DS_DRS_EXTENSIONS_CHANGED",
  sDescription =    "The directory service binding must be renegotiated due to a change in the server extensions information.");
fAddWindowsDefine("ERROR_DS_REPLICA_SET_CHANGE_NOT_ALLOWED_ON_DISABLED_CR",
  sDescription =    "Operation not allowed on a disabled cross ref.");
fAddWindowsDefine("ERROR_DS_NO_MSDS_INTID",
  sDescription =    "Schema update failed: No values for msDS-IntId are available.");
fAddWindowsDefine("ERROR_DS_DUP_MSDS_INTID",
  sDescription =    "Schema update failed: Duplicate msDS-INtId. Retry the operation.");
fAddWindowsDefine("ERROR_DS_EXISTS_IN_RDNATTID",
  sDescription =    "Schema deletion failed: attribute is used in rDNAttID.");
fAddWindowsDefine("ERROR_DS_AUTHORIZATION_FAILED",
  sDescription =    "The directory service failed to authorize the request.");
fAddWindowsDefine("ERROR_DS_INVALID_SCRIPT",
  sDescription =    "The Directory Service cannot process the script because it is invalid.");
fAddWindowsDefine("ERROR_DS_REMOTE_CROSSREF_OP_FAILED",
  sDescription =    "The remote create cross reference operation failed on the Domain Naming Master FSMO. The operation's error is in the extended data.");
fAddWindowsDefine("ERROR_DS_CROSS_REF_BUSY",
  sDescription =    "A cross reference is in use locally with the same name.");
fAddWindowsDefine("ERROR_DS_CANT_DERIVE_SPN_FOR_DELETED_DOMAIN",
  sDescription =    "The DS cannot derive a service principal name (SPN) with which to mutually authenticate the target server because the server's domain has been deleted from the forest.");
fAddWindowsDefine("ERROR_DS_CANT_DEMOTE_WITH_WRITEABLE_NC",
  sDescription =    "Writeable NCs prevent this DC from demoting.");
fAddWindowsDefine("ERROR_DS_DUPLICATE_ID_FOUND",
  sDescription =    "The requested object has a non-unique identifier and cannot be retrieved.");
fAddWindowsDefine("ERROR_DS_INSUFFICIENT_ATTR_TO_CREATE_OBJECT",
  sDescription =    "Insufficient attributes were given to create an object. This object may not exist because it may have been deleted and already garbage collected.");
fAddWindowsDefine("ERROR_DS_GROUP_CONVERSION_ERROR",
  sDescription =    "The group cannot be converted due to attribute restrictions on the requested group type.");
fAddWindowsDefine("ERROR_DS_CANT_MOVE_APP_BASIC_GROUP",
  sDescription =    "Cross-domain move of non-empty basic application groups is not allowed.");
fAddWindowsDefine("ERROR_DS_CANT_MOVE_APP_QUERY_GROUP",
  sDescription =    "Cross-domain move of non-empty query based application groups is not allowed.");
fAddWindowsDefine("ERROR_DS_ROLE_NOT_VERIFIED",
  sDescription =    "The FSMO role ownership could not be verified because its directory partition has not replicated successfully with at least one replication partner.");
fAddWindowsDefine("ERROR_DS_WKO_CONTAINER_CANNOT_BE_SPECIAL",
  sDescription =    "The target container for a redirection of a well known object container cannot already be a special container.");
fAddWindowsDefine("ERROR_DS_DOMAIN_RENAME_IN_PROGRESS",
  sDescription =    "The Directory Service cannot perform the requested operation because a domain rename operation is in progress.");
fAddWindowsDefine("ERROR_DS_EXISTING_AD_CHILD_NC",
  sDescription =    "The directory service detected a child partition below the requested partition name. The partition hierarchy must be created in a top down method.");
fAddWindowsDefine("ERROR_DS_REPL_LIFETIME_EXCEEDED",
  sDescription =    "The directory service cannot replicate with this server because the time since the last replication with this server has exceeded the tombstone lifetime.");
fAddWindowsDefine("ERROR_DS_DISALLOWED_IN_SYSTEM_CONTAINER",
  sDescription =    "The requested operation is not allowed on an object under the system container.");
fAddWindowsDefine("ERROR_DS_LDAP_SEND_QUEUE_FULL",
  sDescription =    "The LDAP servers network send queue has filled up because the client is not processing the results of its requests fast enough. No more requests will be processed until the client catches up. If the client does not catch up then it will be disconnected.");
fAddWindowsDefine("ERROR_DS_DRA_OUT_SCHEDULE_WINDOW",
  sDescription =    "The scheduled replication did not take place because the system was too busy to execute the request within the schedule window. The replication queue is overloaded. Consider reducing the number of partners or decreasing the scheduled replication frequency.");
fAddWindowsDefine("ERROR_DS_POLICY_NOT_KNOWN",
  sDescription =    "At this time, it cannot be determined if the branch replication policy is available on the hub domain controller. Please retry at a later time to account for replication latencies.");
fAddWindowsDefine("ERROR_NO_SITE_SETTINGS_OBJECT",
  sDescription =    "The site settings object for the specified site does not exist.");
fAddWindowsDefine("ERROR_NO_SECRETS",
  sDescription =    "The local account store does not contain secret material for the specified account.");
fAddWindowsDefine("ERROR_NO_WRITABLE_DC_FOUND",
  sDescription =    "Could not find a writable domain controller in the domain.");
fAddWindowsDefine("ERROR_DS_NO_SERVER_OBJECT",
  sDescription =    "The server object for the domain controller does not exist.");
fAddWindowsDefine("ERROR_DS_NO_NTDSA_OBJECT",
  sDescription =    "The NTDS Settings object for the domain controller does not exist.");
fAddWindowsDefine("ERROR_DS_NON_ASQ_SEARCH",
  sDescription =    "The requested search operation is not supported for ASQ searches.");
fAddWindowsDefine("ERROR_DS_AUDIT_FAILURE",
  sDescription =    "A required audit event could not be generated for the operation.");
fAddWindowsDefine("ERROR_DS_INVALID_SEARCH_FLAG_SUBTREE",
  sDescription =    "The search flags for the attribute are invalid. The subtree index bit is valid only on single valued attributes.");
fAddWindowsDefine("ERROR_DS_INVALID_SEARCH_FLAG_TUPLE",
  sDescription =    "The search flags for the attribute are invalid. The tuple index bit is valid only on attributes of Unicode strings.");
fAddWindowsDefine("ERROR_DS_HIERARCHY_TABLE_TOO_DEEP",
  sDescription =    "The address books are nested too deeply. Failed to build the hierarchy table.");
fAddWindowsDefine("ERROR_DS_DRA_CORRUPT_UTD_VECTOR",
  sDescription =    "The specified up-to-date-ness vector is corrupt.");
fAddWindowsDefine("ERROR_DS_DRA_SECRETS_DENIED",
  sDescription =    "The request to replicate secrets is denied.");
fAddWindowsDefine("ERROR_DS_RESERVED_MAPI_ID",
  sDescription =    "Schema update failed: The MAPI identifier is reserved.");
fAddWindowsDefine("ERROR_DS_MAPI_ID_NOT_AVAILABLE",
  sDescription =    "Schema update failed: There are no MAPI identifiers available.");
fAddWindowsDefine("ERROR_DS_DRA_MISSING_KRBTGT_SECRET",
  sDescription =    "The replication operation failed because the required attributes of the local krbtgt object are missing.");
fAddWindowsDefine("ERROR_DS_DOMAIN_NAME_EXISTS_IN_FOREST",
  sDescription =    "The domain name of the trusted domain already exists in the forest.");
fAddWindowsDefine("ERROR_DS_FLAT_NAME_EXISTS_IN_FOREST",
  sDescription =    "The flat name of the trusted domain already exists in the forest.");
fAddWindowsDefine("ERROR_INVALID_USER_PRINCIPAL_NAME",
  sDescription =    "The User Principal Name (UPN) is invalid.");
fAddWindowsDefine("ERROR_DS_OID_MAPPED_GROUP_CANT_HAVE_MEMBERS",
  sDescription =    "OID mapped groups cannot have members.");
fAddWindowsDefine("ERROR_DS_OID_NOT_FOUND",
  sDescription =    "The specified OID cannot be found.");
fAddWindowsDefine("ERROR_DS_DRA_RECYCLED_TARGET",
  sDescription =    "The replication operation failed because the target object referred by a link value is recycled.");
fAddWindowsDefine("ERROR_DS_DISALLOWED_NC_REDIRECT",
  sDescription =    "The redirect operation failed because the target object is in a NC different from the domain NC of the current domain controller.");
fAddWindowsDefine("ERROR_DS_HIGH_ADLDS_FFL",
  sDescription =    "The functional level of the AD LDS configuration set cannot be lowered to the requested value.");
fAddWindowsDefine("ERROR_DS_HIGH_DSA_VERSION",
  sDescription =    "The functional level of the domain (or forest) cannot be lowered to the requested value.");
fAddWindowsDefine("ERROR_DS_LOW_ADLDS_FFL",
  sDescription =    "The functional level of the AD LDS configuration set cannot be raised to the requested value, because there exist one or more ADLDS instances that are at a lower incompatible functional level.");
fAddWindowsDefine("ERROR_DOMAIN_SID_SAME_AS_LOCAL_WORKSTATION",
  sDescription =    "The domain join cannot be completed because the SID of the domain you attempted to join was identical to the SID of this machine. This is a symptom of an improperly cloned operating system install. You should run sysprep on this machine in order to generate a new machine SID. Please see http://go.microsoft.com/fwlink/?LinkId=168895 for more information.");
fAddWindowsDefine("ERROR_DS_UNDELETE_SAM_VALIDATION_FAILED",
  sDescription =    "The undelete operation failed because the Sam Account Name or Additional Sam Account Name of the object being undeleted conflicts with an existing live object.");
fAddWindowsDefine("ERROR_INCORRECT_ACCOUNT_TYPE",
  sDescription =    "The system is not authoritative for the specified account and therefore cannot complete the operation. Please retry the operation using the provider associated with this account. If this is an online provider please use the provider's online site.");
fAddWindowsDefine("ERROR_DS_SPN_VALUE_NOT_UNIQUE_IN_FOREST",
  sDescription =    "The operation failed because SPN value provided for addition/modification is not unique forest-wide.");
fAddWindowsDefine("ERROR_DS_UPN_VALUE_NOT_UNIQUE_IN_FOREST",
  sDescription =    "The operation failed because UPN value provided for addition/modification is not unique forest-wide.");
fAddWindowsDefine("ERROR_DS_MISSING_FOREST_TRUST",
  sDescription =    "The operation failed because the addition/modification referenced an inbound forest-wide trust that is not present.");
fAddWindowsDefine("ERROR_DS_VALUE_KEY_NOT_UNIQUE",
  sDescription =    "The link value specified was not found, but a link value with that key was found.");
fAddWindowsDefine("DNS_ERROR_RCODE_FORMAT_ERROR",
  sDescription =    "DNS server unable to interpret format.");
fAddWindowsDefine("DNS_ERROR_RCODE_SERVER_FAILURE",
  sDescription =    "DNS server failure.");
fAddWindowsDefine("DNS_ERROR_RCODE_NAME_ERROR",
  sDescription =    "DNS name does not exist.");
fAddWindowsDefine("DNS_ERROR_RCODE_NOT_IMPLEMENTED",
  sDescription =    "DNS request not supported by name server.");
fAddWindowsDefine("DNS_ERROR_RCODE_REFUSED",
  sDescription =    "DNS operation refused.");
fAddWindowsDefine("DNS_ERROR_RCODE_YXDOMAIN",
  sDescription =    "DNS name that ought not exist, does exist.");
fAddWindowsDefine("DNS_ERROR_RCODE_YXRRSET",
  sDescription =    "DNS RR set that ought not exist, does exist.");
fAddWindowsDefine("DNS_ERROR_RCODE_NXRRSET",
  sDescription =    "DNS RR set that ought to exist, does not exist.");
fAddWindowsDefine("DNS_ERROR_RCODE_NOTAUTH",
  sDescription =    "DNS server not authoritative for zone.");
fAddWindowsDefine("DNS_ERROR_RCODE_NOTZONE",
  sDescription =    "DNS name in update or prereq is not in zone.");
fAddWindowsDefine("DNS_ERROR_RCODE_BADSIG",
  sDescription =    "DNS signature failed to verify.");
fAddWindowsDefine("DNS_ERROR_RCODE_BADKEY",
  sDescription =    "DNS bad key.");
fAddWindowsDefine("DNS_ERROR_RCODE_BADTIME",
  sDescription =    "DNS signature validity expired.");
fAddWindowsDefine("DNS_ERROR_KEYMASTER_REQUIRED",
  sDescription =    "Only the DNS server acting as the key master for the zone may perform this operation.");
fAddWindowsDefine("DNS_ERROR_NOT_ALLOWED_ON_SIGNED_ZONE",
  sDescription =    "This operation is not allowed on a zone that is signed or has signing keys.");
fAddWindowsDefine("DNS_ERROR_NSEC3_INCOMPATIBLE_WITH_RSA_SHA1",
  sDescription =    "NSEC3 is not compatible with the RSA-SHA-1 algorithm. Choose a different algorithm or use NSEC.");
fAddWindowsDefine("DNS_ERROR_NOT_ENOUGH_SIGNING_KEY_DESCRIPTORS",
  sDescription =    "The zone does not have enough signing keys. There must be at least one key signing key (KSK) and at least one zone signing key (ZSK).");
fAddWindowsDefine("DNS_ERROR_UNSUPPORTED_ALGORITHM",
  sDescription =    "The specified algorithm is not supported.");
fAddWindowsDefine("DNS_ERROR_INVALID_KEY_SIZE",
  sDescription =    "The specified key size is not supported.");
fAddWindowsDefine("DNS_ERROR_SIGNING_KEY_NOT_ACCESSIBLE",
  sDescription =    "One or more of the signing keys for a zone are not accessible to the DNS server. Zone signing will not be operational until this error is resolved.");
fAddWindowsDefine("DNS_ERROR_KSP_DOES_NOT_SUPPORT_PROTECTION",
  sDescription =    "The specified key storage provider does not support DPAPI++ data protection. Zone signing will not be operational until this error is resolved.");
fAddWindowsDefine("DNS_ERROR_UNEXPECTED_DATA_PROTECTION_ERROR",
  sDescription =    "An unexpected DPAPI++ error was encountered. Zone signing will not be operational until this error is resolved.");
fAddWindowsDefine("DNS_ERROR_UNEXPECTED_CNG_ERROR",
  sDescription =    "An unexpected crypto error was encountered. Zone signing may not be operational until this error is resolved.");
fAddWindowsDefine("DNS_ERROR_UNKNOWN_SIGNING_PARAMETER_VERSION",
  sDescription =    "The DNS server encountered a signing key with an unknown version. Zone signing will not be operational until this error is resolved.");
fAddWindowsDefine("DNS_ERROR_KSP_NOT_ACCESSIBLE",
  sDescription =    "The specified key service provider cannot be opened by the DNS server.");
fAddWindowsDefine("DNS_ERROR_TOO_MANY_SKDS",
  sDescription =    "The DNS server cannot accept any more signing keys with the specified algorithm and KSK flag value for this zone.");
fAddWindowsDefine("DNS_ERROR_INVALID_ROLLOVER_PERIOD",
  sDescription =    "The specified rollover period is invalid.");
fAddWindowsDefine("DNS_ERROR_INVALID_INITIAL_ROLLOVER_OFFSET",
  sDescription =    "The specified initial rollover offset is invalid.");
fAddWindowsDefine("DNS_ERROR_ROLLOVER_IN_PROGRESS",
  sDescription =    "The specified signing key is already in process of rolling over keys.");
fAddWindowsDefine("DNS_ERROR_STANDBY_KEY_NOT_PRESENT",
  sDescription =    "The specified signing key does not have a standby key to revoke.");
fAddWindowsDefine("DNS_ERROR_NOT_ALLOWED_ON_ZSK",
  sDescription =    "This operation is not allowed on a zone signing key (ZSK).");
fAddWindowsDefine("DNS_ERROR_NOT_ALLOWED_ON_ACTIVE_SKD",
  sDescription =    "This operation is not allowed on an active signing key.");
fAddWindowsDefine("DNS_ERROR_ROLLOVER_ALREADY_QUEUED",
  sDescription =    "The specified signing key is already queued for rollover.");
fAddWindowsDefine("DNS_ERROR_NOT_ALLOWED_ON_UNSIGNED_ZONE",
  sDescription =    "This operation is not allowed on an unsigned zone.");
fAddWindowsDefine("DNS_ERROR_BAD_KEYMASTER",
  sDescription =    "This operation could not be completed because the DNS server listed as the current key master for this zone is down or misconfigured. Resolve the problem on the current key master for this zone or use another DNS server to seize the key master role.");
fAddWindowsDefine("DNS_ERROR_INVALID_SIGNATURE_VALIDITY_PERIOD",
  sDescription =    "The specified signature validity period is invalid.");
fAddWindowsDefine("DNS_ERROR_INVALID_NSEC3_ITERATION_COUNT",
  sDescription =    "The specified NSEC3 iteration count is higher than allowed by the minimum key length used in the zone.");
fAddWindowsDefine("DNS_ERROR_DNSSEC_IS_DISABLED",
  sDescription =    "This operation could not be completed because the DNS server has been configured with DNSSEC features disabled. Enable DNSSEC on the DNS server.");
fAddWindowsDefine("DNS_ERROR_INVALID_XML",
  sDescription =    "This operation could not be completed because the XML stream received is empty or syntactically invalid.");
fAddWindowsDefine("DNS_ERROR_NO_VALID_TRUST_ANCHORS",
  sDescription =    "This operation completed, but no trust anchors were added because all of the trust anchors received were either invalid, unsupported, expired, or would not become valid in less than 30 days.");
fAddWindowsDefine("DNS_ERROR_ROLLOVER_NOT_POKEABLE",
  sDescription =    "The specified signing key is not waiting for parental DS update.");
fAddWindowsDefine("DNS_ERROR_NSEC3_NAME_COLLISION",
  sDescription =    "Hash collision detected during NSEC3 signing. Specify a different user-provided salt, or use a randomly generated salt, and attempt to sign the zone again.");
fAddWindowsDefine("DNS_ERROR_NSEC_INCOMPATIBLE_WITH_NSEC3_RSA_SHA1",
  sDescription =    "NSEC is not compatible with the NSEC3-RSA-SHA-1 algorithm. Choose a different algorithm or use NSEC3.");
fAddWindowsDefine("DNS_INFO_NO_RECORDS",
  sDescription =    "No records found for given DNS query.");
fAddWindowsDefine("DNS_ERROR_BAD_PACKET",
  sDescription =    "Bad DNS packet.");
fAddWindowsDefine("DNS_ERROR_NO_PACKET",
  sDescription =    "No DNS packet.");
fAddWindowsDefine("DNS_ERROR_RCODE",
  sDescription =    "DNS error, check rcode.");
fAddWindowsDefine("DNS_ERROR_UNSECURE_PACKET",
  sDescription =    "Unsecured DNS packet.");
fAddWindowsDefine("DNS_REQUEST_PENDING",
  sDescription =    "DNS query request is pending.");
fAddWindowsDefine("DNS_ERROR_INVALID_TYPE",
  sDescription =    "Invalid DNS type.");
fAddWindowsDefine("DNS_ERROR_INVALID_IP_ADDRESS",
  sDescription =    "Invalid IP address.");
fAddWindowsDefine("DNS_ERROR_INVALID_PROPERTY",
  sDescription =    "Invalid property.");
fAddWindowsDefine("DNS_ERROR_TRY_AGAIN_LATER",
  sDescription =    "Try DNS operation again later.");
fAddWindowsDefine("DNS_ERROR_NOT_UNIQUE",
  sDescription =    "Record for given name and type is not unique.");
fAddWindowsDefine("DNS_ERROR_NON_RFC_NAME",
  sDescription =    "DNS name does not comply with RFC specifications.");
fAddWindowsDefine("DNS_STATUS_FQDN",
  sDescription =    "DNS name is a fully-qualified DNS name.");
fAddWindowsDefine("DNS_STATUS_DOTTED_NAME",
  sDescription =    "DNS name is dotted (multi-label).");
fAddWindowsDefine("DNS_STATUS_SINGLE_PART_NAME",
  sDescription =    "DNS name is a single-part name.");
fAddWindowsDefine("DNS_ERROR_INVALID_NAME_CHAR",
  sDescription =    "DNS name contains an invalid character.");
fAddWindowsDefine("DNS_ERROR_NUMERIC_NAME",
  sDescription =    "DNS name is entirely numeric.");
fAddWindowsDefine("DNS_ERROR_NOT_ALLOWED_ON_ROOT_SERVER",
  sDescription =    "The operation requested is not permitted on a DNS root server.");
fAddWindowsDefine("DNS_ERROR_NOT_ALLOWED_UNDER_DELEGATION",
  sDescription =    "The record could not be created because this part of the DNS namespace has been delegated to another server.");
fAddWindowsDefine("DNS_ERROR_CANNOT_FIND_ROOT_HINTS",
  sDescription =    "The DNS server could not find a set of root hints.");
fAddWindowsDefine("DNS_ERROR_INCONSISTENT_ROOT_HINTS",
  sDescription =    "The DNS server found root hints but they were not consistent across all adapters.");
fAddWindowsDefine("DNS_ERROR_DWORD_VALUE_TOO_SMALL",
  sDescription =    "The specified value is too small for this parameter.");
fAddWindowsDefine("DNS_ERROR_DWORD_VALUE_TOO_LARGE",
  sDescription =    "The specified value is too large for this parameter.");
fAddWindowsDefine("DNS_ERROR_BACKGROUND_LOADING",
  sDescription =    "This operation is not allowed while the DNS server is loading zones in the background. Please try again later.");
fAddWindowsDefine("DNS_ERROR_NOT_ALLOWED_ON_RODC",
  sDescription =    "The operation requested is not permitted on against a DNS server running on a read-only DC.");
fAddWindowsDefine("DNS_ERROR_NOT_ALLOWED_UNDER_DNAME",
  sDescription =    "No data is allowed to exist underneath a DNAME record.");
fAddWindowsDefine("DNS_ERROR_DELEGATION_REQUIRED",
  sDescription =    "This operation requires credentials delegation.");
fAddWindowsDefine("DNS_ERROR_INVALID_POLICY_TABLE",
  sDescription =    "Name resolution policy table has been corrupted. DNS resolution will fail until it is fixed. Contact your network administrator.");
fAddWindowsDefine("DNS_ERROR_ADDRESS_REQUIRED",
  sDescription =    "Not allowed to remove all addresses.");
fAddWindowsDefine("DNS_ERROR_ZONE_DOES_NOT_EXIST",
  sDescription =    "DNS zone does not exist.");
fAddWindowsDefine("DNS_ERROR_NO_ZONE_INFO",
  sDescription =    "DNS zone information not available.");
fAddWindowsDefine("DNS_ERROR_INVALID_ZONE_OPERATION",
  sDescription =    "Invalid operation for DNS zone.");
fAddWindowsDefine("DNS_ERROR_ZONE_CONFIGURATION_ERROR",
  sDescription =    "Invalid DNS zone configuration.");
fAddWindowsDefine("DNS_ERROR_ZONE_HAS_NO_SOA_RECORD",
  sDescription =    "DNS zone has no start of authority (SOA) record.");
fAddWindowsDefine("DNS_ERROR_ZONE_HAS_NO_NS_RECORDS",
  sDescription =    "DNS zone has no Name Server (NS) record.");
fAddWindowsDefine("DNS_ERROR_ZONE_LOCKED",
  sDescription =    "DNS zone is locked.");
fAddWindowsDefine("DNS_ERROR_ZONE_CREATION_FAILED",
  sDescription =    "DNS zone creation failed.");
fAddWindowsDefine("DNS_ERROR_ZONE_ALREADY_EXISTS",
  sDescription =    "DNS zone already exists.");
fAddWindowsDefine("DNS_ERROR_AUTOZONE_ALREADY_EXISTS",
  sDescription =    "DNS automatic zone already exists.");
fAddWindowsDefine("DNS_ERROR_INVALID_ZONE_TYPE",
  sDescription =    "Invalid DNS zone type.");
fAddWindowsDefine("DNS_ERROR_SECONDARY_REQUIRES_MASTER_IP",
  sDescription =    "Secondary DNS zone requires master IP address.");
fAddWindowsDefine("DNS_ERROR_ZONE_NOT_SECONDARY",
  sDescription =    "DNS zone not secondary.");
fAddWindowsDefine("DNS_ERROR_NEED_SECONDARY_ADDRESSES",
  sDescription =    "Need secondary IP address.");
fAddWindowsDefine("DNS_ERROR_WINS_INIT_FAILED",
  sDescription =    "WINS initialization failed.");
fAddWindowsDefine("DNS_ERROR_NEED_WINS_SERVERS",
  sDescription =    "Need WINS servers.");
fAddWindowsDefine("DNS_ERROR_NBSTAT_INIT_FAILED",
  sDescription =    "NBTSTAT initialization call failed.");
fAddWindowsDefine("DNS_ERROR_SOA_DELETE_INVALID",
  sDescription =    "Invalid delete of start of authority (SOA)");
fAddWindowsDefine("DNS_ERROR_FORWARDER_ALREADY_EXISTS",
  sDescription =    "A conditional forwarding zone already exists for that name.");
fAddWindowsDefine("DNS_ERROR_ZONE_REQUIRES_MASTER_IP",
  sDescription =    "This zone must be configured with one or more master DNS server IP addresses.");
fAddWindowsDefine("DNS_ERROR_ZONE_IS_SHUTDOWN",
  sDescription =    "The operation cannot be performed because this zone is shut down.");
fAddWindowsDefine("DNS_ERROR_ZONE_LOCKED_FOR_SIGNING",
  sDescription =    "This operation cannot be performed because the zone is currently being signed. Please try again later.");
fAddWindowsDefine("DNS_ERROR_PRIMARY_REQUIRES_DATAFILE",
  sDescription =    "Primary DNS zone requires datafile.");
fAddWindowsDefine("DNS_ERROR_INVALID_DATAFILE_NAME",
  sDescription =    "Invalid datafile name for DNS zone.");
fAddWindowsDefine("DNS_ERROR_DATAFILE_OPEN_FAILURE",
  sDescription =    "Failed to open datafile for DNS zone.");
fAddWindowsDefine("DNS_ERROR_FILE_WRITEBACK_FAILED",
  sDescription =    "Failed to write datafile for DNS zone.");
fAddWindowsDefine("DNS_ERROR_DATAFILE_PARSING",
  sDescription =    "Failure while reading datafile for DNS zone.");
fAddWindowsDefine("DNS_ERROR_RECORD_DOES_NOT_EXIST",
  sDescription =    "DNS record does not exist.");
fAddWindowsDefine("DNS_ERROR_RECORD_FORMAT",
  sDescription =    "DNS record format error.");
fAddWindowsDefine("DNS_ERROR_NODE_CREATION_FAILED",
  sDescription =    "Node creation failure in DNS.");
fAddWindowsDefine("DNS_ERROR_UNKNOWN_RECORD_TYPE",
  sDescription =    "Unknown DNS record type.");
fAddWindowsDefine("DNS_ERROR_RECORD_TIMED_OUT",
  sDescription =    "DNS record timed out.");
fAddWindowsDefine("DNS_ERROR_NAME_NOT_IN_ZONE",
  sDescription =    "Name not in DNS zone.");
fAddWindowsDefine("DNS_ERROR_CNAME_LOOP",
  sDescription =    "CNAME loop detected.");
fAddWindowsDefine("DNS_ERROR_NODE_IS_CNAME",
  sDescription =    "Node is a CNAME DNS record.");
fAddWindowsDefine("DNS_ERROR_CNAME_COLLISION",
  sDescription =    "A CNAME record already exists for given name.");
fAddWindowsDefine("DNS_ERROR_RECORD_ONLY_AT_ZONE_ROOT",
  sDescription =    "Record only at DNS zone root.");
fAddWindowsDefine("DNS_ERROR_RECORD_ALREADY_EXISTS",
  sDescription =    "DNS record already exists.");
fAddWindowsDefine("DNS_ERROR_SECONDARY_DATA",
  sDescription =    "Secondary DNS zone data error.");
fAddWindowsDefine("DNS_ERROR_NO_CREATE_CACHE_DATA",
  sDescription =    "Could not create DNS cache data.");
fAddWindowsDefine("DNS_ERROR_NAME_DOES_NOT_EXIST",
  sDescription =    "DNS name does not exist.");
fAddWindowsDefine("DNS_WARNING_PTR_CREATE_FAILED",
  sDescription =    "Could not create pointer (PTR) record.");
fAddWindowsDefine("DNS_WARNING_DOMAIN_UNDELETED",
  sDescription =    "DNS domain was undeleted.");
fAddWindowsDefine("DNS_ERROR_DS_UNAVAILABLE",
  sDescription =    "The directory service is unavailable.");
fAddWindowsDefine("DNS_ERROR_DS_ZONE_ALREADY_EXISTS",
  sDescription =    "DNS zone already exists in the directory service.");
fAddWindowsDefine("DNS_ERROR_NO_BOOTFILE_IF_DS_ZONE",
  sDescription =    "DNS server not creating or reading the boot file for the directory service integrated DNS zone.");
fAddWindowsDefine("DNS_ERROR_NODE_IS_DNAME",
  sDescription =    "Node is a DNAME DNS record.");
fAddWindowsDefine("DNS_ERROR_DNAME_COLLISION",
  sDescription =    "A DNAME record already exists for given name.");
fAddWindowsDefine("DNS_ERROR_ALIAS_LOOP",
  sDescription =    "An alias loop has been detected with either CNAME or DNAME records.");
fAddWindowsDefine("DNS_INFO_AXFR_COMPLETE",
  sDescription =    "DNS AXFR (zone transfer) complete.");
fAddWindowsDefine("DNS_ERROR_AXFR",
  sDescription =    "DNS zone transfer failed.");
fAddWindowsDefine("DNS_INFO_ADDED_LOCAL_WINS",
  sDescription =    "Added local WINS server.");
fAddWindowsDefine("DNS_STATUS_CONTINUE_NEEDED",
  sDescription =    "Secure update call needs to continue update request.");
fAddWindowsDefine("DNS_ERROR_NO_TCPIP",
  sDescription =    "TCP/IP network protocol not installed.");
fAddWindowsDefine("DNS_ERROR_NO_DNS_SERVERS",
  sDescription =    "No DNS servers configured for local system.");
fAddWindowsDefine("DNS_ERROR_DP_DOES_NOT_EXIST",
  sDescription =    "The specified directory partition does not exist.");
fAddWindowsDefine("DNS_ERROR_DP_ALREADY_EXISTS",
  sDescription =    "The specified directory partition already exists.");
fAddWindowsDefine("DNS_ERROR_DP_NOT_ENLISTED",
  sDescription =    "This DNS server is not enlisted in the specified directory partition.");
fAddWindowsDefine("DNS_ERROR_DP_ALREADY_ENLISTED",
  sDescription =    "This DNS server is already enlisted in the specified directory partition.");
fAddWindowsDefine("DNS_ERROR_DP_NOT_AVAILABLE",
  sDescription =    "The directory partition is not available at this time. Please wait a few minutes and try again.");
fAddWindowsDefine("DNS_ERROR_DP_FSMO_ERROR",
  sDescription =    "The operation failed because the domain naming master FSMO role could not be reached. The domain controller holding the domain naming master FSMO role is down or unable to service the request or is not running Windows Server 2003 or later.");
fAddWindowsDefine("DNS_ERROR_ZONESCOPE_ALREADY_EXISTS",
  sDescription =    "The scope already exists for the zone.");
fAddWindowsDefine("DNS_ERROR_ZONESCOPE_DOES_NOT_EXIST",
  sDescription =    "The scope does not exist for the zone.");
fAddWindowsDefine("DNS_ERROR_DEFAULT_ZONESCOPE",
  sDescription =    "The scope is the same as the default zone scope.");
fAddWindowsDefine("DNS_ERROR_INVALID_ZONESCOPE_NAME",
  sDescription =    "The scope name contains invalid characters.");
fAddWindowsDefine("DNS_ERROR_NOT_ALLOWED_WITH_ZONESCOPES",
  sDescription =    "Operation not allowed when the zone has scopes.");
fAddWindowsDefine("DNS_ERROR_LOAD_ZONESCOPE_FAILED",
  sDescription =    "Failed to load zone scope.");
fAddWindowsDefine("DNS_ERROR_ZONESCOPE_FILE_WRITEBACK_FAILED",
  sDescription =    "Failed to write data file for DNS zone scope. Please verify the file exists and is writable.");
fAddWindowsDefine("DNS_ERROR_INVALID_SCOPE_NAME",
  sDescription =    "The scope name contains invalid characters.");
fAddWindowsDefine("DNS_ERROR_SCOPE_DOES_NOT_EXIST",
  sDescription =    "The scope does not exist.");
fAddWindowsDefine("DNS_ERROR_DEFAULT_SCOPE",
  sDescription =    "The scope is the same as the default scope.");
fAddWindowsDefine("DNS_ERROR_INVALID_SCOPE_OPERATION",
  sDescription =    "The operation is invalid on the scope.");
fAddWindowsDefine("DNS_ERROR_SCOPE_LOCKED",
  sDescription =    "The scope is locked.");
fAddWindowsDefine("DNS_ERROR_SCOPE_ALREADY_EXISTS",
  sDescription =    "The scope already exists.");
fAddWindowsDefine("DNS_ERROR_POLICY_ALREADY_EXISTS",
  sDescription =    "A policy with the same name already exists on this level (server level or zone level) on the DNS server.");
fAddWindowsDefine("DNS_ERROR_POLICY_DOES_NOT_EXIST",
  sDescription =    "No policy with this name exists on this level (server level or zone level) on the DNS server.");
fAddWindowsDefine("DNS_ERROR_POLICY_INVALID_CRITERIA",
  sDescription =    "The criteria provided in the policy are invalid.");
fAddWindowsDefine("DNS_ERROR_POLICY_INVALID_SETTINGS",
  sDescription =    "At least one of the settings of this policy is invalid.");
fAddWindowsDefine("DNS_ERROR_CLIENT_SUBNET_IS_ACCESSED",
  sDescription =    "The client subnet cannot be deleted while it is being accessed by a policy.");
fAddWindowsDefine("DNS_ERROR_CLIENT_SUBNET_DOES_NOT_EXIST",
  sDescription =    "The client subnet does not exist on the DNS server.");
fAddWindowsDefine("DNS_ERROR_CLIENT_SUBNET_ALREADY_EXISTS",
  sDescription =    "A client subnet with this name already exists on the DNS server.");
fAddWindowsDefine("DNS_ERROR_SUBNET_DOES_NOT_EXIST",
  sDescription =    "The IP subnet specified does not exist in the client subnet.");
fAddWindowsDefine("DNS_ERROR_SUBNET_ALREADY_EXISTS",
  sDescription =    "The IP subnet that is being added, already exists in the client subnet.");
fAddWindowsDefine("DNS_ERROR_POLICY_LOCKED",
  sDescription =    "The policy is locked.");
fAddWindowsDefine("DNS_ERROR_POLICY_INVALID_WEIGHT",
  sDescription =    "The weight of the scope in the policy is invalid.");
fAddWindowsDefine("DNS_ERROR_POLICY_INVALID_NAME",
  sDescription =    "The DNS policy name is invalid.");
fAddWindowsDefine("DNS_ERROR_POLICY_MISSING_CRITERIA",
  sDescription =    "The policy is missing criteria.");
fAddWindowsDefine("DNS_ERROR_INVALID_CLIENT_SUBNET_NAME",
  sDescription =    "The name of the the client subnet record is invalid.");
fAddWindowsDefine("DNS_ERROR_POLICY_PROCESSING_ORDER_INVALID",
  sDescription =    "Invalid policy processing order.");
fAddWindowsDefine("DNS_ERROR_POLICY_SCOPE_MISSING",
  sDescription =    "The scope information has not been provided for a policy that requires it.");
fAddWindowsDefine("DNS_ERROR_POLICY_SCOPE_NOT_ALLOWED",
  sDescription =    "The scope information has been provided for a policy that does not require it.");
fAddWindowsDefine("DNS_ERROR_SERVERSCOPE_IS_REFERENCED",
  sDescription =    "The server scope cannot be deleted because it is referenced by a DNS Policy.");
fAddWindowsDefine("DNS_ERROR_ZONESCOPE_IS_REFERENCED",
  sDescription =    "The zone scope cannot be deleted because it is referenced by a DNS Policy.");
fAddWindowsDefine("DNS_ERROR_POLICY_INVALID_CRITERIA_CLIENT_SUBNET",
  sDescription =    "The criterion client subnet provided in the policy is invalid.");
fAddWindowsDefine("DNS_ERROR_POLICY_INVALID_CRITERIA_TRANSPORT_PROTOCOL",
  sDescription =    "The criterion transport protocol provided in the policy is invalid.");
fAddWindowsDefine("DNS_ERROR_POLICY_INVALID_CRITERIA_NETWORK_PROTOCOL",
  sDescription =    "The criterion network protocol provided in the policy is invalid.");
fAddWindowsDefine("DNS_ERROR_POLICY_INVALID_CRITERIA_INTERFACE",
  sDescription =    "The criterion interface provided in the policy is invalid.");
fAddWindowsDefine("DNS_ERROR_POLICY_INVALID_CRITERIA_FQDN",
  sDescription =    "The criterion FQDN provided in the policy is invalid.");
fAddWindowsDefine("DNS_ERROR_POLICY_INVALID_CRITERIA_QUERY_TYPE",
  sDescription =    "The criterion query type provided in the policy is invalid.");
fAddWindowsDefine("DNS_ERROR_POLICY_INVALID_CRITERIA_TIME_OF_DAY",
  sDescription =    "The criterion time of day provided in the policy is invalid.");
fAddWindowsDefine("WSAEINTR",
  sDescription =    "A blocking operation was interrupted by a call to WSACancelBlockingCall.");
fAddWindowsDefine("WSAEBADF",
  sDescription =    "The file handle supplied is not valid.");
fAddWindowsDefine("WSAEACCES",
  sDescription =    "An attempt was made to access a socket in a way forbidden by its access permissions.");
fAddWindowsDefine("WSAEFAULT",
  sDescription =    "The system detected an invalid pointer address in attempting to use a pointer argument in a call.");
fAddWindowsDefine("WSAEINVAL",
  sDescription =    "An invalid argument was supplied.");
fAddWindowsDefine("WSAEMFILE",
  sDescription =    "Too many open sockets.");
fAddWindowsDefine("WSAEWOULDBLOCK",
  sDescription =    "A non-blocking socket operation could not be completed immediately.");
fAddWindowsDefine("WSAEINPROGRESS",
  sDescription =    "A blocking operation is currently executing.");
fAddWindowsDefine("WSAEALREADY",
  sDescription =    "An operation was attempted on a non-blocking socket that already had an operation in progress.");
fAddWindowsDefine("WSAENOTSOCK",
  sDescription =    "An operation was attempted on something that is not a socket.");
fAddWindowsDefine("WSAEDESTADDRREQ",
  sDescription =    "A required address was omitted from an operation on a socket.");
fAddWindowsDefine("WSAEMSGSIZE",
  sDescription =    "A message sent on a datagram socket was larger than the internal message buffer or some other network limit, or the buffer used to receive a datagram into was smaller than the datagram itself.");
fAddWindowsDefine("WSAEPROTOTYPE",
  sDescription =    "A protocol was specified in the socket function call that does not support the semantics of the socket type requested.");
fAddWindowsDefine("WSAENOPROTOOPT",
  sDescription =    "An unknown, invalid, or unsupported option or level was specified in a getsockopt or setsockopt call.");
fAddWindowsDefine("WSAEPROTONOSUPPORT",
  sDescription =    "The requested protocol has not been configured into the system, or no implementation for it exists.");
fAddWindowsDefine("WSAESOCKTNOSUPPORT",
  sDescription =    "The support for the specified socket type does not exist in this address family.");
fAddWindowsDefine("WSAEOPNOTSUPP",
  sDescription =    "The attempted operation is not supported for the type of object referenced.");
fAddWindowsDefine("WSAEPFNOSUPPORT",
  sDescription =    "The protocol family has not been configured into the system or no implementation for it exists.");
fAddWindowsDefine("WSAEAFNOSUPPORT",
  sDescription =    "An address incompatible with the requested protocol was used.");
fAddWindowsDefine("WSAEADDRINUSE",
  sDescription =    "Only one usage of each socket address (protocol/network address/port) is normally permitted.");
fAddWindowsDefine("WSAEADDRNOTAVAIL",
  sDescription =    "The requested address is not valid in its context.");
fAddWindowsDefine("WSAENETDOWN",
  sDescription =    "A socket operation encountered a dead network.");
fAddWindowsDefine("WSAENETUNREACH",
  sDescription =    "A socket operation was attempted to an unreachable network.");
fAddWindowsDefine("WSAENETRESET",
  sDescription =    "The connection has been broken due to keep-alive activity detecting a failure while the operation was in progress.");
fAddWindowsDefine("WSAECONNABORTED",
  sDescription =    "An established connection was aborted by the software in your host machine.");
fAddWindowsDefine("WSAECONNRESET",
  sDescription =    "An existing connection was forcibly closed by the remote host.");
fAddWindowsDefine("WSAENOBUFS",
  sDescription =    "An operation on a socket could not be performed because the system lacked sufficient buffer space or because a queue was full.");
fAddWindowsDefine("WSAEISCONN",
  sDescription =    "A connect request was made on an already connected socket.");
fAddWindowsDefine("WSAENOTCONN",
  sDescription =    "A request to send or receive data was disallowed because the socket is not connected and (when sending on a datagram socket using a sendto call) no address was supplied.");
fAddWindowsDefine("WSAESHUTDOWN",
  sDescription =    "A request to send or receive data was disallowed because the socket had already been shut down in that direction with a previous shutdown call.");
fAddWindowsDefine("WSAETOOMANYREFS",
  sDescription =    "Too many references to some kernel object.");
fAddWindowsDefine("WSAETIMEDOUT",
  sDescription =    "A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond.");
fAddWindowsDefine("WSAECONNREFUSED",
  sDescription =    "No connection could be made because the target machine actively refused it.");
fAddWindowsDefine("WSAELOOP",
  sDescription =    "Cannot translate name.");
fAddWindowsDefine("WSAENAMETOOLONG",
  sDescription =    "Name component or name was too long.");
fAddWindowsDefine("WSAEHOSTDOWN",
  sDescription =    "A socket operation failed because the destination host was down.");
fAddWindowsDefine("WSAEHOSTUNREACH",
  sDescription =    "A socket operation was attempted to an unreachable host.");
fAddWindowsDefine("WSAENOTEMPTY",
  sDescription =    "Cannot remove a directory that is not empty.");
fAddWindowsDefine("WSAEPROCLIM",
  sDescription =    "A Windows Sockets implementation may have a limit on the number of applications that may use it simultaneously.");
fAddWindowsDefine("WSAEUSERS",
  sDescription =    "Ran out of quota.");
fAddWindowsDefine("WSAEDQUOT",
  sDescription =    "Ran out of disk quota.");
fAddWindowsDefine("WSAESTALE",
  sDescription =    "File handle reference is no longer available.");
fAddWindowsDefine("WSAEREMOTE",
  sDescription =    "Item is not available locally.");
fAddWindowsDefine("WSASYSNOTREADY",
  sDescription =    "WSAStartup cannot function at this time because the underlying system it uses to provide network services is currently unavailable.");
fAddWindowsDefine("WSAVERNOTSUPPORTED",
  sDescription =    "The Windows Sockets version requested is not supported.");
fAddWindowsDefine("WSANOTINITIALISED",
  sDescription =    "Either the application has not called WSAStartup, or WSAStartup failed.");
fAddWindowsDefine("WSAEDISCON",
  sDescription =    "Returned by WSARecv or WSARecvFrom to indicate the remote party has initiated a graceful shutdown sequence.");
fAddWindowsDefine("WSAENOMORE",
  sDescription =    "No more results can be returned by WSALookupServiceNext.");
fAddWindowsDefine("WSAECANCELLED",
  sDescription =    "A call to WSALookupServiceEnd was made while this call was still processing. The call has been canceled.");
fAddWindowsDefine("WSAEINVALIDPROCTABLE",
  sDescription =    "The procedure call table is invalid.");
fAddWindowsDefine("WSAEINVALIDPROVIDER",
  sDescription =    "The requested service provider is invalid.");
fAddWindowsDefine("WSAEPROVIDERFAILEDINIT",
  sDescription =    "The requested service provider could not be loaded or initialized.");
fAddWindowsDefine("WSASYSCALLFAILURE",
  sDescription =    "A system call has failed.");
fAddWindowsDefine("WSASERVICE_NOT_FOUND",
  sDescription =    "No such service is known. The service cannot be found in the specified name space.");
fAddWindowsDefine("WSATYPE_NOT_FOUND",
  sDescription =    "The specified class was not found.");
fAddWindowsDefine("WSA_E_NO_MORE",
  sDescription =    "No more results can be returned by WSALookupServiceNext.");
fAddWindowsDefine("WSA_E_CANCELLED",
  sDescription =    "A call to WSALookupServiceEnd was made while this call was still processing. The call has been canceled.");
fAddWindowsDefine("WSAEREFUSED",
  sDescription =    "A database query failed because it was actively refused.");
fAddWindowsDefine("WSAHOST_NOT_FOUND",
  sDescription =    "No such host is known.");
fAddWindowsDefine("WSATRY_AGAIN",
  sDescription =    "This is usually a temporary error during hostname resolution and means that the local server did not receive a response from an authoritative server.");
fAddWindowsDefine("WSANO_RECOVERY",
  sDescription =    "A non-recoverable error occurred during a database lookup.");
fAddWindowsDefine("WSANO_DATA",
  sDescription =    "The requested name is valid, but no data of the requested type was found.");
fAddWindowsDefine("WSA_QOS_RECEIVERS",
  sDescription =    "At least one reserve has arrived.");
fAddWindowsDefine("WSA_QOS_SENDERS",
  sDescription =    "At least one path has arrived.");
fAddWindowsDefine("WSA_QOS_NO_SENDERS",
  sDescription =    "There are no senders.");
fAddWindowsDefine("WSA_QOS_NO_RECEIVERS",
  sDescription =    "There are no receivers.");
fAddWindowsDefine("WSA_QOS_REQUEST_CONFIRMED",
  sDescription =    "Reserve has been confirmed.");
fAddWindowsDefine("WSA_QOS_ADMISSION_FAILURE",
  sDescription =    "Error due to lack of resources.");
fAddWindowsDefine("WSA_QOS_POLICY_FAILURE",
  sDescription =    "Rejected for administrative reasons - bad credentials.");
fAddWindowsDefine("WSA_QOS_BAD_STYLE",
  sDescription =    "Unknown or conflicting style.");
fAddWindowsDefine("WSA_QOS_BAD_OBJECT",
  sDescription =    "Problem with some part of the filterspec or providerspecific buffer in general.");
fAddWindowsDefine("WSA_QOS_TRAFFIC_CTRL_ERROR",
  sDescription =    "Problem with some part of the flowspec.");
fAddWindowsDefine("WSA_QOS_GENERIC_ERROR",
  sDescription =    "General QOS error.");
fAddWindowsDefine("WSA_QOS_ESERVICETYPE",
  sDescription =    "An invalid or unrecognized service type was found in the flowspec.");
fAddWindowsDefine("WSA_QOS_EFLOWSPEC",
  sDescription =    "An invalid or inconsistent flowspec was found in the QOS structure.");
fAddWindowsDefine("WSA_QOS_EPROVSPECBUF",
  sDescription =    "Invalid QOS provider-specific buffer.");
fAddWindowsDefine("WSA_QOS_EFILTERSTYLE",
  sDescription =    "An invalid QOS filter style was used.");
fAddWindowsDefine("WSA_QOS_EFILTERTYPE",
  sDescription =    "An invalid QOS filter type was used.");
fAddWindowsDefine("WSA_QOS_EFILTERCOUNT",
  sDescription =    "An incorrect number of QOS FILTERSPECs were specified in the FLOWDESCRIPTOR.");
fAddWindowsDefine("WSA_QOS_EOBJLENGTH",
  sDescription =    "An object with an invalid ObjectLength field was specified in the QOS provider-specific buffer.");
fAddWindowsDefine("WSA_QOS_EFLOWCOUNT",
  sDescription =    "An incorrect number of flow descriptors was specified in the QOS structure.");
fAddWindowsDefine("WSA_QOS_EUNKOWNPSOBJ",
  sDescription =    "An unrecognized object was found in the QOS provider-specific buffer.");
fAddWindowsDefine("WSA_QOS_EPOLICYOBJ",
  sDescription =    "An invalid policy object was found in the QOS provider-specific buffer.");
fAddWindowsDefine("WSA_QOS_EFLOWDESC",
  sDescription =    "An invalid QOS flow descriptor was found in the flow descriptor list.");
fAddWindowsDefine("WSA_QOS_EPSFLOWSPEC",
  sDescription =    "An invalid or inconsistent flowspec was found in the QOS provider specific buffer.");
fAddWindowsDefine("WSA_QOS_EPSFILTERSPEC",
  sDescription =    "An invalid FILTERSPEC was found in the QOS provider-specific buffer.");
fAddWindowsDefine("WSA_QOS_ESDMODEOBJ",
  sDescription =    "An invalid shape discard mode object was found in the QOS provider specific buffer.");
fAddWindowsDefine("WSA_QOS_ESHAPERATEOBJ",
  sDescription =    "An invalid shaping rate object was found in the QOS provider-specific buffer.");
fAddWindowsDefine("WSA_QOS_RESERVED_PETYPE",
  sDescription =    "A reserved policy element was found in the QOS provider-specific buffer.");
fAddWindowsDefine("WSA_SECURE_HOST_NOT_FOUND",
  sDescription =    "No such host is known securely.");
fAddWindowsDefine("WSA_IPSEC_NAME_POLICY_ERROR",
  sDescription =    "Name based IPSEC policy could not be added.");
fAddWindowsDefine("WININET_E_OUT_OF_HANDLES",
  sDescription =    "No more Internet handles can be allocated");
fAddWindowsDefine("WININET_E_TIMEOUT",
  sDescription =    "The operation timed out");
fAddWindowsDefine("WININET_E_EXTENDED_ERROR",
  sDescription =    "The server returned extended information");
fAddWindowsDefine("WININET_E_INTERNAL_ERROR",
  sDescription =    "An internal error occurred in the Microsoft Internet extensions");
fAddWindowsDefine("WININET_E_INVALID_URL",
  sDescription =    "The URL is invalid");
fAddWindowsDefine("WININET_E_UNRECOGNIZED_SCHEME",
  sDescription =    "The URL does not use a recognized protocol");
fAddWindowsDefine("WININET_E_NAME_NOT_RESOLVED",
  sDescription =    "The server name or address could not be resolved");
fAddWindowsDefine("WININET_E_PROTOCOL_NOT_FOUND",
  sDescription =    "A protocol with the required capabilities was not found");
fAddWindowsDefine("WININET_E_INVALID_OPTION",
  sDescription =    "The option is invalid");
fAddWindowsDefine("WININET_E_BAD_OPTION_LENGTH",
  sDescription =    "The length is incorrect for the option type");
fAddWindowsDefine("WININET_E_OPTION_NOT_SETTABLE",
  sDescription =    "The option value cannot be set");
fAddWindowsDefine("WININET_E_SHUTDOWN",
  sDescription =    "Microsoft Internet Extension support has been shut down");
fAddWindowsDefine("WININET_E_INCORRECT_USER_NAME",
  sDescription =    "The user name was not allowed");
fAddWindowsDefine("WININET_E_INCORRECT_PASSWORD",
  sDescription =    "The password was not allowed");
fAddWindowsDefine("WININET_E_LOGIN_FAILURE",
  sDescription =    "The login request was denied");
fAddWindowsDefine("WININET_E_INVALID_OPERATION",
  sDescription =    "The requested operation is invalid");
fAddWindowsDefine("WININET_E_OPERATION_CANCELLED",
  sDescription =    "The operation has been canceled");
fAddWindowsDefine("WININET_E_INCORRECT_HANDLE_TYPE",
  sDescription =    "The supplied handle is the wrong type for the requested operation");
fAddWindowsDefine("WININET_E_INCORRECT_HANDLE_STATE",
  sDescription =    "The handle is in the wrong state for the requested operation");
fAddWindowsDefine("WININET_E_NOT_PROXY_REQUEST",
  sDescription =    "The request cannot be made on a Proxy session");
fAddWindowsDefine("WININET_E_REGISTRY_VALUE_NOT_FOUND",
  sDescription =    "The registry value could not be found");
fAddWindowsDefine("WININET_E_BAD_REGISTRY_PARAMETER",
  sDescription =    "The registry parameter is incorrect");
fAddWindowsDefine("WININET_E_NO_DIRECT_ACCESS",
  sDescription =    "Direct Internet access is not available");
fAddWindowsDefine("WININET_E_NO_CONTEXT",
  sDescription =    "No context value was supplied");
fAddWindowsDefine("WININET_E_NO_CALLBACK",
  sDescription =    "No status callback was supplied");
fAddWindowsDefine("WININET_E_REQUEST_PENDING",
  sDescription =    "There are outstanding requests");
fAddWindowsDefine("WININET_E_INCORRECT_FORMAT",
  sDescription =    "The information format is incorrect");
fAddWindowsDefine("WININET_E_ITEM_NOT_FOUND",
  sDescription =    "The requested item could not be found");
fAddWindowsDefine("WININET_E_CANNOT_CONNECT",
  sDescription =    "A connection with the server could not be established");
fAddWindowsDefine("WININET_E_CONNECTION_ABORTED",
  sDescription =    "The connection with the server was terminated abnormally");
fAddWindowsDefine("WININET_E_CONNECTION_RESET",
  sDescription =    "The connection with the server was reset");
fAddWindowsDefine("WININET_E_FORCE_RETRY",
  sDescription =    "The action must be retried");
fAddWindowsDefine("WININET_E_INVALID_PROXY_REQUEST",
  sDescription =    "The proxy request is invalid");
fAddWindowsDefine("WININET_E_NEED_UI",
  sDescription =    "User interaction is required to complete the operation");
fAddWindowsDefine("WININET_E_HANDLE_EXISTS",
  sDescription =    "The handle already exists");
fAddWindowsDefine("WININET_E_SEC_CERT_DATE_INVALID",
  sDescription =    "The date in the certificate is invalid or has expired");
fAddWindowsDefine("WININET_E_SEC_CERT_CN_INVALID",
  sDescription =    "The host name in the certificate is invalid or does not match");
fAddWindowsDefine("WININET_E_HTTP_TO_HTTPS_ON_REDIR",
  sDescription =    "A redirect request will change a non-secure to a secure connection");
fAddWindowsDefine("WININET_E_HTTPS_TO_HTTP_ON_REDIR",
  sDescription =    "A redirect request will change a secure to a non-secure connection");
fAddWindowsDefine("WININET_E_MIXED_SECURITY",
  sDescription =    "Mixed secure and non-secure connections");
fAddWindowsDefine("WININET_E_CHG_POST_IS_NON_SECURE",
  sDescription =    "Changing to non-secure post");
fAddWindowsDefine("WININET_E_POST_IS_NON_SECURE",
  sDescription =    "Data is being posted on a non-secure connection");
fAddWindowsDefine("WININET_E_CLIENT_AUTH_CERT_NEEDED",
  sDescription =    "A certificate is required to complete client authentication");
fAddWindowsDefine("WININET_E_INVALID_CA",
  sDescription =    "The certificate authority is invalid or incorrect");
fAddWindowsDefine("WININET_E_CLIENT_AUTH_NOT_SETUP",
  sDescription =    "Client authentication has not been correctly installed");
fAddWindowsDefine("WININET_E_ASYNC_THREAD_FAILED",
  sDescription =    "An error has occurred in a Wininet asynchronous thread. You may need to restart");
fAddWindowsDefine("WININET_E_REDIRECT_SCHEME_CHANGE",
  sDescription =    "The protocol scheme has changed during a redirect operaiton");
fAddWindowsDefine("WININET_E_DIALOG_PENDING",
  sDescription =    "There are operations awaiting retry");
fAddWindowsDefine("WININET_E_RETRY_DIALOG",
  sDescription =    "The operation must be retried");
fAddWindowsDefine("WININET_E_NO_NEW_CONTAINERS",
  sDescription =    "There are no new cache containers");
fAddWindowsDefine("WININET_E_HTTPS_HTTP_SUBMIT_REDIR",
  sDescription =    "A security zone check indicates the operation must be retried");
fAddWindowsDefine("WININET_E_SEC_CERT_ERRORS",
  sDescription =    "The SSL certificate contains errors.");
fAddWindowsDefine("WININET_E_SEC_CERT_REV_FAILED",
  sDescription =    "It was not possible to connect to the revocation server or a definitive response could not be obtained.");
fAddWindowsDefine("WININET_E_HEADER_NOT_FOUND",
  sDescription =    "The requested header was not found");
fAddWindowsDefine("WININET_E_DOWNLEVEL_SERVER",
  sDescription =    "The server does not support the requested protocol level");
fAddWindowsDefine("WININET_E_INVALID_SERVER_RESPONSE",
  sDescription =    "The server returned an invalid or unrecognized response");
fAddWindowsDefine("WININET_E_INVALID_HEADER",
  sDescription =    "The supplied HTTP header is invalid");
fAddWindowsDefine("WININET_E_INVALID_QUERY_REQUEST",
  sDescription =    "The request for a HTTP header is invalid");
fAddWindowsDefine("WININET_E_HEADER_ALREADY_EXISTS",
  sDescription =    "The HTTP header already exists");
fAddWindowsDefine("WININET_E_REDIRECT_FAILED",
  sDescription =    "The HTTP redirect request failed");
fAddWindowsDefine("WININET_E_SECURITY_CHANNEL_ERROR",
  sDescription =    "An error occurred in the secure channel support");
fAddWindowsDefine("WININET_E_UNABLE_TO_CACHE_FILE",
  sDescription =    "The file could not be written to the cache");
fAddWindowsDefine("WININET_E_TCPIP_NOT_INSTALLED",
  sDescription =    "The TCP/IP protocol is not installed properly");
fAddWindowsDefine("WININET_E_NOT_REDIRECTED",
  sDescription =    "The HTTP request was not redirected");
fAddWindowsDefine("WININET_E_COOKIE_NEEDS_CONFIRMATION",
  sDescription =    "A cookie from the server must be confirmed by the user");
fAddWindowsDefine("WININET_E_COOKIE_DECLINED",
  sDescription =    "A cookie from the server has been declined acceptance");
fAddWindowsDefine("WININET_E_DISCONNECTED",
  sDescription =    "The computer is disconnected from the network");
fAddWindowsDefine("WININET_E_SERVER_UNREACHABLE",
  sDescription =    "The server is unreachable");
fAddWindowsDefine("WININET_E_PROXY_SERVER_UNREACHABLE",
  sDescription =    "The proxy server is unreachable");
fAddWindowsDefine("WININET_E_BAD_AUTO_PROXY_SCRIPT",
  sDescription =    "The proxy auto-configuration script is in error");
fAddWindowsDefine("WININET_E_UNABLE_TO_DOWNLOAD_SCRIPT",
  sDescription =    "Could not download the proxy auto-configuration script file");
fAddWindowsDefine("WININET_E_REDIRECT_NEEDS_CONFIRMATION",
  sDescription =    "The HTTP redirect request must be confirmed by the user");
fAddWindowsDefine("WININET_E_SEC_INVALID_CERT",
  sDescription =    "The supplied certificate is invalid");
fAddWindowsDefine("WININET_E_SEC_CERT_REVOKED",
  sDescription =    "The supplied certificate has been revoked");
fAddWindowsDefine("WININET_E_FAILED_DUETOSECURITYCHECK",
  sDescription =    "The Dialup failed because file sharing was turned on and a failure was requested if security check was needed");
fAddWindowsDefine("WININET_E_NOT_INITIALIZED",
  sDescription =    "Initialization of the WinINet API has not occurred");
fAddWindowsDefine("WININET_E_LOGIN_FAILURE_DISPLAY_ENTITY_BODY",
  sDescription =    "Login failed and the client should display the entity body to the user");
fAddWindowsDefine("WININET_E_DECODING_FAILED",
  sDescription =    "Content decoding has failed");
fAddWindowsDefine("ERROR_IPSEC_QM_POLICY_EXISTS",
  sDescription =    "The specified quick mode policy already exists.");
fAddWindowsDefine("ERROR_IPSEC_QM_POLICY_NOT_FOUND",
  sDescription =    "The specified quick mode policy was not found.");
fAddWindowsDefine("ERROR_IPSEC_QM_POLICY_IN_USE",
  sDescription =    "The specified quick mode policy is being used.");
fAddWindowsDefine("ERROR_IPSEC_MM_POLICY_EXISTS",
  sDescription =    "The specified main mode policy already exists.");
fAddWindowsDefine("ERROR_IPSEC_MM_POLICY_NOT_FOUND",
  sDescription =    "The specified main mode policy was not found");
fAddWindowsDefine("ERROR_IPSEC_MM_POLICY_IN_USE",
  sDescription =    "The specified main mode policy is being used.");
fAddWindowsDefine("ERROR_IPSEC_MM_FILTER_EXISTS",
  sDescription =    "The specified main mode filter already exists.");
fAddWindowsDefine("ERROR_IPSEC_MM_FILTER_NOT_FOUND",
  sDescription =    "The specified main mode filter was not found.");
fAddWindowsDefine("ERROR_IPSEC_TRANSPORT_FILTER_EXISTS",
  sDescription =    "The specified transport mode filter already exists.");
fAddWindowsDefine("ERROR_IPSEC_TRANSPORT_FILTER_NOT_FOUND",
  sDescription =    "The specified transport mode filter does not exist.");
fAddWindowsDefine("ERROR_IPSEC_MM_AUTH_EXISTS",
  sDescription =    "The specified main mode authentication list exists.");
fAddWindowsDefine("ERROR_IPSEC_MM_AUTH_NOT_FOUND",
  sDescription =    "The specified main mode authentication list was not found.");
fAddWindowsDefine("ERROR_IPSEC_MM_AUTH_IN_USE",
  sDescription =    "The specified main mode authentication list is being used.");
fAddWindowsDefine("ERROR_IPSEC_DEFAULT_MM_POLICY_NOT_FOUND",
  sDescription =    "The specified default main mode policy was not found.");
fAddWindowsDefine("ERROR_IPSEC_DEFAULT_MM_AUTH_NOT_FOUND",
  sDescription =    "The specified default main mode authentication list was not found.");
fAddWindowsDefine("ERROR_IPSEC_DEFAULT_QM_POLICY_NOT_FOUND",
  sDescription =    "The specified default quick mode policy was not found.");
fAddWindowsDefine("ERROR_IPSEC_TUNNEL_FILTER_EXISTS",
  sDescription =    "The specified tunnel mode filter exists.");
fAddWindowsDefine("ERROR_IPSEC_TUNNEL_FILTER_NOT_FOUND",
  sDescription =    "The specified tunnel mode filter was not found.");
fAddWindowsDefine("ERROR_IPSEC_MM_FILTER_PENDING_DELETION",
  sDescription =    "The Main Mode filter is pending deletion.");
fAddWindowsDefine("ERROR_IPSEC_TRANSPORT_FILTER_PENDING_DELETION",
  sDescription =    "The transport filter is pending deletion.");
fAddWindowsDefine("ERROR_IPSEC_TUNNEL_FILTER_PENDING_DELETION",
  sDescription =    "The tunnel filter is pending deletion.");
fAddWindowsDefine("ERROR_IPSEC_MM_POLICY_PENDING_DELETION",
  sDescription =    "The Main Mode policy is pending deletion.");
fAddWindowsDefine("ERROR_IPSEC_MM_AUTH_PENDING_DELETION",
  sDescription =    "The Main Mode authentication bundle is pending deletion.");
fAddWindowsDefine("ERROR_IPSEC_QM_POLICY_PENDING_DELETION",
  sDescription =    "The Quick Mode policy is pending deletion.");
fAddWindowsDefine("WARNING_IPSEC_MM_POLICY_PRUNED",
  sDescription =    "The Main Mode policy was successfully added, but some of the requested offers are not supported.");
fAddWindowsDefine("WARNING_IPSEC_QM_POLICY_PRUNED",
  sDescription =    "The Quick Mode policy was successfully added, but some of the requested offers are not supported.");
fAddWindowsDefine("ERROR_IPSEC_IKE_NEG_STATUS_BEGIN",
  sDescription =    "ERROR_IPSEC_IKE_NEG_STATUS_BEGIN");
fAddWindowsDefine("ERROR_IPSEC_IKE_AUTH_FAIL",
  sDescription =    "IKE authentication credentials are unacceptable");
fAddWindowsDefine("ERROR_IPSEC_IKE_ATTRIB_FAIL",
  sDescription =    "IKE security attributes are unacceptable");
fAddWindowsDefine("ERROR_IPSEC_IKE_NEGOTIATION_PENDING",
  sDescription =    "IKE Negotiation in progress");
fAddWindowsDefine("ERROR_IPSEC_IKE_GENERAL_PROCESSING_ERROR",
  sDescription =    "General processing error");
fAddWindowsDefine("ERROR_IPSEC_IKE_TIMED_OUT",
  sDescription =    "Negotiation timed out");
fAddWindowsDefine("ERROR_IPSEC_IKE_NO_CERT",
  sDescription =    "IKE failed to find valid machine certificate. Contact your Network Security Administrator about installing a valid certificate in the appropriate Certificate Store.");
fAddWindowsDefine("ERROR_IPSEC_IKE_SA_DELETED",
  sDescription =    "IKE SA deleted by peer before establishment completed");
fAddWindowsDefine("ERROR_IPSEC_IKE_SA_REAPED",
  sDescription =    "IKE SA deleted before establishment completed");
fAddWindowsDefine("ERROR_IPSEC_IKE_MM_ACQUIRE_DROP",
  sDescription =    "Negotiation request sat in Queue too long");
fAddWindowsDefine("ERROR_IPSEC_IKE_QM_ACQUIRE_DROP",
  sDescription =    "Negotiation request sat in Queue too long");
fAddWindowsDefine("ERROR_IPSEC_IKE_QUEUE_DROP_MM",
  sDescription =    "Negotiation request sat in Queue too long");
fAddWindowsDefine("ERROR_IPSEC_IKE_QUEUE_DROP_NO_MM",
  sDescription =    "Negotiation request sat in Queue too long");
fAddWindowsDefine("ERROR_IPSEC_IKE_DROP_NO_RESPONSE",
  sDescription =    "No response from peer");
fAddWindowsDefine("ERROR_IPSEC_IKE_MM_DELAY_DROP",
  sDescription =    "Negotiation took too long");
fAddWindowsDefine("ERROR_IPSEC_IKE_QM_DELAY_DROP",
  sDescription =    "Negotiation took too long");
fAddWindowsDefine("ERROR_IPSEC_IKE_ERROR",
  sDescription =    "Unknown error occurred");
fAddWindowsDefine("ERROR_IPSEC_IKE_CRL_FAILED",
  sDescription =    "Certificate Revocation Check failed");
fAddWindowsDefine("ERROR_IPSEC_IKE_INVALID_KEY_USAGE",
  sDescription =    "Invalid certificate key usage");
fAddWindowsDefine("ERROR_IPSEC_IKE_INVALID_CERT_TYPE",
  sDescription =    "Invalid certificate type");
fAddWindowsDefine("ERROR_IPSEC_IKE_NO_PRIVATE_KEY",
  sDescription =    "IKE negotiation failed because the machine certificate used does not have a private key. IPsec certificates require a private key. Contact your Network Security administrator about replacing with a certificate that has a private key.");
fAddWindowsDefine("ERROR_IPSEC_IKE_SIMULTANEOUS_REKEY",
  sDescription =    "Simultaneous rekeys were detected.");
fAddWindowsDefine("ERROR_IPSEC_IKE_DH_FAIL",
  sDescription =    "Failure in Diffie-Hellman computation");
fAddWindowsDefine("ERROR_IPSEC_IKE_CRITICAL_PAYLOAD_NOT_RECOGNIZED",
  sDescription =    "Don't know how to process critical payload");
fAddWindowsDefine("ERROR_IPSEC_IKE_INVALID_HEADER",
  sDescription =    "Invalid header");
fAddWindowsDefine("ERROR_IPSEC_IKE_NO_POLICY",
  sDescription =    "No policy configured");
fAddWindowsDefine("ERROR_IPSEC_IKE_INVALID_SIGNATURE",
  sDescription =    "Failed to verify signature");
fAddWindowsDefine("ERROR_IPSEC_IKE_KERBEROS_ERROR",
  sDescription =    "Failed to authenticate using Kerberos");
fAddWindowsDefine("ERROR_IPSEC_IKE_NO_PUBLIC_KEY",
  sDescription =    "Peer's certificate did not have a public key");
fAddWindowsDefine("ERROR_IPSEC_IKE_PROCESS_ERR",
  sDescription =    "Error processing error payload");
fAddWindowsDefine("ERROR_IPSEC_IKE_PROCESS_ERR_SA",
  sDescription =    "Error processing SA payload");
fAddWindowsDefine("ERROR_IPSEC_IKE_PROCESS_ERR_PROP",
  sDescription =    "Error processing Proposal payload");
fAddWindowsDefine("ERROR_IPSEC_IKE_PROCESS_ERR_TRANS",
  sDescription =    "Error processing Transform payload");
fAddWindowsDefine("ERROR_IPSEC_IKE_PROCESS_ERR_KE",
  sDescription =    "Error processing KE payload");
fAddWindowsDefine("ERROR_IPSEC_IKE_PROCESS_ERR_ID",
  sDescription =    "Error processing ID payload");
fAddWindowsDefine("ERROR_IPSEC_IKE_PROCESS_ERR_CERT",
  sDescription =    "Error processing Cert payload");
fAddWindowsDefine("ERROR_IPSEC_IKE_PROCESS_ERR_CERT_REQ",
  sDescription =    "Error processing Certificate Request payload");
fAddWindowsDefine("ERROR_IPSEC_IKE_PROCESS_ERR_HASH",
  sDescription =    "Error processing Hash payload");
fAddWindowsDefine("ERROR_IPSEC_IKE_PROCESS_ERR_SIG",
  sDescription =    "Error processing Signature payload");
fAddWindowsDefine("ERROR_IPSEC_IKE_PROCESS_ERR_NONCE",
  sDescription =    "Error processing Nonce payload");
fAddWindowsDefine("ERROR_IPSEC_IKE_PROCESS_ERR_NOTIFY",
  sDescription =    "Error processing Notify payload");
fAddWindowsDefine("ERROR_IPSEC_IKE_PROCESS_ERR_DELETE",
  sDescription =    "Error processing Delete Payload");
fAddWindowsDefine("ERROR_IPSEC_IKE_PROCESS_ERR_VENDOR",
  sDescription =    "Error processing VendorId payload");
fAddWindowsDefine("ERROR_IPSEC_IKE_INVALID_PAYLOAD",
  sDescription =    "Invalid payload received");
fAddWindowsDefine("ERROR_IPSEC_IKE_LOAD_SOFT_SA",
  sDescription =    "Soft SA loaded");
fAddWindowsDefine("ERROR_IPSEC_IKE_SOFT_SA_TORN_DOWN",
  sDescription =    "Soft SA torn down");
fAddWindowsDefine("ERROR_IPSEC_IKE_INVALID_COOKIE",
  sDescription =    "Invalid cookie received.");
fAddWindowsDefine("ERROR_IPSEC_IKE_NO_PEER_CERT",
  sDescription =    "Peer failed to send valid machine certificate");
fAddWindowsDefine("ERROR_IPSEC_IKE_PEER_CRL_FAILED",
  sDescription =    "Certification Revocation check of peer's certificate failed");
fAddWindowsDefine("ERROR_IPSEC_IKE_POLICY_CHANGE",
  sDescription =    "New policy invalidated SAs formed with old policy");
fAddWindowsDefine("ERROR_IPSEC_IKE_NO_MM_POLICY",
  sDescription =    "There is no available Main Mode IKE policy.");
fAddWindowsDefine("ERROR_IPSEC_IKE_NOTCBPRIV",
  sDescription =    "Failed to enabled TCB privilege.");
fAddWindowsDefine("ERROR_IPSEC_IKE_SECLOADFAIL",
  sDescription =    "Failed to load SECURITY.DLL.");
fAddWindowsDefine("ERROR_IPSEC_IKE_FAILSSPINIT",
  sDescription =    "Failed to obtain security function table dispatch address from SSPI.");
fAddWindowsDefine("ERROR_IPSEC_IKE_FAILQUERYSSP",
  sDescription =    "Failed to query Kerberos package to obtain max token size.");
fAddWindowsDefine("ERROR_IPSEC_IKE_SRVACQFAIL",
  sDescription =    "Failed to obtain Kerberos server credentials for ISAKMP/ERROR_IPSEC_IKE service. Kerberos authentication will not function. The most likely reason for this is lack of domain membership. This is normal if your computer is a member of a workgroup.");
fAddWindowsDefine("ERROR_IPSEC_IKE_SRVQUERYCRED",
  sDescription =    "Failed to determine SSPI principal name for ISAKMP/ERROR_IPSEC_IKE service (QueryCredentialsAttributes).");
fAddWindowsDefine("ERROR_IPSEC_IKE_GETSPIFAIL",
  sDescription =    "Failed to obtain new SPI for the inbound SA from IPsec driver. The most common cause for this is that the driver does not have the correct filter. Check your policy to verify the filters.");
fAddWindowsDefine("ERROR_IPSEC_IKE_INVALID_FILTER",
  sDescription =    "Given filter is invalid");
fAddWindowsDefine("ERROR_IPSEC_IKE_OUT_OF_MEMORY",
  sDescription =    "Memory allocation failed.");
fAddWindowsDefine("ERROR_IPSEC_IKE_ADD_UPDATE_KEY_FAILED",
  sDescription =    "Failed to add Security Association to IPsec Driver. The most common cause for this is if the IKE negotiation took too long to complete. If the problem persists, reduce the load on the faulting machine.");
fAddWindowsDefine("ERROR_IPSEC_IKE_INVALID_POLICY",
  sDescription =    "Invalid policy");
fAddWindowsDefine("ERROR_IPSEC_IKE_UNKNOWN_DOI",
  sDescription =    "Invalid DOI");
fAddWindowsDefine("ERROR_IPSEC_IKE_INVALID_SITUATION",
  sDescription =    "Invalid situation");
fAddWindowsDefine("ERROR_IPSEC_IKE_DH_FAILURE",
  sDescription =    "Diffie-Hellman failure");
fAddWindowsDefine("ERROR_IPSEC_IKE_INVALID_GROUP",
  sDescription =    "Invalid Diffie-Hellman group");
fAddWindowsDefine("ERROR_IPSEC_IKE_ENCRYPT",
  sDescription =    "Error encrypting payload");
fAddWindowsDefine("ERROR_IPSEC_IKE_DECRYPT",
  sDescription =    "Error decrypting payload");
fAddWindowsDefine("ERROR_IPSEC_IKE_POLICY_MATCH",
  sDescription =    "Policy match error");
fAddWindowsDefine("ERROR_IPSEC_IKE_UNSUPPORTED_ID",
  sDescription =    "Unsupported ID");
fAddWindowsDefine("ERROR_IPSEC_IKE_INVALID_HASH",
  sDescription =    "Hash verification failed");
fAddWindowsDefine("ERROR_IPSEC_IKE_INVALID_HASH_ALG",
  sDescription =    "Invalid hash algorithm");
fAddWindowsDefine("ERROR_IPSEC_IKE_INVALID_HASH_SIZE",
  sDescription =    "Invalid hash size");
fAddWindowsDefine("ERROR_IPSEC_IKE_INVALID_ENCRYPT_ALG",
  sDescription =    "Invalid encryption algorithm");
fAddWindowsDefine("ERROR_IPSEC_IKE_INVALID_AUTH_ALG",
  sDescription =    "Invalid authentication algorithm");
fAddWindowsDefine("ERROR_IPSEC_IKE_INVALID_SIG",
  sDescription =    "Invalid certificate signature");
fAddWindowsDefine("ERROR_IPSEC_IKE_LOAD_FAILED",
  sDescription =    "Load failed");
fAddWindowsDefine("ERROR_IPSEC_IKE_RPC_DELETE",
  sDescription =    "Deleted via RPC call");
fAddWindowsDefine("ERROR_IPSEC_IKE_BENIGN_REINIT",
  sDescription =    "Temporary state created to perform reinitialization. This is not a real failure.");
fAddWindowsDefine("ERROR_IPSEC_IKE_INVALID_RESPONDER_LIFETIME_NOTIFY",
  sDescription =    "The lifetime value received in the Responder Lifetime Notify is below the Windows 2000 configured minimum value. Please fix the policy on the peer machine.");
fAddWindowsDefine("ERROR_IPSEC_IKE_INVALID_MAJOR_VERSION",
  sDescription =    "The recipient cannot handle version of IKE specified in the header.");
fAddWindowsDefine("ERROR_IPSEC_IKE_INVALID_CERT_KEYLEN",
  sDescription =    "Key length in certificate is too small for configured security requirements.");
fAddWindowsDefine("ERROR_IPSEC_IKE_MM_LIMIT",
  sDescription =    "Max number of established MM SAs to peer exceeded.");
fAddWindowsDefine("ERROR_IPSEC_IKE_NEGOTIATION_DISABLED",
  sDescription =    "IKE received a policy that disables negotiation.");
fAddWindowsDefine("ERROR_IPSEC_IKE_QM_LIMIT",
  sDescription =    "Reached maximum quick mode limit for the main mode. New main mode will be started.");
fAddWindowsDefine("ERROR_IPSEC_IKE_MM_EXPIRED",
  sDescription =    "Main mode SA lifetime expired or peer sent a main mode delete.");
fAddWindowsDefine("ERROR_IPSEC_IKE_PEER_MM_ASSUMED_INVALID",
  sDescription =    "Main mode SA assumed to be invalid because peer stopped responding.");
fAddWindowsDefine("ERROR_IPSEC_IKE_CERT_CHAIN_POLICY_MISMATCH",
  sDescription =    "Certificate doesn't chain to a trusted root in IPsec policy.");
fAddWindowsDefine("ERROR_IPSEC_IKE_UNEXPECTED_MESSAGE_ID",
  sDescription =    "Received unexpected message ID.");
fAddWindowsDefine("ERROR_IPSEC_IKE_INVALID_AUTH_PAYLOAD",
  sDescription =    "Received invalid authentication offers.");
fAddWindowsDefine("ERROR_IPSEC_IKE_DOS_COOKIE_SENT",
  sDescription =    "Sent DoS cookie notify to initiator.");
fAddWindowsDefine("ERROR_IPSEC_IKE_SHUTTING_DOWN",
  sDescription =    "IKE service is shutting down.");
fAddWindowsDefine("ERROR_IPSEC_IKE_CGA_AUTH_FAILED",
  sDescription =    "Could not verify binding between CGA address and certificate.");
fAddWindowsDefine("ERROR_IPSEC_IKE_PROCESS_ERR_NATOA",
  sDescription =    "Error processing NatOA payload.");
fAddWindowsDefine("ERROR_IPSEC_IKE_INVALID_MM_FOR_QM",
  sDescription =    "Parameters of the main mode are invalid for this quick mode.");
fAddWindowsDefine("ERROR_IPSEC_IKE_QM_EXPIRED",
  sDescription =    "Quick mode SA was expired by IPsec driver.");
fAddWindowsDefine("ERROR_IPSEC_IKE_TOO_MANY_FILTERS",
  sDescription =    "Too many dynamically added IKEEXT filters were detected.");
fAddWindowsDefine("ERROR_IPSEC_IKE_NEG_STATUS_END",
  sDescription =    "ERROR_IPSEC_IKE_NEG_STATUS_END");
fAddWindowsDefine("ERROR_IPSEC_IKE_KILL_DUMMY_NAP_TUNNEL",
  sDescription =    "NAP reauth succeeded and must delete the dummy NAP IKEv2 tunnel.");
fAddWindowsDefine("ERROR_IPSEC_IKE_INNER_IP_ASSIGNMENT_FAILURE",
  sDescription =    "Error in assigning inner IP address to initiator in tunnel mode.");
fAddWindowsDefine("ERROR_IPSEC_IKE_REQUIRE_CP_PAYLOAD_MISSING",
  sDescription =    "Require configuration payload missing.");
fAddWindowsDefine("ERROR_IPSEC_KEY_MODULE_IMPERSONATION_NEGOTIATION_PENDING",
  sDescription =    "A negotiation running as the security principle who issued the connection is in progress");
fAddWindowsDefine("ERROR_IPSEC_IKE_COEXISTENCE_SUPPRESS",
  sDescription =    "SA was deleted due to IKEv1/AuthIP co-existence suppress check.");
fAddWindowsDefine("ERROR_IPSEC_IKE_RATELIMIT_DROP",
  sDescription =    "Incoming SA request was dropped due to peer IP address rate limiting.");
fAddWindowsDefine("ERROR_IPSEC_IKE_PEER_DOESNT_SUPPORT_MOBIKE",
  sDescription =    "Peer does not support MOBIKE.");
fAddWindowsDefine("ERROR_IPSEC_IKE_AUTHORIZATION_FAILURE",
  sDescription =    "SA establishment is not authorized.");
fAddWindowsDefine("ERROR_IPSEC_IKE_STRONG_CRED_AUTHORIZATION_FAILURE",
  sDescription =    "SA establishment is not authorized because there is not a sufficiently strong PKINIT-based credential.");
fAddWindowsDefine("ERROR_IPSEC_IKE_AUTHORIZATION_FAILURE_WITH_OPTIONAL_RETRY",
  sDescription =    "SA establishment is not authorized. You may need to enter updated or different credentials such as a smartcard.");
fAddWindowsDefine("ERROR_IPSEC_IKE_STRONG_CRED_AUTHORIZATION_AND_CERTMAP_FAILURE",
  sDescription =    "SA establishment is not authorized because there is not a sufficiently strong PKINIT-based credential. This might be related to certificate-to-account mapping failure for the SA.");
fAddWindowsDefine("ERROR_IPSEC_IKE_NEG_STATUS_EXTENDED_END",
  sDescription =    "ERROR_IPSEC_IKE_NEG_STATUS_EXTENDED_END");
fAddWindowsDefine("ERROR_IPSEC_BAD_SPI",
  sDescription =    "The SPI in the packet does not match a valid IPsec SA.");
fAddWindowsDefine("ERROR_IPSEC_SA_LIFETIME_EXPIRED",
  sDescription =    "Packet was received on an IPsec SA whose lifetime has expired.");
fAddWindowsDefine("ERROR_IPSEC_WRONG_SA",
  sDescription =    "Packet was received on an IPsec SA that does not match the packet characteristics.");
fAddWindowsDefine("ERROR_IPSEC_REPLAY_CHECK_FAILED",
  sDescription =    "Packet sequence number replay check failed.");
fAddWindowsDefine("ERROR_IPSEC_INVALID_PACKET",
  sDescription =    "IPsec header and/or trailer in the packet is invalid.");
fAddWindowsDefine("ERROR_IPSEC_INTEGRITY_CHECK_FAILED",
  sDescription =    "IPsec integrity check failed.");
fAddWindowsDefine("ERROR_IPSEC_CLEAR_TEXT_DROP",
  sDescription =    "IPsec dropped a clear text packet.");
fAddWindowsDefine("ERROR_IPSEC_AUTH_FIREWALL_DROP",
  sDescription =    "IPsec dropped an incoming ESP packet in authenticated firewall mode. This drop is benign.");
fAddWindowsDefine("ERROR_IPSEC_THROTTLE_DROP",
  sDescription =    "IPsec dropped a packet due to DoS throttling.");
fAddWindowsDefine("ERROR_IPSEC_DOSP_BLOCK",
  sDescription =    "IPsec DoS Protection matched an explicit block rule.");
fAddWindowsDefine("ERROR_IPSEC_DOSP_RECEIVED_MULTICAST",
  sDescription =    "IPsec DoS Protection received an IPsec specific multicast packet which is not allowed.");
fAddWindowsDefine("ERROR_IPSEC_DOSP_INVALID_PACKET",
  sDescription =    "IPsec DoS Protection received an incorrectly formatted packet.");
fAddWindowsDefine("ERROR_IPSEC_DOSP_STATE_LOOKUP_FAILED",
  sDescription =    "IPsec DoS Protection failed to look up state.");
fAddWindowsDefine("ERROR_IPSEC_DOSP_MAX_ENTRIES",
  sDescription =    "IPsec DoS Protection failed to create state because the maximum number of entries allowed by policy has been reached.");
fAddWindowsDefine("ERROR_IPSEC_DOSP_KEYMOD_NOT_ALLOWED",
  sDescription =    "IPsec DoS Protection received an IPsec negotiation packet for a keying module which is not allowed by policy.");
fAddWindowsDefine("ERROR_IPSEC_DOSP_NOT_INSTALLED",
  sDescription =    "IPsec DoS Protection has not been enabled.");
fAddWindowsDefine("ERROR_IPSEC_DOSP_MAX_PER_IP_RATELIMIT_QUEUES",
  sDescription =    "IPsec DoS Protection failed to create a per internal IP rate limit queue because the maximum number of queues allowed by policy has been reached.");
fAddWindowsDefine("ERROR_SXS_SECTION_NOT_FOUND",
  sDescription =    "The requested section was not present in the activation context.");
fAddWindowsDefine("ERROR_SXS_CANT_GEN_ACTCTX",
  sDescription =    "The application has failed to start because its side-by-side configuration is incorrect. Please see the application event log or use the command-line sxstrace.exe tool for more detail.");
fAddWindowsDefine("ERROR_SXS_INVALID_ACTCTXDATA_FORMAT",
  sDescription =    "The application binding data format is invalid.");
fAddWindowsDefine("ERROR_SXS_ASSEMBLY_NOT_FOUND",
  sDescription =    "The referenced assembly is not installed on your system.");
fAddWindowsDefine("ERROR_SXS_MANIFEST_FORMAT_ERROR",
  sDescription =    "The manifest file does not begin with the required tag and format information.");
fAddWindowsDefine("ERROR_SXS_MANIFEST_PARSE_ERROR",
  sDescription =    "The manifest file contains one or more syntax errors.");
fAddWindowsDefine("ERROR_SXS_ACTIVATION_CONTEXT_DISABLED",
  sDescription =    "The application attempted to activate a disabled activation context.");
fAddWindowsDefine("ERROR_SXS_KEY_NOT_FOUND",
  sDescription =    "The requested lookup key was not found in any active activation context.");
fAddWindowsDefine("ERROR_SXS_VERSION_CONFLICT",
  sDescription =    "A component version required by the application conflicts with another component version already active.");
fAddWindowsDefine("ERROR_SXS_WRONG_SECTION_TYPE",
  sDescription =    "The type requested activation context section does not match the query API used.");
fAddWindowsDefine("ERROR_SXS_THREAD_QUERIES_DISABLED",
  sDescription =    "Lack of system resources has required isolated activation to be disabled for the current thread of execution.");
fAddWindowsDefine("ERROR_SXS_PROCESS_DEFAULT_ALREADY_SET",
  sDescription =    "An attempt to set the process default activation context failed because the process default activation context was already set.");
fAddWindowsDefine("ERROR_SXS_UNKNOWN_ENCODING_GROUP",
  sDescription =    "The encoding group identifier specified is not recognized.");
fAddWindowsDefine("ERROR_SXS_UNKNOWN_ENCODING",
  sDescription =    "The encoding requested is not recognized.");
fAddWindowsDefine("ERROR_SXS_INVALID_XML_NAMESPACE_URI",
  sDescription =    "The manifest contains a reference to an invalid URI.");
fAddWindowsDefine("ERROR_SXS_ROOT_MANIFEST_DEPENDENCY_NOT_INSTALLED",
  sDescription =    "The application manifest contains a reference to a dependent assembly which is not installed");
fAddWindowsDefine("ERROR_SXS_LEAF_MANIFEST_DEPENDENCY_NOT_INSTALLED",
  sDescription =    "The manifest for an assembly used by the application has a reference to a dependent assembly which is not installed");
fAddWindowsDefine("ERROR_SXS_INVALID_ASSEMBLY_IDENTITY_ATTRIBUTE",
  sDescription =    "The manifest contains an attribute for the assembly identity which is not valid.");
fAddWindowsDefine("ERROR_SXS_MANIFEST_MISSING_REQUIRED_DEFAULT_NAMESPACE",
  sDescription =    "The manifest is missing the required default namespace specification on the assembly element.");
fAddWindowsDefine("ERROR_SXS_MANIFEST_INVALID_REQUIRED_DEFAULT_NAMESPACE",
  sDescription =    "The manifest has a default namespace specified on the assembly element but its value is not \"urn:schemas-microsoft-com:asm.v1\".");
fAddWindowsDefine("ERROR_SXS_PRIVATE_MANIFEST_CROSS_PATH_WITH_REPARSE_POINT",
  sDescription =    "The private manifest probed has crossed a path with an unsupported reparse point.");
fAddWindowsDefine("ERROR_SXS_DUPLICATE_DLL_NAME",
  sDescription =    "Two or more components referenced directly or indirectly by the application manifest have files by the same name.");
fAddWindowsDefine("ERROR_SXS_DUPLICATE_WINDOWCLASS_NAME",
  sDescription =    "Two or more components referenced directly or indirectly by the application manifest have window classes with the same name.");
fAddWindowsDefine("ERROR_SXS_DUPLICATE_CLSID",
  sDescription =    "Two or more components referenced directly or indirectly by the application manifest have the same COM server CLSIDs.");
fAddWindowsDefine("ERROR_SXS_DUPLICATE_IID",
  sDescription =    "Two or more components referenced directly or indirectly by the application manifest have proxies for the same COM interface IIDs.");
fAddWindowsDefine("ERROR_SXS_DUPLICATE_TLBID",
  sDescription =    "Two or more components referenced directly or indirectly by the application manifest have the same COM type library TLBIDs.");
fAddWindowsDefine("ERROR_SXS_DUPLICATE_PROGID",
  sDescription =    "Two or more components referenced directly or indirectly by the application manifest have the same COM ProgIDs.");
fAddWindowsDefine("ERROR_SXS_DUPLICATE_ASSEMBLY_NAME",
  sDescription =    "Two or more components referenced directly or indirectly by the application manifest are different versions of the same component which is not permitted.");
fAddWindowsDefine("ERROR_SXS_FILE_HASH_MISMATCH",
  sDescription =    "A component's file does not match the verification information present in the component manifest.");
fAddWindowsDefine("ERROR_SXS_POLICY_PARSE_ERROR",
  sDescription =    "The policy manifest contains one or more syntax errors.");
fAddWindowsDefine("ERROR_SXS_XML_E_MISSINGQUOTE",
  sDescription =    "Manifest Parse Error : A string literal was expected, but no opening quote character was found.");
fAddWindowsDefine("ERROR_SXS_XML_E_COMMENTSYNTAX",
  sDescription =    "Manifest Parse Error : Incorrect syntax was used in a comment.");
fAddWindowsDefine("ERROR_SXS_XML_E_BADSTARTNAMECHAR",
  sDescription =    "Manifest Parse Error : A name was started with an invalid character.");
fAddWindowsDefine("ERROR_SXS_XML_E_BADNAMECHAR",
  sDescription =    "Manifest Parse Error : A name contained an invalid character.");
fAddWindowsDefine("ERROR_SXS_XML_E_BADCHARINSTRING",
  sDescription =    "Manifest Parse Error : A string literal contained an invalid character.");
fAddWindowsDefine("ERROR_SXS_XML_E_XMLDECLSYNTAX",
  sDescription =    "Manifest Parse Error : Invalid syntax for an xml declaration.");
fAddWindowsDefine("ERROR_SXS_XML_E_BADCHARDATA",
  sDescription =    "Manifest Parse Error : An Invalid character was found in text content.");
fAddWindowsDefine("ERROR_SXS_XML_E_MISSINGWHITESPACE",
  sDescription =    "Manifest Parse Error : Required white space was missing.");
fAddWindowsDefine("ERROR_SXS_XML_E_EXPECTINGTAGEND",
  sDescription =    "Manifest Parse Error : The character '>' was expected.");
fAddWindowsDefine("ERROR_SXS_XML_E_MISSINGSEMICOLON",
  sDescription =    "Manifest Parse Error : A semi colon character was expected.");
fAddWindowsDefine("ERROR_SXS_XML_E_UNBALANCEDPAREN",
  sDescription =    "Manifest Parse Error : Unbalanced parentheses.");
fAddWindowsDefine("ERROR_SXS_XML_E_INTERNALERROR",
  sDescription =    "Manifest Parse Error : Internal error.");
fAddWindowsDefine("ERROR_SXS_XML_E_UNEXPECTED_WHITESPACE",
  sDescription =    "Manifest Parse Error : Whitespace is not allowed at this location.");
fAddWindowsDefine("ERROR_SXS_XML_E_INCOMPLETE_ENCODING",
  sDescription =    "Manifest Parse Error : End of file reached in invalid state for current encoding.");
fAddWindowsDefine("ERROR_SXS_XML_E_MISSING_PAREN",
  sDescription =    "Manifest Parse Error : Missing parenthesis.");
fAddWindowsDefine("ERROR_SXS_XML_E_EXPECTINGCLOSEQUOTE",
  sDescription =    "Manifest Parse Error : A single or double closing quote character (' or \") is missing.");
fAddWindowsDefine("ERROR_SXS_XML_E_MULTIPLE_COLONS",
  sDescription =    "Manifest Parse Error : Multiple colons are not allowed in a name.");
fAddWindowsDefine("ERROR_SXS_XML_E_INVALID_DECIMAL",
  sDescription =    "Manifest Parse Error : Invalid character for decimal digit.");
fAddWindowsDefine("ERROR_SXS_XML_E_INVALID_HEXIDECIMAL",
  sDescription =    "Manifest Parse Error : Invalid character for hexadecimal digit.");
fAddWindowsDefine("ERROR_SXS_XML_E_INVALID_UNICODE",
  sDescription =    "Manifest Parse Error : Invalid unicode character value for this platform.");
fAddWindowsDefine("ERROR_SXS_XML_E_WHITESPACEORQUESTIONMARK",
  sDescription =    "Manifest Parse Error : Expecting whitespace or '?'.");
fAddWindowsDefine("ERROR_SXS_XML_E_UNEXPECTEDENDTAG",
  sDescription =    "Manifest Parse Error : End tag was not expected at this location.");
fAddWindowsDefine("ERROR_SXS_XML_E_UNCLOSEDTAG",
  sDescription =    "Manifest Parse Error : The following tags were not closed: %1.");
fAddWindowsDefine("ERROR_SXS_XML_E_DUPLICATEATTRIBUTE",
  sDescription =    "Manifest Parse Error : Duplicate attribute.");
fAddWindowsDefine("ERROR_SXS_XML_E_MULTIPLEROOTS",
  sDescription =    "Manifest Parse Error : Only one top level element is allowed in an XML document.");
fAddWindowsDefine("ERROR_SXS_XML_E_INVALIDATROOTLEVEL",
  sDescription =    "Manifest Parse Error : Invalid at the top level of the document.");
fAddWindowsDefine("ERROR_SXS_XML_E_BADXMLDECL",
  sDescription =    "Manifest Parse Error : Invalid xml declaration.");
fAddWindowsDefine("ERROR_SXS_XML_E_MISSINGROOT",
  sDescription =    "Manifest Parse Error : XML document must have a top level element.");
fAddWindowsDefine("ERROR_SXS_XML_E_UNEXPECTEDEOF",
  sDescription =    "Manifest Parse Error : Unexpected end of file.");
fAddWindowsDefine("ERROR_SXS_XML_E_BADPEREFINSUBSET",
  sDescription =    "Manifest Parse Error : Parameter entities cannot be used inside markup declarations in an internal subset.");
fAddWindowsDefine("ERROR_SXS_XML_E_UNCLOSEDSTARTTAG",
  sDescription =    "Manifest Parse Error : Element was not closed.");
fAddWindowsDefine("ERROR_SXS_XML_E_UNCLOSEDENDTAG",
  sDescription =    "Manifest Parse Error : End element was missing the character '>'.");
fAddWindowsDefine("ERROR_SXS_XML_E_UNCLOSEDSTRING",
  sDescription =    "Manifest Parse Error : A string literal was not closed.");
fAddWindowsDefine("ERROR_SXS_XML_E_UNCLOSEDCOMMENT",
  sDescription =    "Manifest Parse Error : A comment was not closed.");
fAddWindowsDefine("ERROR_SXS_XML_E_UNCLOSEDDECL",
  sDescription =    "Manifest Parse Error : A declaration was not closed.");
fAddWindowsDefine("ERROR_SXS_XML_E_UNCLOSEDCDATA",
  sDescription =    "Manifest Parse Error : A CDATA section was not closed.");
fAddWindowsDefine("ERROR_SXS_XML_E_RESERVEDNAMESPACE",
  sDescription =    "Manifest Parse Error : The namespace prefix is not allowed to start with the reserved string \"xml\".");
fAddWindowsDefine("ERROR_SXS_XML_E_INVALIDENCODING",
  sDescription =    "Manifest Parse Error : System does not support the specified encoding.");
fAddWindowsDefine("ERROR_SXS_XML_E_INVALIDSWITCH",
  sDescription =    "Manifest Parse Error : Switch from current encoding to specified encoding not supported.");
fAddWindowsDefine("ERROR_SXS_XML_E_BADXMLCASE",
  sDescription =    "Manifest Parse Error : The name 'xml' is reserved and must be lower case.");
fAddWindowsDefine("ERROR_SXS_XML_E_INVALID_STANDALONE",
  sDescription =    "Manifest Parse Error : The standalone attribute must have the value 'yes' or 'no'.");
fAddWindowsDefine("ERROR_SXS_XML_E_UNEXPECTED_STANDALONE",
  sDescription =    "Manifest Parse Error : The standalone attribute cannot be used in external entities.");
fAddWindowsDefine("ERROR_SXS_XML_E_INVALID_VERSION",
  sDescription =    "Manifest Parse Error : Invalid version number.");
fAddWindowsDefine("ERROR_SXS_XML_E_MISSINGEQUALS",
  sDescription =    "Manifest Parse Error : Missing equals sign between attribute and attribute value.");
fAddWindowsDefine("ERROR_SXS_PROTECTION_RECOVERY_FAILED",
  sDescription =    "Assembly Protection Error : Unable to recover the specified assembly.");
fAddWindowsDefine("ERROR_SXS_PROTECTION_PUBLIC_KEY_TOO_SHORT",
  sDescription =    "Assembly Protection Error : The public key for an assembly was too short to be allowed.");
fAddWindowsDefine("ERROR_SXS_PROTECTION_CATALOG_NOT_VALID",
  sDescription =    "Assembly Protection Error : The catalog for an assembly is not valid, or does not match the assembly's manifest.");
fAddWindowsDefine("ERROR_SXS_UNTRANSLATABLE_HRESULT",
  sDescription =    "An HRESULT could not be translated to a corresponding Win32 error code.");
fAddWindowsDefine("ERROR_SXS_PROTECTION_CATALOG_FILE_MISSING",
  sDescription =    "Assembly Protection Error : The catalog for an assembly is missing.");
fAddWindowsDefine("ERROR_SXS_MISSING_ASSEMBLY_IDENTITY_ATTRIBUTE",
  sDescription =    "The supplied assembly identity is missing one or more attributes which must be present in this context.");
fAddWindowsDefine("ERROR_SXS_INVALID_ASSEMBLY_IDENTITY_ATTRIBUTE_NAME",
  sDescription =    "The supplied assembly identity has one or more attribute names that contain characters not permitted in XML names.");
fAddWindowsDefine("ERROR_SXS_ASSEMBLY_MISSING",
  sDescription =    "The referenced assembly could not be found.");
fAddWindowsDefine("ERROR_SXS_CORRUPT_ACTIVATION_STACK",
  sDescription =    "The activation context activation stack for the running thread of execution is corrupt.");
fAddWindowsDefine("ERROR_SXS_CORRUPTION",
  sDescription =    "The application isolation metadata for this process or thread has become corrupt.");
fAddWindowsDefine("ERROR_SXS_EARLY_DEACTIVATION",
  sDescription =    "The activation context being deactivated is not the most recently activated one.");
fAddWindowsDefine("ERROR_SXS_INVALID_DEACTIVATION",
  sDescription =    "The activation context being deactivated is not active for the current thread of execution.");
fAddWindowsDefine("ERROR_SXS_MULTIPLE_DEACTIVATION",
  sDescription =    "The activation context being deactivated has already been deactivated.");
fAddWindowsDefine("ERROR_SXS_PROCESS_TERMINATION_REQUESTED",
  sDescription =    "A component used by the isolation facility has requested to terminate the process.");
fAddWindowsDefine("ERROR_SXS_RELEASE_ACTIVATION_CONTEXT",
  sDescription =    "A kernel mode component is releasing a reference on an activation context.");
fAddWindowsDefine("ERROR_SXS_SYSTEM_DEFAULT_ACTIVATION_CONTEXT_EMPTY",
  sDescription =    "The activation context of system default assembly could not be generated.");
fAddWindowsDefine("ERROR_SXS_INVALID_IDENTITY_ATTRIBUTE_VALUE",
  sDescription =    "The value of an attribute in an identity is not within the legal range.");
fAddWindowsDefine("ERROR_SXS_INVALID_IDENTITY_ATTRIBUTE_NAME",
  sDescription =    "The name of an attribute in an identity is not within the legal range.");
fAddWindowsDefine("ERROR_SXS_IDENTITY_DUPLICATE_ATTRIBUTE",
  sDescription =    "An identity contains two definitions for the same attribute.");
fAddWindowsDefine("ERROR_SXS_IDENTITY_PARSE_ERROR",
  sDescription =    "The identity string is malformed. This may be due to a trailing comma, more than two unnamed attributes, missing attribute name or missing attribute value.");
fAddWindowsDefine("ERROR_MALFORMED_SUBSTITUTION_STRING",
  sDescription =    "A string containing localized substitutable content was malformed. Either a dollar sign ($) was followed by something other than a left parenthesis or another dollar sign or an substitution's right parenthesis was not found.");
fAddWindowsDefine("ERROR_SXS_INCORRECT_PUBLIC_KEY_TOKEN",
  sDescription =    "The public key token does not correspond to the public key specified.");
fAddWindowsDefine("ERROR_UNMAPPED_SUBSTITUTION_STRING",
  sDescription =    "A substitution string had no mapping.");
fAddWindowsDefine("ERROR_SXS_ASSEMBLY_NOT_LOCKED",
  sDescription =    "The component must be locked before making the request.");
fAddWindowsDefine("ERROR_SXS_COMPONENT_STORE_CORRUPT",
  sDescription =    "The component store has been corrupted.");
fAddWindowsDefine("ERROR_ADVANCED_INSTALLER_FAILED",
  sDescription =    "An advanced installer failed during setup or servicing.");
fAddWindowsDefine("ERROR_XML_ENCODING_MISMATCH",
  sDescription =    "The character encoding in the XML declaration did not match the encoding used in the document.");
fAddWindowsDefine("ERROR_SXS_MANIFEST_IDENTITY_SAME_BUT_CONTENTS_DIFFERENT",
  sDescription =    "The identities of the manifests are identical but their contents are different.");
fAddWindowsDefine("ERROR_SXS_IDENTITIES_DIFFERENT",
  sDescription =    "The component identities are different.");
fAddWindowsDefine("ERROR_SXS_ASSEMBLY_IS_NOT_A_DEPLOYMENT",
  sDescription =    "The assembly is not a deployment.");
fAddWindowsDefine("ERROR_SXS_FILE_NOT_PART_OF_ASSEMBLY",
  sDescription =    "The file is not a part of the assembly.");
fAddWindowsDefine("ERROR_SXS_MANIFEST_TOO_BIG",
  sDescription =    "The size of the manifest exceeds the maximum allowed.");
fAddWindowsDefine("ERROR_SXS_SETTING_NOT_REGISTERED",
  sDescription =    "The setting is not registered.");
fAddWindowsDefine("ERROR_SXS_TRANSACTION_CLOSURE_INCOMPLETE",
  sDescription =    "One or more required members of the transaction are not present.");
fAddWindowsDefine("ERROR_SMI_PRIMITIVE_INSTALLER_FAILED",
  sDescription =    "The SMI primitive installer failed during setup or servicing.");
fAddWindowsDefine("ERROR_GENERIC_COMMAND_FAILED",
  sDescription =    "A generic command executable returned a result that indicates failure.");
fAddWindowsDefine("ERROR_SXS_FILE_HASH_MISSING",
  sDescription =    "A component is missing file verification information in its manifest.");
fAddWindowsDefine("ERROR_EVT_INVALID_CHANNEL_PATH",
  sDescription =    "The specified channel path is invalid.");
fAddWindowsDefine("ERROR_EVT_INVALID_QUERY",
  sDescription =    "The specified query is invalid.");
fAddWindowsDefine("ERROR_EVT_PUBLISHER_METADATA_NOT_FOUND",
  sDescription =    "The publisher metadata cannot be found in the resource.");
fAddWindowsDefine("ERROR_EVT_EVENT_TEMPLATE_NOT_FOUND",
  sDescription =    "The template for an event definition cannot be found in the resource (error = %1).");
fAddWindowsDefine("ERROR_EVT_INVALID_PUBLISHER_NAME",
  sDescription =    "The specified publisher name is invalid.");
fAddWindowsDefine("ERROR_EVT_INVALID_EVENT_DATA",
  sDescription =    "The event data raised by the publisher is not compatible with the event template definition in the publisher's manifest");
fAddWindowsDefine("ERROR_EVT_CHANNEL_NOT_FOUND",
  sDescription =    "The specified channel could not be found. Check channel configuration.");
fAddWindowsDefine("ERROR_EVT_MALFORMED_XML_TEXT",
  sDescription =    "The specified xml text was not well-formed. See Extended Error for more details.");
fAddWindowsDefine("ERROR_EVT_SUBSCRIPTION_TO_DIRECT_CHANNEL",
  sDescription =    "The caller is trying to subscribe to a direct channel which is not allowed. The events for a direct channel go directly to a logfile and cannot be subscribed to.");
fAddWindowsDefine("ERROR_EVT_CONFIGURATION_ERROR",
  sDescription =    "Configuration error.");
fAddWindowsDefine("ERROR_EVT_QUERY_RESULT_STALE",
  sDescription =    "The query result is stale / invalid. This may be due to the log being cleared or rolling over after the query result was created. Users should handle this code by releasing the query result object and reissuing the query.");
fAddWindowsDefine("ERROR_EVT_QUERY_RESULT_INVALID_POSITION",
  sDescription =    "Query result is currently at an invalid position.");
fAddWindowsDefine("ERROR_EVT_NON_VALIDATING_MSXML",
  sDescription =    "Registered MSXML doesn't support validation.");
fAddWindowsDefine("ERROR_EVT_FILTER_ALREADYSCOPED",
  sDescription =    "An expression can only be followed by a change of scope operation if it itself evaluates to a node set and is not already part of some other change of scope operation.");
fAddWindowsDefine("ERROR_EVT_FILTER_NOTELTSET",
  sDescription =    "Can't perform a step operation from a term that does not represent an element set.");
fAddWindowsDefine("ERROR_EVT_FILTER_INVARG",
  sDescription =    "Left hand side arguments to binary operators must be either attributes, nodes or variables and right hand side arguments must be constants.");
fAddWindowsDefine("ERROR_EVT_FILTER_INVTEST",
  sDescription =    "A step operation must involve either a node test or, in the case of a predicate, an algebraic expression against which to test each node in the node set identified by the preceeding node set can be evaluated.");
fAddWindowsDefine("ERROR_EVT_FILTER_INVTYPE",
  sDescription =    "This data type is currently unsupported.");
fAddWindowsDefine("ERROR_EVT_FILTER_PARSEERR",
  sDescription =    "A syntax error occurred at position %1!d!");
fAddWindowsDefine("ERROR_EVT_FILTER_UNSUPPORTEDOP",
  sDescription =    "This operator is unsupported by this implementation of the filter.");
fAddWindowsDefine("ERROR_EVT_FILTER_UNEXPECTEDTOKEN",
  sDescription =    "The token encountered was unexpected.");
fAddWindowsDefine("ERROR_EVT_INVALID_OPERATION_OVER_ENABLED_DIRECT_CHANNEL",
  sDescription =    "The requested operation cannot be performed over an enabled direct channel. The channel must first be disabled before performing the requested operation.");
fAddWindowsDefine("ERROR_EVT_INVALID_CHANNEL_PROPERTY_VALUE",
  sDescription =    "Channel property %1!s! contains invalid value. The value has invalid type, is outside of valid range, can't be updated or is not supported by this type of channel.");
fAddWindowsDefine("ERROR_EVT_INVALID_PUBLISHER_PROPERTY_VALUE",
  sDescription =    "Publisher property %1!s! contains invalid value. The value has invalid type, is outside of valid range, can't be updated or is not supported by this type of publisher.");
fAddWindowsDefine("ERROR_EVT_CHANNEL_CANNOT_ACTIVATE",
  sDescription =    "The channel fails to activate.");
fAddWindowsDefine("ERROR_EVT_FILTER_TOO_COMPLEX",
  sDescription =    "The xpath expression exceeded supported complexity. Please symplify it or split it into two or more simple expressions.");
fAddWindowsDefine("ERROR_EVT_MESSAGE_NOT_FOUND",
  sDescription =    "the message resource is present but the message is not found in the string/message table");
fAddWindowsDefine("ERROR_EVT_MESSAGE_ID_NOT_FOUND",
  sDescription =    "The message id for the desired message could not be found.");
fAddWindowsDefine("ERROR_EVT_UNRESOLVED_VALUE_INSERT",
  sDescription =    "The substitution string for insert index (%1) could not be found.");
fAddWindowsDefine("ERROR_EVT_UNRESOLVED_PARAMETER_INSERT",
  sDescription =    "The description string for parameter reference (%1) could not be found.");
fAddWindowsDefine("ERROR_EVT_MAX_INSERTS_REACHED",
  sDescription =    "The maximum number of replacements has been reached.");
fAddWindowsDefine("ERROR_EVT_EVENT_DEFINITION_NOT_FOUND",
  sDescription =    "The event definition could not be found for event id (%1).");
fAddWindowsDefine("ERROR_EVT_MESSAGE_LOCALE_NOT_FOUND",
  sDescription =    "The locale specific resource for the desired message is not present.");
fAddWindowsDefine("ERROR_EVT_VERSION_TOO_OLD",
  sDescription =    "The resource is too old to be compatible.");
fAddWindowsDefine("ERROR_EVT_VERSION_TOO_NEW",
  sDescription =    "The resource is too new to be compatible.");
fAddWindowsDefine("ERROR_EVT_CANNOT_OPEN_CHANNEL_OF_QUERY",
  sDescription =    "The channel at index %1!d! of the query can't be opened.");
fAddWindowsDefine("ERROR_EVT_PUBLISHER_DISABLED",
  sDescription =    "The publisher has been disabled and its resource is not available. This usually occurs when the publisher is in the process of being uninstalled or upgraded.");
fAddWindowsDefine("ERROR_EVT_FILTER_OUT_OF_RANGE",
  sDescription =    "Attempted to create a numeric type that is outside of its valid range.");
fAddWindowsDefine("ERROR_EC_SUBSCRIPTION_CANNOT_ACTIVATE",
  sDescription =    "The subscription fails to activate.");
fAddWindowsDefine("ERROR_EC_LOG_DISABLED",
  sDescription =    "The log of the subscription is in disabled state, and can not be used to forward events to. The log must first be enabled before the subscription can be activated.");
fAddWindowsDefine("ERROR_EC_CIRCULAR_FORWARDING",
  sDescription =    "When forwarding events from local machine to itself, the query of the subscription can't contain target log of the subscription.");
fAddWindowsDefine("ERROR_EC_CREDSTORE_FULL",
  sDescription =    "The credential store that is used to save credentials is full.");
fAddWindowsDefine("ERROR_EC_CRED_NOT_FOUND",
  sDescription =    "The credential used by this subscription can't be found in credential store.");
fAddWindowsDefine("ERROR_EC_NO_ACTIVE_CHANNEL",
  sDescription =    "No active channel is found for the query.");
fAddWindowsDefine("ERROR_MUI_FILE_NOT_FOUND",
  sDescription =    "The resource loader failed to find MUI file.");
fAddWindowsDefine("ERROR_MUI_INVALID_FILE",
  sDescription =    "The resource loader failed to load MUI file because the file fail to pass validation.");
fAddWindowsDefine("ERROR_MUI_INVALID_RC_CONFIG",
  sDescription =    "The RC Manifest is corrupted with garbage data or unsupported version or missing required item.");
fAddWindowsDefine("ERROR_MUI_INVALID_LOCALE_NAME",
  sDescription =    "The RC Manifest has invalid culture name.");
fAddWindowsDefine("ERROR_MUI_INVALID_ULTIMATEFALLBACK_NAME",
  sDescription =    "The RC Manifest has invalid ultimatefallback name.");
fAddWindowsDefine("ERROR_MUI_FILE_NOT_LOADED",
  sDescription =    "The resource loader cache doesn't have loaded MUI entry.");
fAddWindowsDefine("ERROR_RESOURCE_ENUM_USER_STOP",
  sDescription =    "User stopped resource enumeration.");
fAddWindowsDefine("ERROR_MUI_INTLSETTINGS_UILANG_NOT_INSTALLED",
  sDescription =    "UI language installation failed.");
fAddWindowsDefine("ERROR_MUI_INTLSETTINGS_INVALID_LOCALE_NAME",
  sDescription =    "Locale installation failed.");
fAddWindowsDefine("ERROR_MRM_RUNTIME_NO_DEFAULT_OR_NEUTRAL_RESOURCE",
  sDescription =    "A resource does not have default or neutral value.");
fAddWindowsDefine("ERROR_MRM_INVALID_PRICONFIG",
  sDescription =    "Invalid PRI config file.");
fAddWindowsDefine("ERROR_MRM_INVALID_FILE_TYPE",
  sDescription =    "Invalid file type.");
fAddWindowsDefine("ERROR_MRM_UNKNOWN_QUALIFIER",
  sDescription =    "Unknown qualifier.");
fAddWindowsDefine("ERROR_MRM_INVALID_QUALIFIER_VALUE",
  sDescription =    "Invalid qualifier value.");
fAddWindowsDefine("ERROR_MRM_NO_CANDIDATE",
  sDescription =    "No Candidate found.");
fAddWindowsDefine("ERROR_MRM_NO_MATCH_OR_DEFAULT_CANDIDATE",
  sDescription =    "The ResourceMap or NamedResource has an item that does not have default or neutral resource..");
fAddWindowsDefine("ERROR_MRM_RESOURCE_TYPE_MISMATCH",
  sDescription =    "Invalid ResourceCandidate type.");
fAddWindowsDefine("ERROR_MRM_DUPLICATE_MAP_NAME",
  sDescription =    "Duplicate Resource Map.");
fAddWindowsDefine("ERROR_MRM_DUPLICATE_ENTRY",
  sDescription =    "Duplicate Entry.");
fAddWindowsDefine("ERROR_MRM_INVALID_RESOURCE_IDENTIFIER",
  sDescription =    "Invalid Resource Identifier.");
fAddWindowsDefine("ERROR_MRM_FILEPATH_TOO_LONG",
  sDescription =    "Filepath too long.");
fAddWindowsDefine("ERROR_MRM_UNSUPPORTED_DIRECTORY_TYPE",
  sDescription =    "Unsupported directory type.");
fAddWindowsDefine("ERROR_MRM_INVALID_PRI_FILE",
  sDescription =    "Invalid PRI File.");
fAddWindowsDefine("ERROR_MRM_NAMED_RESOURCE_NOT_FOUND",
  sDescription =    "NamedResource Not Found.");
fAddWindowsDefine("ERROR_MRM_MAP_NOT_FOUND",
  sDescription =    "ResourceMap Not Found.");
fAddWindowsDefine("ERROR_MRM_UNSUPPORTED_PROFILE_TYPE",
  sDescription =    "Unsupported MRT profile type.");
fAddWindowsDefine("ERROR_MRM_INVALID_QUALIFIER_OPERATOR",
  sDescription =    "Invalid qualifier operator.");
fAddWindowsDefine("ERROR_MRM_INDETERMINATE_QUALIFIER_VALUE",
  sDescription =    "Unable to determine qualifier value or qualifier value has not been set.");
fAddWindowsDefine("ERROR_MRM_AUTOMERGE_ENABLED",
  sDescription =    "Automerge is enabled in the PRI file.");
fAddWindowsDefine("ERROR_MRM_TOO_MANY_RESOURCES",
  sDescription =    "Too many resources defined for package.");
fAddWindowsDefine("ERROR_MRM_UNSUPPORTED_FILE_TYPE_FOR_MERGE",
  sDescription =    "Resource File can not be used for merge operation.");
fAddWindowsDefine("ERROR_MRM_UNSUPPORTED_FILE_TYPE_FOR_LOAD_UNLOAD_PRI_FILE",
  sDescription =    "Load/UnloadPriFiles cannot be used with resource packages.");
fAddWindowsDefine("ERROR_MRM_NO_CURRENT_VIEW_ON_THREAD",
  sDescription =    "Resource Contexts may not be created on threads that do not have a CoreWindow.");
fAddWindowsDefine("ERROR_DIFFERENT_PROFILE_RESOURCE_MANAGER_EXIST",
  sDescription =    "The singleton Resource Manager with different profile is already created.");
fAddWindowsDefine("ERROR_OPERATION_NOT_ALLOWED_FROM_SYSTEM_COMPONENT",
  sDescription =    "The system component cannot operate given API operation");
fAddWindowsDefine("ERROR_MRM_DIRECT_REF_TO_NON_DEFAULT_RESOURCE",
  sDescription =    "The resource is a direct reference to a non-default resource candidate.");
fAddWindowsDefine("ERROR_MRM_GENERATION_COUNT_MISMATCH",
  sDescription =    "Resource Map has been re-generated and the query string is not valid anymore.");
fAddWindowsDefine("ERROR_MCA_INVALID_CAPABILITIES_STRING",
  sDescription =    "The monitor returned a DDC/CI capabilities string that did not comply with the ACCESS.bus 3.0, DDC/CI 1.1 or MCCS 2 Revision 1 specification.");
fAddWindowsDefine("ERROR_MCA_INVALID_VCP_VERSION",
  sDescription =    "The monitor's VCP Version (0xDF) VCP code returned an invalid version value.");
fAddWindowsDefine("ERROR_MCA_MONITOR_VIOLATES_MCCS_SPECIFICATION",
  sDescription =    "The monitor does not comply with the MCCS specification it claims to support.");
fAddWindowsDefine("ERROR_MCA_MCCS_VERSION_MISMATCH",
  sDescription =    "The MCCS version in a monitor's mccs_ver capability does not match the MCCS version the monitor reports when the VCP Version (0xDF) VCP code is used.");
fAddWindowsDefine("ERROR_MCA_UNSUPPORTED_MCCS_VERSION",
  sDescription =    "The Monitor Configuration API only works with monitors that support the MCCS 1.0 specification, MCCS 2.0 specification or the MCCS 2.0 Revision 1 specification.");
fAddWindowsDefine("ERROR_MCA_INTERNAL_ERROR",
  sDescription =    "An internal Monitor Configuration API error occurred.");
fAddWindowsDefine("ERROR_MCA_INVALID_TECHNOLOGY_TYPE_RETURNED",
  sDescription =    "The monitor returned an invalid monitor technology type. CRT, Plasma and LCD (TFT) are examples of monitor technology types. This error implies that the monitor violated the MCCS 2.0 or MCCS 2.0 Revision 1 specification.");
fAddWindowsDefine("ERROR_MCA_UNSUPPORTED_COLOR_TEMPERATURE",
  sDescription =    "The caller of SetMonitorColorTemperature specified a color temperature that the current monitor did not support. This error implies that the monitor violated the MCCS 2.0 or MCCS 2.0 Revision 1 specification.");
fAddWindowsDefine("ERROR_AMBIGUOUS_SYSTEM_DEVICE",
  sDescription =    "The requested system device cannot be identified due to multiple indistinguishable devices potentially matching the identification criteria.");
fAddWindowsDefine("ERROR_SYSTEM_DEVICE_NOT_FOUND",
  sDescription =    "The requested system device cannot be found.");
fAddWindowsDefine("ERROR_HASH_NOT_SUPPORTED",
  sDescription =    "Hash generation for the specified hash version and hash type is not enabled on the server.");
fAddWindowsDefine("ERROR_HASH_NOT_PRESENT",
  sDescription =    "The hash requested from the server is not available or no longer valid.");
fAddWindowsDefine("ERROR_SECONDARY_IC_PROVIDER_NOT_REGISTERED",
  sDescription =    "The secondary interrupt controller instance that manages the specified interrupt is not registered.");
fAddWindowsDefine("ERROR_GPIO_CLIENT_INFORMATION_INVALID",
  sDescription =    "The information supplied by the GPIO client driver is invalid.");
fAddWindowsDefine("ERROR_GPIO_VERSION_NOT_SUPPORTED",
  sDescription =    "The version specified by the GPIO client driver is not supported.");
fAddWindowsDefine("ERROR_GPIO_INVALID_REGISTRATION_PACKET",
  sDescription =    "The registration packet supplied by the GPIO client driver is not valid.");
fAddWindowsDefine("ERROR_GPIO_OPERATION_DENIED",
  sDescription =    "The requested operation is not suppported for the specified handle.");
fAddWindowsDefine("ERROR_GPIO_INCOMPATIBLE_CONNECT_MODE",
  sDescription =    "The requested connect mode conflicts with an existing mode on one or more of the specified pins.");
fAddWindowsDefine("ERROR_GPIO_INTERRUPT_ALREADY_UNMASKED",
  sDescription =    "The interrupt requested to be unmasked is not masked.");
fAddWindowsDefine("ERROR_CANNOT_SWITCH_RUNLEVEL",
  sDescription =    "The requested run level switch cannot be completed successfully.");
fAddWindowsDefine("ERROR_INVALID_RUNLEVEL_SETTING",
  sDescription =    "The service has an invalid run level setting. The run level for a service must not be higher than the run level of its dependent services.");
fAddWindowsDefine("ERROR_RUNLEVEL_SWITCH_TIMEOUT",
  sDescription =    "The requested run level switch cannot be completed successfully since one or more services will not stop or restart within the specified timeout.");
fAddWindowsDefine("ERROR_RUNLEVEL_SWITCH_AGENT_TIMEOUT",
  sDescription =    "A run level switch agent did not respond within the specified timeout.");
fAddWindowsDefine("ERROR_RUNLEVEL_SWITCH_IN_PROGRESS",
  sDescription =    "A run level switch is currently in progress.");
fAddWindowsDefine("ERROR_SERVICES_FAILED_AUTOSTART",
  sDescription =    "One or more services failed to start during the service startup phase of a run level switch.");
fAddWindowsDefine("ERROR_COM_TASK_STOP_PENDING",
  sDescription =    "The task stop request cannot be completed immediately since task needs more time to shutdown.");
fAddWindowsDefine("ERROR_INSTALL_OPEN_PACKAGE_FAILED",
  sDescription =    "Package could not be opened.");
fAddWindowsDefine("ERROR_INSTALL_PACKAGE_NOT_FOUND",
  sDescription =    "Package was not found.");
fAddWindowsDefine("ERROR_INSTALL_INVALID_PACKAGE",
  sDescription =    "Package data is invalid.");
fAddWindowsDefine("ERROR_INSTALL_RESOLVE_DEPENDENCY_FAILED",
  sDescription =    "Package failed updates, dependency or conflict validation.");
fAddWindowsDefine("ERROR_INSTALL_OUT_OF_DISK_SPACE",
  sDescription =    "There is not enough disk space on your computer. Please free up some space and try again.");
fAddWindowsDefine("ERROR_INSTALL_NETWORK_FAILURE",
  sDescription =    "There was a problem downloading your product.");
fAddWindowsDefine("ERROR_INSTALL_REGISTRATION_FAILURE",
  sDescription =    "Package could not be registered.");
fAddWindowsDefine("ERROR_INSTALL_DEREGISTRATION_FAILURE",
  sDescription =    "Package could not be unregistered.");
fAddWindowsDefine("ERROR_INSTALL_CANCEL",
  sDescription =    "User cancelled the install request.");
fAddWindowsDefine("ERROR_INSTALL_FAILED",
  sDescription =    "Install failed. Please contact your software vendor.");
fAddWindowsDefine("ERROR_REMOVE_FAILED",
  sDescription =    "Removal failed. Please contact your software vendor.");
fAddWindowsDefine("ERROR_PACKAGE_ALREADY_EXISTS",
  sDescription =    "The provided package is already installed, and reinstallation of the package was blocked. Check the AppXDeployment-Server event log for details.");
fAddWindowsDefine("ERROR_NEEDS_REMEDIATION",
  sDescription =    "The application cannot be started. Try reinstalling the application to fix the problem.");
fAddWindowsDefine("ERROR_INSTALL_PREREQUISITE_FAILED",
  sDescription =    "A Prerequisite for an install could not be satisfied.");
fAddWindowsDefine("ERROR_PACKAGE_REPOSITORY_CORRUPTED",
  sDescription =    "The package repository is corrupted.");
fAddWindowsDefine("ERROR_INSTALL_POLICY_FAILURE",
  sDescription =    "To install this application you need either a Windows developer license or a sideloading-enabled system.");
fAddWindowsDefine("ERROR_PACKAGE_UPDATING",
  sDescription =    "The application cannot be started because it is currently updating.");
fAddWindowsDefine("ERROR_DEPLOYMENT_BLOCKED_BY_POLICY",
  sDescription =    "The package deployment operation is blocked by policy. Please contact your system administrator.");
fAddWindowsDefine("ERROR_PACKAGES_IN_USE",
  sDescription =    "The package could not be installed because resources it modifies are currently in use.");
fAddWindowsDefine("ERROR_RECOVERY_FILE_CORRUPT",
  sDescription =    "The package could not be recovered because necessary data for recovery have been corrupted.");
fAddWindowsDefine("ERROR_INVALID_STAGED_SIGNATURE",
  sDescription =    "The signature is invalid. To register in developer mode, AppxSignature.p7x and AppxBlockMap.xml must be valid or should not be present.");
fAddWindowsDefine("ERROR_DELETING_EXISTING_APPLICATIONDATA_STORE_FAILED",
  sDescription =    "An error occurred while deleting the package's previously existing application data.");
fAddWindowsDefine("ERROR_INSTALL_PACKAGE_DOWNGRADE",
  sDescription =    "The package could not be installed because a higher version of this package is already installed.");
fAddWindowsDefine("ERROR_SYSTEM_NEEDS_REMEDIATION",
  sDescription =    "An error in a system binary was detected. Try refreshing the PC to fix the problem.");
fAddWindowsDefine("ERROR_APPX_INTEGRITY_FAILURE_CLR_NGEN",
  sDescription =    "A corrupted CLR NGEN binary was detected on the system.");
fAddWindowsDefine("ERROR_RESILIENCY_FILE_CORRUPT",
  sDescription =    "The operation could not be resumed because necessary data for recovery have been corrupted.");
fAddWindowsDefine("ERROR_INSTALL_FIREWALL_SERVICE_NOT_RUNNING",
  sDescription =    "The package could not be installed because the Windows Firewall service is not running. Enable the Windows Firewall service and try again.");
fAddWindowsDefine("ERROR_PACKAGE_MOVE_FAILED",
  sDescription =    "Package move failed.");
fAddWindowsDefine("ERROR_INSTALL_VOLUME_NOT_EMPTY",
  sDescription =    "The deployment operation failed because the volume is not empty.");
fAddWindowsDefine("ERROR_INSTALL_VOLUME_OFFLINE",
  sDescription =    "The deployment operation failed because the volume is offline.");
fAddWindowsDefine("ERROR_INSTALL_VOLUME_CORRUPT",
  sDescription =    "The deployment operation failed because the specified volume is corrupt.");
fAddWindowsDefine("ERROR_NEEDS_REGISTRATION",
  sDescription =    "The deployment operation failed because the specified application needs to be registered first.");
fAddWindowsDefine("ERROR_INSTALL_WRONG_PROCESSOR_ARCHITECTURE",
  sDescription =    "The deployment operation failed because the package targets the wrong processor architecture.");
fAddWindowsDefine("ERROR_DEV_SIDELOAD_LIMIT_EXCEEDED",
  sDescription =    "You have reached the maximum number of developer sideloaded packages allowed on this device. Please uninstall a sideloaded package and try again.");
fAddWindowsDefine("APPMODEL_ERROR_NO_PACKAGE",
  sDescription =    "The process has no package identity.");
fAddWindowsDefine("APPMODEL_ERROR_PACKAGE_RUNTIME_CORRUPT",
  sDescription =    "The package runtime information is corrupted.");
fAddWindowsDefine("APPMODEL_ERROR_PACKAGE_IDENTITY_CORRUPT",
  sDescription =    "The package identity is corrupted.");
fAddWindowsDefine("APPMODEL_ERROR_NO_APPLICATION",
  sDescription =    "The process has no application identity.");
fAddWindowsDefine("APPMODEL_ERROR_DYNAMIC_PROPERTY_READ_FAILED",
  sDescription =    "One or more AppModel Runtime group policy values could not be read. Please contact your system administrator with the contents of your AppModel Runtime event log.");
fAddWindowsDefine("APPMODEL_ERROR_DYNAMIC_PROPERTY_INVALID",
  sDescription =    "One or more AppModel Runtime group policy values are invalid. Please contact your system administrator with the contents of your AppModel Runtime event log.");
fAddWindowsDefine("APPMODEL_ERROR_PACKAGE_NOT_AVAILABLE",
  sDescription =    "The package is currently not available.");
fAddWindowsDefine("ERROR_STATE_LOAD_STORE_FAILED",
  sDescription =    "Loading the state store failed.");
fAddWindowsDefine("ERROR_STATE_GET_VERSION_FAILED",
  sDescription =    "Retrieving the state version for the application failed.");
fAddWindowsDefine("ERROR_STATE_SET_VERSION_FAILED",
  sDescription =    "Setting the state version for the application failed.");
fAddWindowsDefine("ERROR_STATE_STRUCTURED_RESET_FAILED",
  sDescription =    "Resetting the structured state of the application failed.");
fAddWindowsDefine("ERROR_STATE_OPEN_CONTAINER_FAILED",
  sDescription =    "State Manager failed to open the container.");
fAddWindowsDefine("ERROR_STATE_CREATE_CONTAINER_FAILED",
  sDescription =    "State Manager failed to create the container.");
fAddWindowsDefine("ERROR_STATE_DELETE_CONTAINER_FAILED",
  sDescription =    "State Manager failed to delete the container.");
fAddWindowsDefine("ERROR_STATE_READ_SETTING_FAILED",
  sDescription =    "State Manager failed to read the setting.");
fAddWindowsDefine("ERROR_STATE_WRITE_SETTING_FAILED",
  sDescription =    "State Manager failed to write the setting.");
fAddWindowsDefine("ERROR_STATE_DELETE_SETTING_FAILED",
  sDescription =    "State Manager failed to delete the setting.");
fAddWindowsDefine("ERROR_STATE_QUERY_SETTING_FAILED",
  sDescription =    "State Manager failed to query the setting.");
fAddWindowsDefine("ERROR_STATE_READ_COMPOSITE_SETTING_FAILED",
  sDescription =    "State Manager failed to read the composite setting.");
fAddWindowsDefine("ERROR_STATE_WRITE_COMPOSITE_SETTING_FAILED",
  sDescription =    "State Manager failed to write the composite setting.");
fAddWindowsDefine("ERROR_STATE_ENUMERATE_CONTAINER_FAILED",
  sDescription =    "State Manager failed to enumerate the containers.");
fAddWindowsDefine("ERROR_STATE_ENUMERATE_SETTINGS_FAILED",
  sDescription =    "State Manager failed to enumerate the settings.");
fAddWindowsDefine("ERROR_STATE_COMPOSITE_SETTING_VALUE_SIZE_LIMIT_EXCEEDED",
  sDescription =    "The size of the state manager composite setting value has exceeded the limit.");
fAddWindowsDefine("ERROR_STATE_SETTING_VALUE_SIZE_LIMIT_EXCEEDED",
  sDescription =    "The size of the state manager setting value has exceeded the limit.");
fAddWindowsDefine("ERROR_STATE_SETTING_NAME_SIZE_LIMIT_EXCEEDED",
  sDescription =    "The length of the state manager setting name has exceeded the limit.");
fAddWindowsDefine("ERROR_STATE_CONTAINER_NAME_SIZE_LIMIT_EXCEEDED",
  sDescription =    "The length of the state manager container name has exceeded the limit.");
fAddWindowsDefine("ERROR_API_UNAVAILABLE",
  sDescription =    "This API cannot be used in the context of the caller's application type.");
fAddWindowsDefine("STORE_ERROR_UNLICENSED",
  sDescription =    "This PC does not have a valid license for the application or product.");
fAddWindowsDefine("STORE_ERROR_UNLICENSED_USER",
  sDescription =    "The authenticated user does not have a valid license for the application or product.");
fAddWindowsDefine("STORE_ERROR_PENDING_COM_TRANSACTION",
  sDescription =    "The commerce transaction associated with this license is still pending verification.");
fAddWindowsDefine("STORE_ERROR_LICENSE_REVOKED",
  sDescription =    "The license has been revoked for this user");
fAddWindowsDefine("STATUS_CLUSTER_NODE_ALREADY_UP",
  sDescription =    "The cluster node is already up.");
fAddWindowsDefine("STATUS_CLUSTER_NODE_ALREADY_DOWN",
  sDescription =    "The cluster node is already down.");
fAddWindowsDefine("STATUS_CLUSTER_NETWORK_ALREADY_ONLINE",
  sDescription =    "The cluster network is already online.");
fAddWindowsDefine("STATUS_CLUSTER_NETWORK_ALREADY_OFFLINE",
  sDescription =    "The cluster network is already offline.");
fAddWindowsDefine("STATUS_CLUSTER_NODE_ALREADY_MEMBER",
  sDescription =    "The cluster node is already a member of the cluster.");
fAddWindowsDefine("STATUS_COULD_NOT_RESIZE_LOG",
  sDescription =    "The log could not be set to the requested size.");
fAddWindowsDefine("STATUS_NO_TXF_METADATA",
  sDescription =    "There is no transaction metadata on the file.");
fAddWindowsDefine("STATUS_CANT_RECOVER_WITH_HANDLE_OPEN",
  sDescription =    "The file cannot be recovered because there is a handle still open on it.");
fAddWindowsDefine("STATUS_TXF_METADATA_ALREADY_PRESENT",
  sDescription =    "Transaction metadata is already present on this file and cannot be superseded.");
fAddWindowsDefine("STATUS_TRANSACTION_SCOPE_CALLBACKS_NOT_SET",
  sDescription =    "A transaction scope could not be entered because the scope handler has not been initialized.");
fAddWindowsDefine("STATUS_VIDEO_HUNG_DISPLAY_DRIVER_THREAD_RECOVERED",
  sDescription =    "The %hs display driver has stopped working normally. The recovery had been performed.");
fAddWindowsDefine("STATUS_FLT_BUFFER_TOO_SMALL",
  sDescription =    "The buffer is too small to contain the entry. No information has been written to the buffer.");
fAddWindowsDefine("STATUS_FVE_PARTIAL_METADATA",
  sDescription =    "Volume metadata read or write is incomplete.");
fAddWindowsDefine("STATUS_FVE_TRANSIENT_STATE",
  sDescription =    "BitLocker encryption keys were ignored because the volume was in a transient state.");
fAddWindowsDefine("E_XAMLPARSEFAILED",
  sDescription =    "XAML parsing failed.");
fAddWindowsDefine("E_LAYOUTCYCLE",
  sDescription =    "XAML: Layout cycle detected. Layout could not complete.");
fAddWindowsDefine("E_ELEMENTNOTAVAILABLE",
  sDescription =    "XAML: Element not available.");
fAddWindowsDefine("E_ELEMENTNOTENABLED",
  sDescription =    "XAML: The operation is not allowed on a nonenabled element.");
fAddWindowsDefine("E_UNKNOWNTYPE",
  sDescription =    "XAML: Unknown error type.");
fAddWindowsDefine("STATUS_UNSUCCESSFUL",
  sDescription =    "The requested operation was unsuccessful.");
fAddWindowsDefine("STATUS_NOT_IMPLEMENTED",
  sDescription =    "The requested operation is not implemented.",
  sTypeId =         "PureCall",
                             sSecurityImpact = "May be a security issue");
fAddWindowsDefine("STATUS_INVALID_INFO_CLASS",
  sDescription =    "The specified information class is not a valid information class for the specified object.");
fAddWindowsDefine("STATUS_INFO_LENGTH_MISMATCH",
  sDescription =    "The specified information record length does not match the length that is required for the specified information class.");
fAddWindowsDefine("STATUS_ACCESS_VIOLATION",
  sDescription =    "The instruction at 0x%08lx referenced memory at 0x%08lx. The memory could not be %s.",
  sTypeId =         "AV",
                             sSecurityImpact = "May be a security issue");
fAddWindowsDefine("STATUS_IN_PAGE_ERROR",
  sDescription =    "The instruction at 0x%08lx referenced memory at 0x%08lx. The required data was not placed into memory because of an I/O error status of 0x%08lx.");
fAddWindowsDefine("STATUS_PAGEFILE_QUOTA",
  sDescription =    "The page file quota for the process has been exhausted.");
fAddWindowsDefine("STATUS_INVALID_HANDLE",
  sDescription =    "An invalid HANDLE was specified.");
fAddWindowsDefine("STATUS_BAD_INITIAL_STACK",
  sDescription =    "An invalid initial stack was specified in a call to NtCreateThread.");
fAddWindowsDefine("STATUS_BAD_INITIAL_PC",
  sDescription =    "An invalid initial start address was specified in a call to NtCreateThread.");
fAddWindowsDefine("STATUS_INVALID_CID",
  sDescription =    "An invalid client ID was specified.");
fAddWindowsDefine("STATUS_TIMER_NOT_CANCELED",
  sDescription =    "An attempt was made to cancel or set a timer that has an associated APC and the specified thread is not the thread that originally set the timer with an associated APC routine.");
fAddWindowsDefine("STATUS_INVALID_PARAMETER",
  sDescription =    "An invalid parameter was passed to a service or function.");
fAddWindowsDefine("STATUS_NO_SUCH_DEVICE",
  sDescription =    "A device that does not exist was specified.");
fAddWindowsDefine("STATUS_NO_SUCH_FILE",
  sDescription =    "The file %hs does not exist.");
fAddWindowsDefine("STATUS_INVALID_DEVICE_REQUEST",
  sDescription =    "The specified request is not a valid operation for the target device.");
fAddWindowsDefine("STATUS_END_OF_FILE",
  sDescription =    "The end-of-file marker has been reached. There is no valid data in the file beyond this marker.");
fAddWindowsDefine("STATUS_WRONG_VOLUME",
  sDescription =    "The wrong volume is in the drive. Insert volume %hs into drive %hs.");
fAddWindowsDefine("STATUS_NO_MEDIA_IN_DEVICE",
  sDescription =    "There is no disk in the drive. Insert a disk into drive %hs.");
fAddWindowsDefine("STATUS_UNRECOGNIZED_MEDIA",
  sDescription =    "The disk in drive %hs is not formatted properly. Check the disk, and reformat it, if needed.");
fAddWindowsDefine("STATUS_NONEXISTENT_SECTOR",
  sDescription =    "The specified sector does not exist.");
fAddWindowsDefine("STATUS_MORE_PROCESSING_REQUIRED",
  sDescription =    "The specified I/O request packet (IRP) cannot be disposed of because the I/O operation is not complete.");
fAddWindowsDefine("STATUS_NO_MEMORY",
  sDescription =    "Not enough virtual memory or paging file quota is available to complete the specified operation.",
  sTypeId =         "OOM");
fAddWindowsDefine("STATUS_CONFLICTING_ADDRESSES",
  sDescription =    "The specified address range conflicts with the address space.");
fAddWindowsDefine("STATUS_NOT_MAPPED_VIEW",
  sDescription =    "The address range to unmap is not a mapped view.");
fAddWindowsDefine("STATUS_UNABLE_TO_FREE_VM",
  sDescription =    "The virtual memory cannot be freed.");
fAddWindowsDefine("STATUS_UNABLE_TO_DELETE_SECTION",
  sDescription =    "The specified section cannot be deleted.");
fAddWindowsDefine("STATUS_INVALID_SYSTEM_SERVICE",
  sDescription =    "An invalid system service was specified in a system service call.");
fAddWindowsDefine("STATUS_ILLEGAL_INSTRUCTION",
  sDescription =    "Illegal Instruction An attempt was made to execute an illegal instruction.",
  sTypeId =         "IllegalInstruction",
                             sSecurityImpact = "May be a security issue, as it could indicate the instruction pointer was corrupted");
fAddWindowsDefine("STATUS_INVALID_LOCK_SEQUENCE",
  sDescription =    "An attempt was made to execute an invalid lock sequence.");
fAddWindowsDefine("STATUS_INVALID_VIEW_SIZE",
  sDescription =    "An attempt was made to create a view for a section that is bigger than the section.");
fAddWindowsDefine("STATUS_INVALID_FILE_FOR_SECTION",
  sDescription =    "The attributes of the specified mapping file for a section of memory cannot be read.");
fAddWindowsDefine("STATUS_ALREADY_COMMITTED",
  sDescription =    "The specified address range is already committed.");
fAddWindowsDefine("STATUS_ACCESS_DENIED",
  sDescription =    "A process has requested access to an object but has not been granted those access rights.");
fAddWindowsDefine("STATUS_BUFFER_TOO_SMALL",
  sDescription =    "The buffer is too small to contain the entry. No information has been written to the buffer.");
fAddWindowsDefine("STATUS_OBJECT_TYPE_MISMATCH",
  sDescription =    "There is a mismatch between the type of object that is required by the requested operation and the type of object that is specified in the request.");
fAddWindowsDefine("STATUS_NONCONTINUABLE_EXCEPTION",
  sDescription =    "Cannot Continue Windows cannot continue from this exception.");
fAddWindowsDefine("STATUS_INVALID_DISPOSITION",
  sDescription =    "An invalid exception disposition was returned by an exception handler.");
fAddWindowsDefine("STATUS_UNWIND",
  sDescription =    "Unwind exception code.");
fAddWindowsDefine("STATUS_BAD_STACK",
  sDescription =    "An invalid or unaligned stack was encountered during an unwind operation.");
fAddWindowsDefine("STATUS_INVALID_UNWIND_TARGET",
  sDescription =    "An invalid unwind target was encountered during an unwind operation.");
fAddWindowsDefine("STATUS_NOT_LOCKED",
  sDescription =    "An attempt was made to unlock a page of memory that was not locked.");
fAddWindowsDefine("STATUS_PARITY_ERROR",
  sDescription =    "A device parity error on an I/O operation.");
fAddWindowsDefine("STATUS_UNABLE_TO_DECOMMIT_VM",
  sDescription =    "An attempt was made to decommit uncommitted virtual memory.");
fAddWindowsDefine("STATUS_NOT_COMMITTED",
  sDescription =    "An attempt was made to change the attributes on memory that has not been committed.");
fAddWindowsDefine("STATUS_INVALID_PORT_ATTRIBUTES",
  sDescription =    "Invalid object attributes specified to NtCreatePort or invalid port attributes specified to NtConnectPort.");
fAddWindowsDefine("STATUS_PORT_MESSAGE_TOO_LONG",
  sDescription =    "The length of the message that was passed to NtRequestPort or NtRequestWaitReplyPort is longer than the maximum message that is allowed by the port.");
fAddWindowsDefine("STATUS_INVALID_PARAMETER_MIX",
  sDescription =    "An invalid combination of parameters was specified.");
fAddWindowsDefine("STATUS_INVALID_QUOTA_LOWER",
  sDescription =    "An attempt was made to lower a quota limit below the current usage.");
fAddWindowsDefine("STATUS_DISK_CORRUPT_ERROR",
  sDescription =    "The file system structure on the disk is corrupt and unusable. Run the Chkdsk utility on the volume %hs.");
fAddWindowsDefine("STATUS_OBJECT_NAME_INVALID",
  sDescription =    "The object name is invalid.");
fAddWindowsDefine("STATUS_OBJECT_NAME_NOT_FOUND",
  sDescription =    "The object name is not found.");
fAddWindowsDefine("STATUS_OBJECT_NAME_COLLISION",
  sDescription =    "The object name already exists.");
fAddWindowsDefine("STATUS_PORT_DISCONNECTED",
  sDescription =    "An attempt was made to send a message to a disconnected communication port.");
fAddWindowsDefine("STATUS_DEVICE_ALREADY_ATTACHED",
  sDescription =    "An attempt was made to attach to a device that was already attached to another device.");
fAddWindowsDefine("STATUS_OBJECT_PATH_INVALID",
  sDescription =    "The object path component was not a directory object.");
fAddWindowsDefine("STATUS_OBJECT_PATH_NOT_FOUND",
  sDescription =    "The path %hs does not exist.");
fAddWindowsDefine("STATUS_OBJECT_PATH_SYNTAX_BAD",
  sDescription =    "The object path component was not a directory object.");
fAddWindowsDefine("STATUS_DATA_OVERRUN",
  sDescription =    "A data overrun error occurred.");
fAddWindowsDefine("STATUS_DATA_LATE_ERROR",
  sDescription =    "A data late error occurred.");
fAddWindowsDefine("STATUS_DATA_ERROR",
  sDescription =    "An error occurred in reading or writing data.");
fAddWindowsDefine("STATUS_CRC_ERROR",
  sDescription =    "A cyclic redundancy check (CRC) checksum error occurred.");
fAddWindowsDefine("STATUS_SECTION_TOO_BIG",
  sDescription =    "The specified section is too big to map the file.");
fAddWindowsDefine("STATUS_PORT_CONNECTION_REFUSED",
  sDescription =    "The NtConnectPort request is refused.");
fAddWindowsDefine("STATUS_INVALID_PORT_HANDLE",
  sDescription =    "The type of port handle is invalid for the operation that is requested.");
fAddWindowsDefine("STATUS_SHARING_VIOLATION",
  sDescription =    "A file cannot be opened because the share access flags are incompatible.");
fAddWindowsDefine("STATUS_QUOTA_EXCEEDED",
  sDescription =    "Insufficient quota exists to complete the operation.");
fAddWindowsDefine("STATUS_INVALID_PAGE_PROTECTION",
  sDescription =    "The specified page protection was not valid.");
fAddWindowsDefine("STATUS_MUTANT_NOT_OWNED",
  sDescription =    "An attempt to release a mutant object was made by a thread that was not the owner of the mutant object.");
fAddWindowsDefine("STATUS_SEMAPHORE_LIMIT_EXCEEDED",
  sDescription =    "An attempt was made to release a semaphore such that its maximum count would have been exceeded.");
fAddWindowsDefine("STATUS_PORT_ALREADY_SET",
  sDescription =    "An attempt was made to set the DebugPort or ExceptionPort of a process, but a port already exists in the process, or an attempt was made to set the CompletionPort of a file but a port was already set in the file, or an attempt was made to set the associated completion port of an ALPC port but it is already set.");
fAddWindowsDefine("STATUS_SECTION_NOT_IMAGE",
  sDescription =    "An attempt was made to query image information on a section that does not map an image.");
fAddWindowsDefine("STATUS_SUSPEND_COUNT_EXCEEDED",
  sDescription =    "An attempt was made to suspend a thread whose suspend count was at its maximum.");
fAddWindowsDefine("STATUS_THREAD_IS_TERMINATING",
  sDescription =    "An attempt was made to suspend a thread that has begun termination.");
fAddWindowsDefine("STATUS_BAD_WORKING_SET_LIMIT",
  sDescription =    "An attempt was made to set the working set limit to an invalid value (for example, the minimum greater than maximum).");
fAddWindowsDefine("STATUS_INCOMPATIBLE_FILE_MAP",
  sDescription =    "A section was created to map a file that is not compatible with an already existing section that maps the same file.");
fAddWindowsDefine("STATUS_SECTION_PROTECTION",
  sDescription =    "A view to a section specifies a protection that is incompatible with the protection of the initial view.");
fAddWindowsDefine("STATUS_EAS_NOT_SUPPORTED",
  sDescription =    "An operation involving EAs failed because the file system does not support EAs.");
fAddWindowsDefine("STATUS_EA_TOO_LARGE",
  sDescription =    "An EA operation failed because the EA set is too large.");
fAddWindowsDefine("STATUS_NONEXISTENT_EA_ENTRY",
  sDescription =    "An EA operation failed because the name or EA index is invalid.");
fAddWindowsDefine("STATUS_NO_EAS_ON_FILE",
  sDescription =    "The file for which EAs were requested has no EAs.");
fAddWindowsDefine("STATUS_EA_CORRUPT_ERROR",
  sDescription =    "The EA is corrupt and cannot be read.");
fAddWindowsDefine("STATUS_FILE_LOCK_CONFLICT",
  sDescription =    "A requested read/write cannot be granted due to a conflicting file lock.");
fAddWindowsDefine("STATUS_LOCK_NOT_GRANTED",
  sDescription =    "A requested file lock cannot be granted due to other existing locks.");
fAddWindowsDefine("STATUS_DELETE_PENDING",
  sDescription =    "A non-close operation has been requested of a file object that has a delete pending.");
fAddWindowsDefine("STATUS_CTL_FILE_NOT_SUPPORTED",
  sDescription =    "An attempt was made to set the control attribute on a file. This attribute is not supported in the destination file system.");
fAddWindowsDefine("STATUS_UNKNOWN_REVISION",
  sDescription =    "Indicates a revision number that was encountered or specified is not one that is known by the service. It might be a more recent revision than the service is aware of.");
fAddWindowsDefine("STATUS_REVISION_MISMATCH",
  sDescription =    "Indicates that two revision levels are incompatible.");
fAddWindowsDefine("STATUS_INVALID_OWNER",
  sDescription =    "Indicates a particular security ID cannot be assigned as the owner of an object.");
fAddWindowsDefine("STATUS_INVALID_PRIMARY_GROUP",
  sDescription =    "Indicates a particular security ID cannot be assigned as the primary group of an object.");
fAddWindowsDefine("STATUS_NO_IMPERSONATION_TOKEN",
  sDescription =    "An attempt has been made to operate on an impersonation token by a thread that is not currently impersonating a client.");
fAddWindowsDefine("STATUS_CANT_DISABLE_MANDATORY",
  sDescription =    "A mandatory group cannot be disabled.");
fAddWindowsDefine("STATUS_NO_LOGON_SERVERS",
  sDescription =    "No logon servers are currently available to service the logon request.");
fAddWindowsDefine("STATUS_NO_SUCH_LOGON_SESSION",
  sDescription =    "A specified logon session does not exist. It might already have been terminated.");
fAddWindowsDefine("STATUS_NO_SUCH_PRIVILEGE",
  sDescription =    "A specified privilege does not exist.");
fAddWindowsDefine("STATUS_PRIVILEGE_NOT_HELD",
  sDescription =    "A required privilege is not held by the client.");
fAddWindowsDefine("STATUS_INVALID_ACCOUNT_NAME",
  sDescription =    "The name provided is not a properly formed account name.");
fAddWindowsDefine("STATUS_USER_EXISTS",
  sDescription =    "The specified account already exists.");
fAddWindowsDefine("STATUS_NO_SUCH_USER",
  sDescription =    "The specified account does not exist.");
fAddWindowsDefine("STATUS_GROUP_EXISTS",
  sDescription =    "The specified group already exists.");
fAddWindowsDefine("STATUS_NO_SUCH_GROUP",
  sDescription =    "The specified group does not exist.");
fAddWindowsDefine("STATUS_MEMBER_IN_GROUP",
  sDescription =    "The specified user account is already in the specified group account. Also used to indicate a group cannot be deleted because it contains a member.");
fAddWindowsDefine("STATUS_MEMBER_NOT_IN_GROUP",
  sDescription =    "The specified user account is not a member of the specified group account.");
fAddWindowsDefine("STATUS_LAST_ADMIN",
  sDescription =    "Indicates the requested operation would disable or delete the last remaining administration account. This is not allowed to prevent creating a situation in which the system cannot be administrated.");
fAddWindowsDefine("STATUS_WRONG_PASSWORD",
  sDescription =    "When trying to update a password, this return status indicates that the value provided as the current password is not correct.");
fAddWindowsDefine("STATUS_ILL_FORMED_PASSWORD",
  sDescription =    "When trying to update a password, this return status indicates that the value provided for the new password contains values that are not allowed in passwords.");
fAddWindowsDefine("STATUS_PASSWORD_RESTRICTION",
  sDescription =    "When trying to update a password, this status indicates that some password update rule has been violated. For example, the password might not meet length criteria.");
fAddWindowsDefine("STATUS_LOGON_FAILURE",
  sDescription =    "The attempted logon is invalid. This is either due to a bad username or authentication information.");
fAddWindowsDefine("STATUS_ACCOUNT_RESTRICTION",
  sDescription =    "Indicates a referenced user name and authentication information are valid, but some user account restriction has prevented successful authentication (such as time-of-day restrictions).");
fAddWindowsDefine("STATUS_INVALID_LOGON_HOURS",
  sDescription =    "The user account has time restrictions and cannot be logged onto at this time.");
fAddWindowsDefine("STATUS_INVALID_WORKSTATION",
  sDescription =    "The user account is restricted so that it cannot be used to log on from the source workstation.");
fAddWindowsDefine("STATUS_PASSWORD_EXPIRED",
  sDescription =    "The user account password has expired.");
fAddWindowsDefine("STATUS_ACCOUNT_DISABLED",
  sDescription =    "The referenced account is currently disabled and cannot be logged on to.");
fAddWindowsDefine("STATUS_NONE_MAPPED",
  sDescription =    "None of the information to be translated has been translated.");
fAddWindowsDefine("STATUS_TOO_MANY_LUIDS_REQUESTED",
  sDescription =    "The number of LUIDs requested cannot be allocated with a single allocation.");
fAddWindowsDefine("STATUS_LUIDS_EXHAUSTED",
  sDescription =    "Indicates there are no more LUIDs to allocate.");
fAddWindowsDefine("STATUS_INVALID_SUB_AUTHORITY",
  sDescription =    "Indicates the sub-authority value is invalid for the particular use.");
fAddWindowsDefine("STATUS_INVALID_ACL",
  sDescription =    "Indicates the ACL structure is not valid.");
fAddWindowsDefine("STATUS_INVALID_SID",
  sDescription =    "Indicates the SID structure is not valid.");
fAddWindowsDefine("STATUS_INVALID_SECURITY_DESCR",
  sDescription =    "Indicates the SECURITY_DESCRIPTOR structure is not valid.");
fAddWindowsDefine("STATUS_PROCEDURE_NOT_FOUND",
  sDescription =    "Indicates the specified procedure address cannot be found in the DLL.");
fAddWindowsDefine("STATUS_INVALID_IMAGE_FORMAT",
  sDescription =    "%hs is either not designed to run on Windows or it contains an error. Try installing the program again using the original installation media or contact your system administrator or the software vendor for support.");
fAddWindowsDefine("STATUS_NO_TOKEN",
  sDescription =    "An attempt was made to reference a token that does not exist. This is typically done by referencing the token that is associated with a thread when the thread is not impersonating a client.");
fAddWindowsDefine("STATUS_BAD_INHERITANCE_ACL",
  sDescription =    "Indicates that an attempt to build either an inherited ACL or ACE was not successful. This can be caused by a number of things. One of the more probable causes is the replacement of a CreatorId with a SID that did not fit into the ACE or ACL.");
fAddWindowsDefine("STATUS_RANGE_NOT_LOCKED",
  sDescription =    "The range specified in NtUnlockFile was not locked.");
fAddWindowsDefine("STATUS_DISK_FULL",
  sDescription =    "An operation failed because the disk was full.");
fAddWindowsDefine("STATUS_SERVER_DISABLED",
  sDescription =    "The GUID allocation server is disabled at the moment.");
fAddWindowsDefine("STATUS_SERVER_NOT_DISABLED",
  sDescription =    "The GUID allocation server is enabled at the moment.");
fAddWindowsDefine("STATUS_TOO_MANY_GUIDS_REQUESTED",
  sDescription =    "Too many GUIDs were requested from the allocation server at once.");
fAddWindowsDefine("STATUS_GUIDS_EXHAUSTED",
  sDescription =    "The GUIDs could not be allocated because the Authority Agent was exhausted.");
fAddWindowsDefine("STATUS_INVALID_ID_AUTHORITY",
  sDescription =    "The value provided was an invalid value for an identifier authority.");
fAddWindowsDefine("STATUS_AGENTS_EXHAUSTED",
  sDescription =    "No more authority agent values are available for the particular identifier authority value.");
fAddWindowsDefine("STATUS_INVALID_VOLUME_LABEL",
  sDescription =    "An invalid volume label has been specified.");
fAddWindowsDefine("STATUS_SECTION_NOT_EXTENDED",
  sDescription =    "A mapped section could not be extended.");
fAddWindowsDefine("STATUS_NOT_MAPPED_DATA",
  sDescription =    "Specified section to flush does not map a data file.");
fAddWindowsDefine("STATUS_RESOURCE_DATA_NOT_FOUND",
  sDescription =    "Indicates the specified image file did not contain a resource section.");
fAddWindowsDefine("STATUS_RESOURCE_TYPE_NOT_FOUND",
  sDescription =    "Indicates the specified resource type cannot be found in the image file.");
fAddWindowsDefine("STATUS_RESOURCE_NAME_NOT_FOUND",
  sDescription =    "Indicates the specified resource name cannot be found in the image file.");
fAddWindowsDefine("STATUS_ARRAY_BOUNDS_EXCEEDED",
  sDescription =    "Array bounds exceeded.",
  sTypeId =         "ArrayBounds",
                             sSecurityImpact = "May be a security issue, but probably not exploitable");
fAddWindowsDefine("STATUS_FLOAT_DENORMAL_OPERAND",
  sDescription =    "Floating-point denormal operand.",
  sTypeId =         "FloatDenormalOperand");
fAddWindowsDefine("STATUS_FLOAT_DIVIDE_BY_ZERO",
  sDescription =    "Floating-point division by zero.",
  sTypeId =         "FloatDivideByZero");
fAddWindowsDefine("STATUS_FLOAT_INEXACT_RESULT",
  sDescription =    "Floating-point inexact result.",
  sTypeId =         "FloatInexactResult");
fAddWindowsDefine("STATUS_FLOAT_INVALID_OPERATION",
  sDescription =    "Floating-point invalid operation.",
  sTypeId =         "FloatInvalidOperation");
fAddWindowsDefine("STATUS_FLOAT_OVERFLOW",
  sDescription =    "Floating-point overflow.",
  sTypeId =         "FloatOverflow");
fAddWindowsDefine("STATUS_FLOAT_STACK_CHECK",
  sDescription =    "Floating-point stack check.",
  sTypeId =         "FloatStackCheck");
fAddWindowsDefine("STATUS_FLOAT_UNDERFLOW",
  sDescription =    "Floating-point underflow.",
  sTypeId =         "FloatUnderflow");
fAddWindowsDefine("STATUS_INTEGER_DIVIDE_BY_ZERO",
  sDescription =    "Integer division by zero.",
  sTypeId =         "IntegerDivideByZero");
fAddWindowsDefine("STATUS_INTEGER_OVERFLOW",
  sDescription =    "Integer overflow.",
  sTypeId =         "IntegerOverflow");
fAddWindowsDefine("STATUS_PRIVILEGED_INSTRUCTION",
  sDescription =    "Privileged instruction.",
  sTypeId =         "PrivilegedInstruction",
                             sSecurityImpact = "May be a security issue, as it could indicate the instruction pointer was corrupted");
fAddWindowsDefine("STATUS_TOO_MANY_PAGING_FILES",
  sDescription =    "An attempt was made to install more paging files than the system supports.");
fAddWindowsDefine("STATUS_FILE_INVALID",
  sDescription =    "The volume for a file has been externally altered such that the opened file is no longer valid.");
fAddWindowsDefine("STATUS_ALLOTTED_SPACE_EXCEEDED",
  sDescription =    "When a block of memory is allotted for future updates, such as the memory allocated to hold discretionary access control and primary group information, successive updates might exceed the amount of memory originally allotted. Because a quota might already have been charged to several processes that have handles to the object, it is not reasonable to alter the size of the allocated memory. Instead, a request that requires more memory than has been allotted must fail and the STATUS_ALLOTTED_SPACE_EXCEEDED error returned.");
fAddWindowsDefine("STATUS_INSUFFICIENT_RESOURCES",
  sDescription =    "Insufficient system resources exist to complete the API.");
fAddWindowsDefine("STATUS_DFS_EXIT_PATH_FOUND",
  sDescription =    "An attempt has been made to open a DFS exit path control file.");
fAddWindowsDefine("STATUS_DEVICE_DATA_ERROR",
  sDescription =    "There are bad blocks (sectors) on the hard disk.");
fAddWindowsDefine("STATUS_DEVICE_NOT_CONNECTED",
  sDescription =    "There is bad cabling, non-termination, or the controller is not able to obtain access to the hard disk.");
fAddWindowsDefine("STATUS_FREE_VM_NOT_AT_BASE",
  sDescription =    "Virtual memory cannot be freed because the base address is not the base of the region and a region size of zero was specified.");
fAddWindowsDefine("STATUS_MEMORY_NOT_ALLOCATED",
  sDescription =    "An attempt was made to free virtual memory that is not allocated.");
fAddWindowsDefine("STATUS_WORKING_SET_QUOTA",
  sDescription =    "The working set is not big enough to allow the requested pages to be locked.");
fAddWindowsDefine("STATUS_MEDIA_WRITE_PROTECTED",
  sDescription =    "The disk cannot be written to because it is write-protected. Remove the write protection from the volume %hs in drive %hs.");
fAddWindowsDefine("STATUS_DEVICE_NOT_READY",
  sDescription =    "The drive is not ready for use; its door might be open. Check drive %hs and make sure that a disk is inserted and that the drive door is closed.");
fAddWindowsDefine("STATUS_INVALID_GROUP_ATTRIBUTES",
  sDescription =    "The specified attributes are invalid or are incompatible with the attributes for the group as a whole.");
fAddWindowsDefine("STATUS_BAD_IMPERSONATION_LEVEL",
  sDescription =    "A specified impersonation level is invalid. Also used to indicate that a required impersonation level was not provided.");
fAddWindowsDefine("STATUS_CANT_OPEN_ANONYMOUS",
  sDescription =    "An attempt was made to open an anonymous-level token. Anonymous tokens cannot be opened.");
fAddWindowsDefine("STATUS_BAD_VALIDATION_CLASS",
  sDescription =    "The validation information class requested was invalid.");
fAddWindowsDefine("STATUS_BAD_TOKEN_TYPE",
  sDescription =    "The type of a token object is inappropriate for its attempted use.");
fAddWindowsDefine("STATUS_BAD_MASTER_BOOT_RECORD",
  sDescription =    "The type of a token object is inappropriate for its attempted use.");
fAddWindowsDefine("STATUS_INSTRUCTION_MISALIGNMENT",
  sDescription =    "An attempt was made to execute an instruction at an unaligned address and the host system does not support unaligned instruction references.");
fAddWindowsDefine("STATUS_INSTANCE_NOT_AVAILABLE",
  sDescription =    "The maximum named pipe instance count has been reached.");
fAddWindowsDefine("STATUS_PIPE_NOT_AVAILABLE",
  sDescription =    "An instance of a named pipe cannot be found in the listening state.");
fAddWindowsDefine("STATUS_INVALID_PIPE_STATE",
  sDescription =    "The named pipe is not in the connected or closing state.");
fAddWindowsDefine("STATUS_PIPE_BUSY",
  sDescription =    "The specified pipe is set to complete operations and there are current I/O operations queued so that it cannot be changed to queue operations.");
fAddWindowsDefine("STATUS_ILLEGAL_FUNCTION",
  sDescription =    "The specified handle is not open to the server end of the named pipe.");
fAddWindowsDefine("STATUS_PIPE_DISCONNECTED",
  sDescription =    "The specified named pipe is in the disconnected state.");
fAddWindowsDefine("STATUS_PIPE_CLOSING",
  sDescription =    "The specified named pipe is in the closing state.");
fAddWindowsDefine("STATUS_PIPE_CONNECTED",
  sDescription =    "The specified named pipe is in the connected state.");
fAddWindowsDefine("STATUS_PIPE_LISTENING",
  sDescription =    "The specified named pipe is in the listening state.");
fAddWindowsDefine("STATUS_INVALID_READ_MODE",
  sDescription =    "The specified named pipe is not in message mode.");
fAddWindowsDefine("STATUS_IO_TIMEOUT",
  sDescription =    "The specified I/O operation on %hs was not completed before the time-out period expired.");
fAddWindowsDefine("STATUS_FILE_FORCED_CLOSED",
  sDescription =    "The specified file has been closed by another process.");
fAddWindowsDefine("STATUS_PROFILING_NOT_STARTED",
  sDescription =    "Profiling is not started.");
fAddWindowsDefine("STATUS_PROFILING_NOT_STOPPED",
  sDescription =    "Profiling is not stopped.");
fAddWindowsDefine("STATUS_COULD_NOT_INTERPRET",
  sDescription =    "The passed ACL did not contain the minimum required information.");
fAddWindowsDefine("STATUS_FILE_IS_A_DIRECTORY",
  sDescription =    "The file that was specified as a target is a directory, and the caller specified that it could be anything but a directory.");
fAddWindowsDefine("STATUS_NOT_SUPPORTED",
  sDescription =    "The request is not supported.");
fAddWindowsDefine("STATUS_REMOTE_NOT_LISTENING",
  sDescription =    "This remote computer is not listening.");
fAddWindowsDefine("STATUS_DUPLICATE_NAME",
  sDescription =    "A duplicate name exists on the network.");
fAddWindowsDefine("STATUS_BAD_NETWORK_PATH",
  sDescription =    "The network path cannot be located.");
fAddWindowsDefine("STATUS_NETWORK_BUSY",
  sDescription =    "The network is busy.");
fAddWindowsDefine("STATUS_DEVICE_DOES_NOT_EXIST",
  sDescription =    "This device does not exist.");
fAddWindowsDefine("STATUS_TOO_MANY_COMMANDS",
  sDescription =    "The network BIOS command limit has been reached.");
fAddWindowsDefine("STATUS_ADAPTER_HARDWARE_ERROR",
  sDescription =    "An I/O adapter hardware error has occurred.");
fAddWindowsDefine("STATUS_INVALID_NETWORK_RESPONSE",
  sDescription =    "The network responded incorrectly.");
fAddWindowsDefine("STATUS_UNEXPECTED_NETWORK_ERROR",
  sDescription =    "An unexpected network error occurred.");
fAddWindowsDefine("STATUS_BAD_REMOTE_ADAPTER",
  sDescription =    "The remote adapter is not compatible.");
fAddWindowsDefine("STATUS_PRINT_QUEUE_FULL",
  sDescription =    "The print queue is full.");
fAddWindowsDefine("STATUS_NO_SPOOL_SPACE",
  sDescription =    "Space to store the file that is waiting to be printed is not available on the server.");
fAddWindowsDefine("STATUS_PRINT_CANCELLED",
  sDescription =    "The requested print file has been canceled.");
fAddWindowsDefine("STATUS_NETWORK_NAME_DELETED",
  sDescription =    "The network name was deleted.");
fAddWindowsDefine("STATUS_NETWORK_ACCESS_DENIED",
  sDescription =    "Network access is denied.");
fAddWindowsDefine("STATUS_BAD_DEVICE_TYPE",
  sDescription =    "The specified device type (LPT, for example) conflicts with the actual device type on the remote resource.");
fAddWindowsDefine("STATUS_BAD_NETWORK_NAME",
  sDescription =    "The specified share name cannot be found on the remote server.");
fAddWindowsDefine("STATUS_TOO_MANY_NAMES",
  sDescription =    "The name limit for the network adapter card of the local computer was exceeded.");
fAddWindowsDefine("STATUS_TOO_MANY_SESSIONS",
  sDescription =    "The network BIOS session limit was exceeded.");
fAddWindowsDefine("STATUS_SHARING_PAUSED",
  sDescription =    "File sharing has been temporarily paused.");
fAddWindowsDefine("STATUS_REQUEST_NOT_ACCEPTED",
  sDescription =    "No more connections can be made to this remote computer at this time because the computer has already accepted the maximum number of connections.");
fAddWindowsDefine("STATUS_REDIRECTOR_PAUSED",
  sDescription =    "Print or disk redirection is temporarily paused.");
fAddWindowsDefine("STATUS_NET_WRITE_FAULT",
  sDescription =    "A network data fault occurred.");
fAddWindowsDefine("STATUS_PROFILING_AT_LIMIT",
  sDescription =    "The number of active profiling objects is at the maximum and no more can be started.");
fAddWindowsDefine("STATUS_NOT_SAME_DEVICE",
  sDescription =    "The destination file of a rename request is located on a different device than the source of the rename request.");
fAddWindowsDefine("STATUS_FILE_RENAMED",
  sDescription =    "The specified file has been renamed and thus cannot be modified.");
fAddWindowsDefine("STATUS_VIRTUAL_CIRCUIT_CLOSED",
  sDescription =    "The session with a remote server has been disconnected because the time-out interval for a request has expired.");
fAddWindowsDefine("STATUS_NO_SECURITY_ON_OBJECT",
  sDescription =    "Indicates an attempt was made to operate on the security of an object that does not have security associated with it.");
fAddWindowsDefine("STATUS_CANT_WAIT",
  sDescription =    "Used to indicate that an operation cannot continue without blocking for I/O.");
fAddWindowsDefine("STATUS_PIPE_EMPTY",
  sDescription =    "Used to indicate that a read operation was done on an empty pipe.");
fAddWindowsDefine("STATUS_CANT_ACCESS_DOMAIN_INFO",
  sDescription =    "Configuration information could not be read from the domain controller, either because the machine is unavailable or access has been denied.");
fAddWindowsDefine("STATUS_CANT_TERMINATE_SELF",
  sDescription =    "Indicates that a thread attempted to terminate itself by default (called NtTerminateThread with NULL) and it was the last thread in the current process.");
fAddWindowsDefine("STATUS_INVALID_SERVER_STATE",
  sDescription =    "Indicates the Sam Server was in the wrong state to perform the desired operation.");
fAddWindowsDefine("STATUS_INVALID_DOMAIN_STATE",
  sDescription =    "Indicates the domain was in the wrong state to perform the desired operation.");
fAddWindowsDefine("STATUS_INVALID_DOMAIN_ROLE",
  sDescription =    "This operation is only allowed for the primary domain controller of the domain.");
fAddWindowsDefine("STATUS_NO_SUCH_DOMAIN",
  sDescription =    "The specified domain did not exist.");
fAddWindowsDefine("STATUS_DOMAIN_EXISTS",
  sDescription =    "The specified domain already exists.");
fAddWindowsDefine("STATUS_DOMAIN_LIMIT_EXCEEDED",
  sDescription =    "An attempt was made to exceed the limit on the number of domains per server for this release.");
fAddWindowsDefine("STATUS_OPLOCK_NOT_GRANTED",
  sDescription =    "An error status returned when the opportunistic lock (oplock) request is denied.");
fAddWindowsDefine("STATUS_INVALID_OPLOCK_PROTOCOL",
  sDescription =    "An error status returned when an invalid opportunistic lock (oplock) acknowledgment is received by a file system.");
fAddWindowsDefine("STATUS_INTERNAL_DB_CORRUPTION",
  sDescription =    "This error indicates that the requested operation cannot be completed due to a catastrophic media failure or an on-disk data structure corruption.");
fAddWindowsDefine("STATUS_INTERNAL_ERROR",
  sDescription =    "An internal error occurred.");
fAddWindowsDefine("STATUS_GENERIC_NOT_MAPPED",
  sDescription =    "Indicates generic access types were contained in an access mask which should already be mapped to non-generic access types.");
fAddWindowsDefine("STATUS_BAD_DESCRIPTOR_FORMAT",
  sDescription =    "Indicates a security descriptor is not in the necessary format (absolute or self-relative).");
fAddWindowsDefine("STATUS_INVALID_USER_BUFFER",
  sDescription =    "An access to a user buffer failed at an expected point in time. This code is defined because the caller does not want to accept STATUS_ACCESS_VIOLATION in its filter.");
fAddWindowsDefine("STATUS_UNEXPECTED_IO_ERROR",
  sDescription =    "If an I/O error that is not defined in the standard FsRtl filter is returned, it is converted to the following error, which is guaranteed to be in the filter. In this case, information is lost; however, the filter correctly handles the exception.");
fAddWindowsDefine("STATUS_UNEXPECTED_MM_CREATE_ERR",
  sDescription =    "If an MM error that is not defined in the standard FsRtl filter is returned, it is converted to one of the following errors, which are guaranteed to be in the filter. In this case, information is lost; however, the filter correctly handles the exception.");
fAddWindowsDefine("STATUS_UNEXPECTED_MM_MAP_ERROR",
  sDescription =    "If an MM error that is not defined in the standard FsRtl filter is returned, it is converted to one of the following errors, which are guaranteed to be in the filter. In this case, information is lost; however, the filter correctly handles the exception.");
fAddWindowsDefine("STATUS_UNEXPECTED_MM_EXTEND_ERR",
  sDescription =    "If an MM error that is not defined in the standard FsRtl filter is returned, it is converted to one of the following errors, which are guaranteed to be in the filter. In this case, information is lost; however, the filter correctly handles the exception.");
fAddWindowsDefine("STATUS_NOT_LOGON_PROCESS",
  sDescription =    "The requested action is restricted for use by logon processes only. The calling process has not registered as a logon process.");
fAddWindowsDefine("STATUS_LOGON_SESSION_EXISTS",
  sDescription =    "An attempt has been made to start a new session manager or LSA logon session by using an ID that is already in use.");
fAddWindowsDefine("STATUS_INVALID_PARAMETER_1",
  sDescription =    "An invalid parameter was passed to a service or function as the first argument.");
fAddWindowsDefine("STATUS_INVALID_PARAMETER_2",
  sDescription =    "An invalid parameter was passed to a service or function as the second argument.");
fAddWindowsDefine("STATUS_INVALID_PARAMETER_3",
  sDescription =    "An invalid parameter was passed to a service or function as the third argument.");
fAddWindowsDefine("STATUS_INVALID_PARAMETER_4",
  sDescription =    "An invalid parameter was passed to a service or function as the fourth argument.");
fAddWindowsDefine("STATUS_INVALID_PARAMETER_5",
  sDescription =    "An invalid parameter was passed to a service or function as the fifth argument.");
fAddWindowsDefine("STATUS_INVALID_PARAMETER_6",
  sDescription =    "An invalid parameter was passed to a service or function as the sixth argument.");
fAddWindowsDefine("STATUS_INVALID_PARAMETER_7",
  sDescription =    "An invalid parameter was passed to a service or function as the seventh argument.");
fAddWindowsDefine("STATUS_INVALID_PARAMETER_8",
  sDescription =    "An invalid parameter was passed to a service or function as the eighth argument.");
fAddWindowsDefine("STATUS_INVALID_PARAMETER_9",
  sDescription =    "An invalid parameter was passed to a service or function as the ninth argument.");
fAddWindowsDefine("STATUS_INVALID_PARAMETER_10",
  sDescription =    "An invalid parameter was passed to a service or function as the tenth argument.");
fAddWindowsDefine("STATUS_INVALID_PARAMETER_11",
  sDescription =    "An invalid parameter was passed to a service or function as the eleventh argument.");
fAddWindowsDefine("STATUS_INVALID_PARAMETER_12",
  sDescription =    "An invalid parameter was passed to a service or function as the twelfth argument.");
fAddWindowsDefine("STATUS_REDIRECTOR_NOT_STARTED",
  sDescription =    "An attempt was made to access a network file, but the network software was not yet started.");
fAddWindowsDefine("STATUS_REDIRECTOR_STARTED",
  sDescription =    "An attempt was made to start the redirector, but the redirector has already been started.");
fAddWindowsDefine("STATUS_STACK_OVERFLOW",
  sDescription =    "A new guard page for the stack cannot be created.",
  sTypeId =         "StackExhaustion");
fAddWindowsDefine("STATUS_NO_SUCH_PACKAGE",
  sDescription =    "A specified authentication package is unknown.");
fAddWindowsDefine("STATUS_BAD_FUNCTION_TABLE",
  sDescription =    "A malformed function table was encountered during an unwind operation.");
fAddWindowsDefine("STATUS_VARIABLE_NOT_FOUND",
  sDescription =    "Indicates the specified environment variable name was not found in the specified environment block.");
fAddWindowsDefine("STATUS_DIRECTORY_NOT_EMPTY",
  sDescription =    "Indicates that the directory trying to be deleted is not empty.");
fAddWindowsDefine("STATUS_FILE_CORRUPT_ERROR",
  sDescription =    "The file or directory %hs is corrupt and unreadable. Run the Chkdsk utility.");
fAddWindowsDefine("STATUS_NOT_A_DIRECTORY",
  sDescription =    "A requested opened file is not a directory.");
fAddWindowsDefine("STATUS_BAD_LOGON_SESSION_STATE",
  sDescription =    "The logon session is not in a state that is consistent with the requested operation.");
fAddWindowsDefine("STATUS_LOGON_SESSION_COLLISION",
  sDescription =    "An internal LSA error has occurred. An authentication package has requested the creation of a logon session but the ID of an already existing logon session has been specified.");
fAddWindowsDefine("STATUS_NAME_TOO_LONG",
  sDescription =    "A specified name string is too long for its intended use.");
fAddWindowsDefine("STATUS_FILES_OPEN",
  sDescription =    "The user attempted to force close the files on a redirected drive, but there were opened files on the drive, and the user did not specify a sufficient level of force.");
fAddWindowsDefine("STATUS_CONNECTION_IN_USE",
  sDescription =    "The user attempted to force close the files on a redirected drive, but there were opened directories on the drive, and the user did not specify a sufficient level of force.");
fAddWindowsDefine("STATUS_MESSAGE_NOT_FOUND",
  sDescription =    "RtlFindMessage could not locate the requested message ID in the message table resource.");
fAddWindowsDefine("STATUS_PROCESS_IS_TERMINATING",
  sDescription =    "An attempt was made to duplicate an object handle into or out of an exiting process.");
fAddWindowsDefine("STATUS_INVALID_LOGON_TYPE",
  sDescription =    "Indicates an invalid value has been provided for the LogonType requested.");
fAddWindowsDefine("STATUS_NO_GUID_TRANSLATION",
  sDescription =    "Indicates that an attempt was made to assign protection to a file system file or directory and one of the SIDs in the security descriptor could not be translated into a GUID that could be stored by the file system. This causes the protection attempt to fail, which might cause a file creation attempt to fail.");
fAddWindowsDefine("STATUS_CANNOT_IMPERSONATE",
  sDescription =    "Indicates that an attempt has been made to impersonate via a named pipe that has not yet been read from.");
fAddWindowsDefine("STATUS_IMAGE_ALREADY_LOADED",
  sDescription =    "Indicates that the specified image is already loaded.");
fAddWindowsDefine("STATUS_NO_LDT",
  sDescription =    "Indicates that an attempt was made to change the size of the LDT for a process that has no LDT.");
fAddWindowsDefine("STATUS_INVALID_LDT_SIZE",
  sDescription =    "Indicates that an attempt was made to grow an LDT by setting its size, or that the size was not an even number of selectors.");
fAddWindowsDefine("STATUS_INVALID_LDT_OFFSET",
  sDescription =    "Indicates that the starting value for the LDT information was not an integral multiple of the selector size.");
fAddWindowsDefine("STATUS_INVALID_LDT_DESCRIPTOR",
  sDescription =    "Indicates that the user supplied an invalid descriptor when trying to set up LDT descriptors.");
fAddWindowsDefine("STATUS_INVALID_IMAGE_NE_FORMAT",
  sDescription =    "The specified image file did not have the correct format. It appears to be NE format.");
fAddWindowsDefine("STATUS_RXACT_INVALID_STATE",
  sDescription =    "Indicates that the transaction state of a registry subtree is incompatible with the requested operation. For example, a request has been made to start a new transaction with one already in progress, or a request has been made to apply a transaction when one is not currently in progress.");
fAddWindowsDefine("STATUS_RXACT_COMMIT_FAILURE",
  sDescription =    "Indicates an error has occurred during a registry transaction commit. The database has been left in an unknown, but probably inconsistent, state. The state of the registry transaction is left as COMMITTING.");
fAddWindowsDefine("STATUS_MAPPED_FILE_SIZE_ZERO",
  sDescription =    "An attempt was made to map a file of size zero with the maximum size specified as zero.");
fAddWindowsDefine("STATUS_TOO_MANY_OPENED_FILES",
  sDescription =    "Too many files are opened on a remote server. This error should only be returned by the Windows redirector on a remote drive.");
fAddWindowsDefine("STATUS_CANCELLED",
  sDescription =    "The I/O request was canceled.");
fAddWindowsDefine("STATUS_CANNOT_DELETE",
  sDescription =    "An attempt has been made to remove a file or directory that cannot be deleted.");
fAddWindowsDefine("STATUS_INVALID_COMPUTER_NAME",
  sDescription =    "Indicates a name that was specified as a remote computer name is syntactically invalid.");
fAddWindowsDefine("STATUS_FILE_DELETED",
  sDescription =    "An I/O request other than close was performed on a file after it was deleted, which can only happen to a request that did not complete before the last handle was closed via NtClose.");
fAddWindowsDefine("STATUS_SPECIAL_ACCOUNT",
  sDescription =    "Indicates an operation that is incompatible with built-in accounts has been attempted on a built-in (special) SAM account. For example, built-in accounts cannot be deleted.");
fAddWindowsDefine("STATUS_SPECIAL_GROUP",
  sDescription =    "The operation requested cannot be performed on the specified group because it is a built-in special group.");
fAddWindowsDefine("STATUS_SPECIAL_USER",
  sDescription =    "The operation requested cannot be performed on the specified user because it is a built-in special user.");
fAddWindowsDefine("STATUS_MEMBERS_PRIMARY_GROUP",
  sDescription =    "Indicates a member cannot be removed from a group because the group is currently the member's primary group.");
fAddWindowsDefine("STATUS_FILE_CLOSED",
  sDescription =    "An I/O request other than close and several other special case operations was attempted using a file object that had already been closed.");
fAddWindowsDefine("STATUS_TOO_MANY_THREADS",
  sDescription =    "Indicates a process has too many threads to perform the requested action. For example, assignment of a primary token can be performed only when a process has zero or one threads.");
fAddWindowsDefine("STATUS_THREAD_NOT_IN_PROCESS",
  sDescription =    "An attempt was made to operate on a thread within a specific process, but the specified thread is not in the specified process.");
fAddWindowsDefine("STATUS_TOKEN_ALREADY_IN_USE",
  sDescription =    "An attempt was made to establish a token for use as a primary token but the token is already in use. A token can only be the primary token of one process at a time.");
fAddWindowsDefine("STATUS_PAGEFILE_QUOTA_EXCEEDED",
  sDescription =    "The page file quota was exceeded.");
fAddWindowsDefine("STATUS_COMMITMENT_LIMIT",
  sDescription =    "Your system is low on virtual memory. To ensure that Windows runs correctly, increase the size of your virtual memory paging file. For more information, see Help.");
fAddWindowsDefine("STATUS_INVALID_IMAGE_LE_FORMAT",
  sDescription =    "The specified image file did not have the correct format: it appears to be LE format.");
fAddWindowsDefine("STATUS_INVALID_IMAGE_NOT_MZ",
  sDescription =    "The specified image file did not have the correct format: it did not have an initial MZ.");
fAddWindowsDefine("STATUS_INVALID_IMAGE_PROTECT",
  sDescription =    "The specified image file did not have the correct format: it did not have a proper e_lfarlc in the MZ header.");
fAddWindowsDefine("STATUS_INVALID_IMAGE_WIN_16",
  sDescription =    "The specified image file did not have the correct format: it appears to be a 16-bit Windows image.");
fAddWindowsDefine("STATUS_LOGON_SERVER_CONFLICT",
  sDescription =    "The Netlogon service cannot start because another Netlogon service running in the domain conflicts with the specified role.");
fAddWindowsDefine("STATUS_TIME_DIFFERENCE_AT_DC",
  sDescription =    "The time at the primary domain controller is different from the time at the backup domain controller or member server by too large an amount.");
fAddWindowsDefine("STATUS_SYNCHRONIZATION_REQUIRED",
  sDescription =    "The SAM database on a Windows Server operating system is significantly out of synchronization with the copy on the domain controller. A complete synchronization is required.");
fAddWindowsDefine("STATUS_DLL_NOT_FOUND",
  sDescription =    "This application has failed to start because %hs was not found. Reinstalling the application might fix this problem.");
fAddWindowsDefine("STATUS_OPEN_FAILED",
  sDescription =    "The NtCreateFile API failed. This error should never be returned to an application; it is a place holder for the Windows LAN Manager Redirector to use in its internal error-mapping routines.");
fAddWindowsDefine("STATUS_IO_PRIVILEGE_FAILED",
  sDescription =    "The I/O permissions for the process could not be changed.");
fAddWindowsDefine("STATUS_ORDINAL_NOT_FOUND",
  sDescription =    "The ordinal %ld could not be located in the dynamic link library %hs.");
fAddWindowsDefine("STATUS_ENTRYPOINT_NOT_FOUND",
  sDescription =    "The procedure entry point %hs could not be located in the dynamic link library %hs.");
fAddWindowsDefine("STATUS_CONTROL_C_EXIT",
  sDescription =    "The application terminated as a result of a CTRL+C.");
fAddWindowsDefine("STATUS_LOCAL_DISCONNECT",
  sDescription =    "The network transport on your computer has closed a network connection. There might or might not be I/O requests outstanding.");
fAddWindowsDefine("STATUS_REMOTE_DISCONNECT",
  sDescription =    "The network transport on a remote computer has closed a network connection. There might or might not be I/O requests outstanding.");
fAddWindowsDefine("STATUS_REMOTE_RESOURCES",
  sDescription =    "The remote computer has insufficient resources to complete the network request. For example, the remote computer might not have enough available memory to carry out the request at this time.");
fAddWindowsDefine("STATUS_LINK_FAILED",
  sDescription =    "An existing connection (virtual circuit) has been broken at the remote computer. There is probably something wrong with the network software protocol or the network hardware on the remote computer.");
fAddWindowsDefine("STATUS_LINK_TIMEOUT",
  sDescription =    "The network transport on your computer has closed a network connection because it had to wait too long for a response from the remote computer.");
fAddWindowsDefine("STATUS_INVALID_CONNECTION",
  sDescription =    "The connection handle that was given to the transport was invalid.");
fAddWindowsDefine("STATUS_INVALID_ADDRESS",
  sDescription =    "The address handle that was given to the transport was invalid.");
fAddWindowsDefine("STATUS_DLL_INIT_FAILED",
  sDescription =    "Initialization of the dynamic link library %hs failed. The process is terminating abnormally.");
fAddWindowsDefine("STATUS_MISSING_SYSTEMFILE",
  sDescription =    "The required system file %hs is bad or missing.");
fAddWindowsDefine("STATUS_UNHANDLED_EXCEPTION",
  sDescription =    "The exception %s (0x%08lx) occurred in the application at location 0x%08lx.");
fAddWindowsDefine("STATUS_APP_INIT_FAILURE",
  sDescription =    "The application failed to initialize properly (0x%lx). Click OK to terminate the application.");
fAddWindowsDefine("STATUS_PAGEFILE_CREATE_FAILED",
  sDescription =    "The creation of the paging file %hs failed (%lx). The requested size was %ld.");
fAddWindowsDefine("STATUS_NO_PAGEFILE",
  sDescription =    "No paging file was specified in the system configuration.");
fAddWindowsDefine("STATUS_INVALID_LEVEL",
  sDescription =    "An invalid level was passed into the specified system call.");
fAddWindowsDefine("STATUS_WRONG_PASSWORD_CORE",
  sDescription =    "You specified an incorrect password to a LAN Manager 2.x or MS-NET server.");
fAddWindowsDefine("STATUS_ILLEGAL_FLOAT_CONTEXT",
  sDescription =    "A real-mode application issued a floating-point instruction and floating-point hardware is not present.");
fAddWindowsDefine("STATUS_PIPE_BROKEN",
  sDescription =    "The pipe operation has failed because the other end of the pipe has been closed.");
fAddWindowsDefine("STATUS_REGISTRY_CORRUPT",
  sDescription =    "The structure of one of the files that contains registry data is corrupt; the image of the file in memory is corrupt; or the file could not be recovered because the alternate copy or log was absent or corrupt.");
fAddWindowsDefine("STATUS_REGISTRY_IO_FAILED",
  sDescription =    "An I/O operation initiated by the Registry failed and cannot be recovered. The registry could not read in, write out, or flush one of the files that contain the system's image of the registry.");
fAddWindowsDefine("STATUS_NO_EVENT_PAIR",
  sDescription =    "An event pair synchronization operation was performed using the thread-specific client/server event pair object, but no event pair object was associated with the thread.");
fAddWindowsDefine("STATUS_UNRECOGNIZED_VOLUME",
  sDescription =    "The volume does not contain a recognized file system. Be sure that all required file system drivers are loaded and that the volume is not corrupt.");
fAddWindowsDefine("STATUS_SERIAL_NO_DEVICE_INITED",
  sDescription =    "No serial device was successfully initialized. The serial driver will unload.");
fAddWindowsDefine("STATUS_NO_SUCH_ALIAS",
  sDescription =    "The specified local group does not exist.");
fAddWindowsDefine("STATUS_MEMBER_NOT_IN_ALIAS",
  sDescription =    "The specified account name is not a member of the group.");
fAddWindowsDefine("STATUS_MEMBER_IN_ALIAS",
  sDescription =    "The specified account name is already a member of the group.");
fAddWindowsDefine("STATUS_ALIAS_EXISTS",
  sDescription =    "The specified local group already exists.");
fAddWindowsDefine("STATUS_LOGON_NOT_GRANTED",
  sDescription =    "A requested type of logon (for example, interactive, network, and service) is not granted by the local security policy of the target system. Ask the system administrator to grant the necessary form of logon.");
fAddWindowsDefine("STATUS_TOO_MANY_SECRETS",
  sDescription =    "The maximum number of secrets that can be stored in a single system was exceeded. The length and number of secrets is limited to satisfy U.S. State Department export restrictions.");
fAddWindowsDefine("STATUS_SECRET_TOO_LONG",
  sDescription =    "The length of a secret exceeds the maximum allowable length. The length and number of secrets is limited to satisfy U.S. State Department export restrictions.");
fAddWindowsDefine("STATUS_INTERNAL_DB_ERROR",
  sDescription =    "The local security authority (LSA) database contains an internal inconsistency.");
fAddWindowsDefine("STATUS_FULLSCREEN_MODE",
  sDescription =    "The requested operation cannot be performed in full-screen mode.");
fAddWindowsDefine("STATUS_TOO_MANY_CONTEXT_IDS",
  sDescription =    "During a logon attempt, the user's security context accumulated too many security IDs. This is a very unusual situation. Remove the user from some global or local groups to reduce the number of security IDs to incorporate into the security context.");
fAddWindowsDefine("STATUS_LOGON_TYPE_NOT_GRANTED",
  sDescription =    "A user has requested a type of logon (for example, interactive or network) that has not been granted. An administrator has control over who can logon interactively and through the network.");
fAddWindowsDefine("STATUS_NOT_REGISTRY_FILE",
  sDescription =    "The system has attempted to load or restore a file into the registry, and the specified file is not in the format of a registry file.");
fAddWindowsDefine("STATUS_NT_CROSS_ENCRYPTION_REQUIRED",
  sDescription =    "An attempt was made to change a user password in the security account manager without providing the necessary Windows cross-encrypted password.");
fAddWindowsDefine("STATUS_DOMAIN_CTRLR_CONFIG_ERROR",
  sDescription =    "A Windows Server has an incorrect configuration.");
fAddWindowsDefine("STATUS_FT_MISSING_MEMBER",
  sDescription =    "An attempt was made to explicitly access the secondary copy of information via a device control to the fault tolerance driver and the secondary copy is not present in the system.");
fAddWindowsDefine("STATUS_ILL_FORMED_SERVICE_ENTRY",
  sDescription =    "A configuration registry node that represents a driver service entry was ill-formed and did not contain the required value entries.");
fAddWindowsDefine("STATUS_ILLEGAL_CHARACTER",
  sDescription =    "An illegal character was encountered. For a multibyte character set, this includes a lead byte without a succeeding trail byte. For the Unicode character set this includes the characters 0xFFFF and 0xFFFE.");
fAddWindowsDefine("STATUS_UNMAPPABLE_CHARACTER",
  sDescription =    "No mapping for the Unicode character exists in the target multibyte code page.");
fAddWindowsDefine("STATUS_UNDEFINED_CHARACTER",
  sDescription =    "The Unicode character is not defined in the Unicode character set that is installed on the system.");
fAddWindowsDefine("STATUS_FLOPPY_VOLUME",
  sDescription =    "The paging file cannot be created on a floppy disk.");
fAddWindowsDefine("STATUS_FLOPPY_ID_MARK_NOT_FOUND",
  sDescription =    "While accessing a floppy disk, an ID address mark was not found.");
fAddWindowsDefine("STATUS_FLOPPY_WRONG_CYLINDER",
  sDescription =    "While accessing a floppy disk, the track address from the sector ID field was found to be different from the track address that is maintained by the controller.");
fAddWindowsDefine("STATUS_FLOPPY_UNKNOWN_ERROR",
  sDescription =    "The floppy disk controller reported an error that is not recognized by the floppy disk driver.");
fAddWindowsDefine("STATUS_FLOPPY_BAD_REGISTERS",
  sDescription =    "While accessing a floppy-disk, the controller returned inconsistent results via its registers.");
fAddWindowsDefine("STATUS_DISK_RECALIBRATE_FAILED",
  sDescription =    "While accessing the hard disk, a recalibrate operation failed, even after retries.");
fAddWindowsDefine("STATUS_DISK_OPERATION_FAILED",
  sDescription =    "While accessing the hard disk, a disk operation failed even after retries.");
fAddWindowsDefine("STATUS_DISK_RESET_FAILED",
  sDescription =    "While accessing the hard disk, a disk controller reset was needed, but even that failed.");
fAddWindowsDefine("STATUS_SHARED_IRQ_BUSY",
  sDescription =    "An attempt was made to open a device that was sharing an interrupt request (IRQ) with other devices. At least one other device that uses that IRQ was already opened. Two concurrent opens of devices that share an IRQ and only work via interrupts is not supported for the particular bus type that the devices use.");
fAddWindowsDefine("STATUS_FT_ORPHANING",
  sDescription =    "A disk that is part of a fault-tolerant volume can no longer be accessed.");
fAddWindowsDefine("STATUS_BIOS_FAILED_TO_CONNECT_INTERRUPT",
  sDescription =    "The basic input/output system (BIOS) failed to connect a system interrupt to the device or bus for which the device is connected.");
fAddWindowsDefine("STATUS_PARTITION_FAILURE",
  sDescription =    "The tape could not be partitioned.");
fAddWindowsDefine("STATUS_INVALID_BLOCK_LENGTH",
  sDescription =    "When accessing a new tape of a multi-volume partition, the current blocksize is incorrect.");
fAddWindowsDefine("STATUS_DEVICE_NOT_PARTITIONED",
  sDescription =    "The tape partition information could not be found when loading a tape.");
fAddWindowsDefine("STATUS_UNABLE_TO_LOCK_MEDIA",
  sDescription =    "An attempt to lock the eject media mechanism failed.");
fAddWindowsDefine("STATUS_UNABLE_TO_UNLOAD_MEDIA",
  sDescription =    "An attempt to unload media failed.");
fAddWindowsDefine("STATUS_EOM_OVERFLOW",
  sDescription =    "The physical end of tape was detected.");
fAddWindowsDefine("STATUS_NO_MEDIA",
  sDescription =    "There is no media in the drive. Insert media into drive %hs.");
fAddWindowsDefine("STATUS_NO_SUCH_MEMBER",
  sDescription =    "A member could not be added to or removed from the local group because the member does not exist.");
fAddWindowsDefine("STATUS_INVALID_MEMBER",
  sDescription =    "A new member could not be added to a local group because the member has the wrong account type.");
fAddWindowsDefine("STATUS_KEY_DELETED",
  sDescription =    "An illegal operation was attempted on a registry key that has been marked for deletion.");
fAddWindowsDefine("STATUS_NO_LOG_SPACE",
  sDescription =    "The system could not allocate the required space in a registry log.");
fAddWindowsDefine("STATUS_TOO_MANY_SIDS",
  sDescription =    "Too many SIDs have been specified.");
fAddWindowsDefine("STATUS_LM_CROSS_ENCRYPTION_REQUIRED",
  sDescription =    "An attempt was made to change a user password in the security account manager without providing the necessary LM cross-encrypted password.");
fAddWindowsDefine("STATUS_KEY_HAS_CHILDREN",
  sDescription =    "An attempt was made to create a symbolic link in a registry key that already has subkeys or values.");
fAddWindowsDefine("STATUS_CHILD_MUST_BE_VOLATILE",
  sDescription =    "An attempt was made to create a stable subkey under a volatile parent key.");
fAddWindowsDefine("STATUS_DEVICE_CONFIGURATION_ERROR",
  sDescription =    "The I/O device is configured incorrectly or the configuration parameters to the driver are incorrect.");
fAddWindowsDefine("STATUS_DRIVER_INTERNAL_ERROR",
  sDescription =    "An error was detected between two drivers or within an I/O driver.");
fAddWindowsDefine("STATUS_INVALID_DEVICE_STATE",
  sDescription =    "The device is not in a valid state to perform this request.");
fAddWindowsDefine("STATUS_IO_DEVICE_ERROR",
  sDescription =    "The I/O device reported an I/O error.");
fAddWindowsDefine("STATUS_DEVICE_PROTOCOL_ERROR",
  sDescription =    "A protocol error was detected between the driver and the device.");
fAddWindowsDefine("STATUS_BACKUP_CONTROLLER",
  sDescription =    "This operation is only allowed for the primary domain controller of the domain.");
fAddWindowsDefine("STATUS_LOG_FILE_FULL",
  sDescription =    "The log file space is insufficient to support this operation.");
fAddWindowsDefine("STATUS_TOO_LATE",
  sDescription =    "A write operation was attempted to a volume after it was dismounted.");
fAddWindowsDefine("STATUS_NO_TRUST_LSA_SECRET",
  sDescription =    "The workstation does not have a trust secret for the primary domain in the local LSA database.");
fAddWindowsDefine("STATUS_NO_TRUST_SAM_ACCOUNT",
  sDescription =    "The SAM database on the Windows Server does not have a computer account for this workstation trust relationship.");
fAddWindowsDefine("STATUS_TRUSTED_DOMAIN_FAILURE",
  sDescription =    "The logon request failed because the trust relationship between the primary domain and the trusted domain failed.");
fAddWindowsDefine("STATUS_TRUSTED_RELATIONSHIP_FAILURE",
  sDescription =    "The logon request failed because the trust relationship between this workstation and the primary domain failed.");
fAddWindowsDefine("STATUS_EVENTLOG_FILE_CORRUPT",
  sDescription =    "The Eventlog log file is corrupt.");
fAddWindowsDefine("STATUS_EVENTLOG_CANT_START",
  sDescription =    "No Eventlog log file could be opened. The Eventlog service did not start.");
fAddWindowsDefine("STATUS_TRUST_FAILURE",
  sDescription =    "The network logon failed. This might be because the validation authority cannot be reached.");
fAddWindowsDefine("STATUS_MUTANT_LIMIT_EXCEEDED",
  sDescription =    "An attempt was made to acquire a mutant such that its maximum count would have been exceeded.");
fAddWindowsDefine("STATUS_NETLOGON_NOT_STARTED",
  sDescription =    "An attempt was made to logon, but the NetLogon service was not started.");
fAddWindowsDefine("STATUS_ACCOUNT_EXPIRED",
  sDescription =    "The user account has expired.");
fAddWindowsDefine("STATUS_POSSIBLE_DEADLOCK",
  sDescription =    "Possible deadlock condition.");
fAddWindowsDefine("STATUS_NETWORK_CREDENTIAL_CONFLICT",
  sDescription =    "Multiple connections to a server or shared resource by the same user, using more than one user name, are not allowed. Disconnect all previous connections to the server or shared resource and try again.");
fAddWindowsDefine("STATUS_REMOTE_SESSION_LIMIT",
  sDescription =    "An attempt was made to establish a session to a network server, but there are already too many sessions established to that server.");
fAddWindowsDefine("STATUS_EVENTLOG_FILE_CHANGED",
  sDescription =    "The log file has changed between reads.");
fAddWindowsDefine("STATUS_NOLOGON_INTERDOMAIN_TRUST_ACCOUNT",
  sDescription =    "The account used is an interdomain trust account. Use your global user account or local user account to access this server.");
fAddWindowsDefine("STATUS_NOLOGON_WORKSTATION_TRUST_ACCOUNT",
  sDescription =    "The account used is a computer account. Use your global user account or local user account to access this server.");
fAddWindowsDefine("STATUS_NOLOGON_SERVER_TRUST_ACCOUNT",
  sDescription =    "The account used is a server trust account. Use your global user account or local user account to access this server.");
fAddWindowsDefine("STATUS_DOMAIN_TRUST_INCONSISTENT",
  sDescription =    "The name or SID of the specified domain is inconsistent with the trust information for that domain.");
fAddWindowsDefine("STATUS_FS_DRIVER_REQUIRED",
  sDescription =    "A volume has been accessed for which a file system driver is required that has not yet been loaded.");
fAddWindowsDefine("STATUS_IMAGE_ALREADY_LOADED_AS_DLL",
  sDescription =    "Indicates that the specified image is already loaded as a DLL.");
fAddWindowsDefine("STATUS_INCOMPATIBLE_WITH_GLOBAL_SHORT_NAME_REGISTRY_SETTING",
  sDescription =    "Short name settings cannot be changed on this volume due to the global registry setting.");
fAddWindowsDefine("STATUS_SHORT_NAMES_NOT_ENABLED_ON_VOLUME",
  sDescription =    "Short names are not enabled on this volume.");
fAddWindowsDefine("STATUS_SECURITY_STREAM_IS_INCONSISTENT",
  sDescription =    "The security stream for the given volume is in an inconsistent state. Please run CHKDSK on the volume.");
fAddWindowsDefine("STATUS_INVALID_LOCK_RANGE",
  sDescription =    "A requested file lock operation cannot be processed due to an invalid byte range.");
fAddWindowsDefine("STATUS_INVALID_ACE_CONDITION",
  sDescription =    "The specified access control entry (ACE) contains an invalid condition.");
fAddWindowsDefine("STATUS_IMAGE_SUBSYSTEM_NOT_PRESENT",
  sDescription =    "The subsystem needed to support the image type is not present.");
fAddWindowsDefine("STATUS_NOTIFICATION_GUID_ALREADY_DEFINED",
  sDescription =    "The specified file already has a notification GUID associated with it.");
fAddWindowsDefine("STATUS_FAILFAST_OOM_EXCEPTION",
  sDescription =    "The amount of memory requested by the application could not be allocated.",
  sTypeId =         "OOM");
fAddWindowsDefine("STATUS_NETWORK_OPEN_RESTRICTION",
  sDescription =    "A remote open failed because the network open restrictions were not satisfied.");
fAddWindowsDefine("STATUS_NO_USER_SESSION_KEY",
  sDescription =    "There is no user session key for the specified logon session.");
fAddWindowsDefine("STATUS_USER_SESSION_DELETED",
  sDescription =    "The remote user session has been deleted.");
fAddWindowsDefine("STATUS_RESOURCE_LANG_NOT_FOUND",
  sDescription =    "Indicates the specified resource language ID cannot be found in the image file.");
fAddWindowsDefine("STATUS_INSUFF_SERVER_RESOURCES",
  sDescription =    "Insufficient server resources exist to complete the request.");
fAddWindowsDefine("STATUS_INVALID_BUFFER_SIZE",
  sDescription =    "The size of the buffer is invalid for the specified operation.");
fAddWindowsDefine("STATUS_INVALID_ADDRESS_COMPONENT",
  sDescription =    "The transport rejected the specified network address as invalid.");
fAddWindowsDefine("STATUS_INVALID_ADDRESS_WILDCARD",
  sDescription =    "The transport rejected the specified network address due to invalid use of a wildcard.");
fAddWindowsDefine("STATUS_TOO_MANY_ADDRESSES",
  sDescription =    "The transport address could not be opened because all the available addresses are in use.");
fAddWindowsDefine("STATUS_ADDRESS_ALREADY_EXISTS",
  sDescription =    "The transport address could not be opened because it already exists.");
fAddWindowsDefine("STATUS_ADDRESS_CLOSED",
  sDescription =    "The transport address is now closed.");
fAddWindowsDefine("STATUS_CONNECTION_DISCONNECTED",
  sDescription =    "The transport connection is now disconnected.");
fAddWindowsDefine("STATUS_CONNECTION_RESET",
  sDescription =    "The transport connection has been reset.");
fAddWindowsDefine("STATUS_TOO_MANY_NODES",
  sDescription =    "The transport cannot dynamically acquire any more nodes.");
fAddWindowsDefine("STATUS_TRANSACTION_ABORTED",
  sDescription =    "The transport aborted a pending transaction.");
fAddWindowsDefine("STATUS_TRANSACTION_TIMED_OUT",
  sDescription =    "The transport timed out a request that is waiting for a response.");
fAddWindowsDefine("STATUS_TRANSACTION_NO_RELEASE",
  sDescription =    "The transport did not receive a release for a pending response.");
fAddWindowsDefine("STATUS_TRANSACTION_NO_MATCH",
  sDescription =    "The transport did not find a transaction that matches the specific token.");
fAddWindowsDefine("STATUS_TRANSACTION_RESPONDED",
  sDescription =    "The transport had previously responded to a transaction request.");
fAddWindowsDefine("STATUS_TRANSACTION_INVALID_ID",
  sDescription =    "The transport does not recognize the specified transaction request ID.");
fAddWindowsDefine("STATUS_TRANSACTION_INVALID_TYPE",
  sDescription =    "The transport does not recognize the specified transaction request type.");
fAddWindowsDefine("STATUS_NOT_SERVER_SESSION",
  sDescription =    "The transport can only process the specified request on the server side of a session.");
fAddWindowsDefine("STATUS_NOT_CLIENT_SESSION",
  sDescription =    "The transport can only process the specified request on the client side of a session.");
fAddWindowsDefine("STATUS_CANNOT_LOAD_REGISTRY_FILE",
  sDescription =    "The registry cannot load the hive (file): %hs or its log or alternate. It is corrupt, absent, or not writable.");
fAddWindowsDefine("STATUS_DEBUG_ATTACH_FAILED",
  sDescription =    "An unexpected failure occurred while processing a DebugActiveProcess API request. Choosing OK will terminate the process, and choosing Cancel will ignore the error.");
fAddWindowsDefine("STATUS_SYSTEM_PROCESS_TERMINATED",
  sDescription =    "The %hs system process terminated unexpectedly with a status of 0x%08x (0x%08x 0x%08x). The system has been shut down.");
fAddWindowsDefine("STATUS_DATA_NOT_ACCEPTED",
  sDescription =    "The TDI client could not handle the data received during an indication.");
fAddWindowsDefine("STATUS_NO_BROWSER_SERVERS_FOUND",
  sDescription =    "The list of servers for this workgroup is not currently available.");
fAddWindowsDefine("STATUS_VDM_HARD_ERROR",
  sDescription =    "NTVDM encountered a hard error.");
fAddWindowsDefine("STATUS_DRIVER_CANCEL_TIMEOUT",
  sDescription =    "The driver %hs failed to complete a canceled I/O request in the allotted time.");
fAddWindowsDefine("STATUS_REPLY_MESSAGE_MISMATCH",
  sDescription =    "An attempt was made to reply to an LPC message, but the thread specified by the client ID in the message was not waiting on that message.");
fAddWindowsDefine("STATUS_MAPPED_ALIGNMENT",
  sDescription =    "An attempt was made to map a view of a file, but either the specified base address or the offset into the file were not aligned on the proper allocation granularity.");
fAddWindowsDefine("STATUS_IMAGE_CHECKSUM_MISMATCH",
  sDescription =    "The image %hs is possibly corrupt. The header checksum does not match the computed checksum.");
fAddWindowsDefine("STATUS_LOST_WRITEBEHIND_DATA",
  sDescription =    "Windows was unable to save all the data for the file %hs. The data has been lost. This error might be caused by a failure of your computer hardware or network connection. Try to save this file elsewhere.");
fAddWindowsDefine("STATUS_CLIENT_SERVER_PARAMETERS_INVALID",
  sDescription =    "The parameters passed to the server in the client/server shared memory window were invalid. Too much data might have been put in the shared memory window.");
fAddWindowsDefine("STATUS_PASSWORD_MUST_CHANGE",
  sDescription =    "The user password must be changed before logging on the first time.");
fAddWindowsDefine("STATUS_NOT_FOUND",
  sDescription =    "The object was not found.");
fAddWindowsDefine("STATUS_NOT_TINY_STREAM",
  sDescription =    "The stream is not a tiny stream.");
fAddWindowsDefine("STATUS_RECOVERY_FAILURE",
  sDescription =    "A transaction recovery failed.");
fAddWindowsDefine("STATUS_STACK_OVERFLOW_READ",
  sDescription =    "The request must be handled by the stack overflow code.");
fAddWindowsDefine("STATUS_FAIL_CHECK",
  sDescription =    "A consistency check failed.");
fAddWindowsDefine("STATUS_DUPLICATE_OBJECTID",
  sDescription =    "The attempt to insert the ID in the index failed because the ID is already in the index.");
fAddWindowsDefine("STATUS_OBJECTID_EXISTS",
  sDescription =    "The attempt to set the object ID failed because the object already has an ID.");
fAddWindowsDefine("STATUS_CONVERT_TO_LARGE",
  sDescription =    "Internal OFS status codes indicating how an allocation operation is handled. Either it is retried after the containing oNode is moved or the extent stream is converted to a large stream.");
fAddWindowsDefine("STATUS_RETRY",
  sDescription =    "The request needs to be retried.");
fAddWindowsDefine("STATUS_FOUND_OUT_OF_SCOPE",
  sDescription =    "The attempt to find the object found an object on the volume that matches by ID; however, it is out of the scope of the handle that is used for the operation.");
fAddWindowsDefine("STATUS_ALLOCATE_BUCKET",
  sDescription =    "The bucket array must be grown. Retry the transaction after doing so.");
fAddWindowsDefine("STATUS_PROPSET_NOT_FOUND",
  sDescription =    "The specified property set does not exist on the object.");
fAddWindowsDefine("STATUS_MARSHALL_OVERFLOW",
  sDescription =    "The user/kernel marshaling buffer has overflowed.");
fAddWindowsDefine("STATUS_INVALID_VARIANT",
  sDescription =    "The supplied variant structure contains invalid data.");
fAddWindowsDefine("STATUS_DOMAIN_CONTROLLER_NOT_FOUND",
  sDescription =    "A domain controller for this domain was not found.");
fAddWindowsDefine("STATUS_ACCOUNT_LOCKED_OUT",
  sDescription =    "The user account has been automatically locked because too many invalid logon attempts or password change attempts have been requested.");
fAddWindowsDefine("STATUS_HANDLE_NOT_CLOSABLE",
  sDescription =    "NtClose was called on a handle that was protected from close via NtSetInformationObject.");
fAddWindowsDefine("STATUS_CONNECTION_REFUSED",
  sDescription =    "The transport-connection attempt was refused by the remote system.");
fAddWindowsDefine("STATUS_GRACEFUL_DISCONNECT",
  sDescription =    "The transport connection was gracefully closed.");
fAddWindowsDefine("STATUS_ADDRESS_ALREADY_ASSOCIATED",
  sDescription =    "The transport endpoint already has an address associated with it.");
fAddWindowsDefine("STATUS_ADDRESS_NOT_ASSOCIATED",
  sDescription =    "An address has not yet been associated with the transport endpoint.");
fAddWindowsDefine("STATUS_CONNECTION_INVALID",
  sDescription =    "An operation was attempted on a nonexistent transport connection.");
fAddWindowsDefine("STATUS_CONNECTION_ACTIVE",
  sDescription =    "An invalid operation was attempted on an active transport connection.");
fAddWindowsDefine("STATUS_NETWORK_UNREACHABLE",
  sDescription =    "The remote network is not reachable by the transport.");
fAddWindowsDefine("STATUS_HOST_UNREACHABLE",
  sDescription =    "The remote system is not reachable by the transport.");
fAddWindowsDefine("STATUS_PROTOCOL_UNREACHABLE",
  sDescription =    "The remote system does not support the transport protocol.");
fAddWindowsDefine("STATUS_PORT_UNREACHABLE",
  sDescription =    "No service is operating at the destination port of the transport on the remote system.");
fAddWindowsDefine("STATUS_REQUEST_ABORTED",
  sDescription =    "The request was aborted.");
fAddWindowsDefine("STATUS_CONNECTION_ABORTED",
  sDescription =    "The transport connection was aborted by the local system.");
fAddWindowsDefine("STATUS_BAD_COMPRESSION_BUFFER",
  sDescription =    "The specified buffer contains ill-formed data.");
fAddWindowsDefine("STATUS_USER_MAPPED_FILE",
  sDescription =    "The requested operation cannot be performed on a file with a user mapped section open.");
fAddWindowsDefine("STATUS_AUDIT_FAILED",
  sDescription =    "An attempt to generate a security audit failed.");
fAddWindowsDefine("STATUS_TIMER_RESOLUTION_NOT_SET",
  sDescription =    "The timer resolution was not previously set by the current process.");
fAddWindowsDefine("STATUS_CONNECTION_COUNT_LIMIT",
  sDescription =    "A connection to the server could not be made because the limit on the number of concurrent connections for this account has been reached.");
fAddWindowsDefine("STATUS_LOGIN_TIME_RESTRICTION",
  sDescription =    "Attempting to log on during an unauthorized time of day for this account.");
fAddWindowsDefine("STATUS_LOGIN_WKSTA_RESTRICTION",
  sDescription =    "The account is not authorized to log on from this station.");
fAddWindowsDefine("STATUS_IMAGE_MP_UP_MISMATCH",
  sDescription =    "The image %hs has been modified for use on a uniprocessor system, but you are running it on a multiprocessor machine. Reinstall the image file.");
fAddWindowsDefine("STATUS_INSUFFICIENT_LOGON_INFO",
  sDescription =    "There is insufficient account information to log you on.");
fAddWindowsDefine("STATUS_BAD_DLL_ENTRYPOINT",
  sDescription =    "The dynamic link library %hs is not written correctly. The stack pointer has been left in an inconsistent state. The entry point should be declared as WINAPI or STDCALL. Select YES to fail the DLL load. Select NO to continue execution. Selecting NO might cause the application to operate incorrectly.");
fAddWindowsDefine("STATUS_BAD_SERVICE_ENTRYPOINT",
  sDescription =    "The %hs service is not written correctly. The stack pointer has been left in an inconsistent state. The callback entry point should be declared as WINAPI or STDCALL. Selecting OK will cause the service to continue operation. However, the service process might operate incorrectly.");
fAddWindowsDefine("STATUS_LPC_REPLY_LOST",
  sDescription =    "The server received the messages but did not send a reply.");
fAddWindowsDefine("STATUS_IP_ADDRESS_CONFLICT1",
  sDescription =    "There is an IP address conflict with another system on the network.");
fAddWindowsDefine("STATUS_IP_ADDRESS_CONFLICT2",
  sDescription =    "There is an IP address conflict with another system on the network.");
fAddWindowsDefine("STATUS_REGISTRY_QUOTA_LIMIT",
  sDescription =    "The system has reached the maximum size that is allowed for the system part of the registry. Additional storage requests will be ignored.");
fAddWindowsDefine("STATUS_PATH_NOT_COVERED",
  sDescription =    "The contacted server does not support the indicated part of the DFS namespace.");
fAddWindowsDefine("STATUS_NO_CALLBACK_ACTIVE",
  sDescription =    "A callback return system service cannot be executed when no callback is active.");
fAddWindowsDefine("STATUS_LICENSE_QUOTA_EXCEEDED",
  sDescription =    "The service being accessed is licensed for a particular number of connections. No more connections can be made to the service at this time because the service has already accepted the maximum number of connections.");
fAddWindowsDefine("STATUS_PWD_TOO_SHORT",
  sDescription =    "The password provided is too short to meet the policy of your user account. Choose a longer password.");
fAddWindowsDefine("STATUS_PWD_TOO_RECENT",
  sDescription =    "The policy of your user account does not allow you to change passwords too frequently. This is done to prevent users from changing back to a familiar, but potentially discovered, password. If you feel your password has been compromised, contact your administrator immediately to have a new one assigned.");
fAddWindowsDefine("STATUS_PWD_HISTORY_CONFLICT",
  sDescription =    "You have attempted to change your password to one that you have used in the past. The policy of your user account does not allow this. Select a password that you have not previously used.");
fAddWindowsDefine("STATUS_PLUGPLAY_NO_DEVICE",
  sDescription =    "You have attempted to load a legacy device driver while its device instance had been disabled.");
fAddWindowsDefine("STATUS_UNSUPPORTED_COMPRESSION",
  sDescription =    "The specified compression format is unsupported.");
fAddWindowsDefine("STATUS_INVALID_HW_PROFILE",
  sDescription =    "The specified hardware profile configuration is invalid.");
fAddWindowsDefine("STATUS_INVALID_PLUGPLAY_DEVICE_PATH",
  sDescription =    "The specified Plug and Play registry device path is invalid.");
fAddWindowsDefine("STATUS_DRIVER_ORDINAL_NOT_FOUND",
  sDescription =    "The %hs device driver could not locate the ordinal %ld in driver %hs.");
fAddWindowsDefine("STATUS_DRIVER_ENTRYPOINT_NOT_FOUND",
  sDescription =    "The %hs device driver could not locate the entry point %hs in driver %hs.");
fAddWindowsDefine("STATUS_RESOURCE_NOT_OWNED",
  sDescription =    "The application attempted to release a resource it did not own. Click OK to terminate the application.");
fAddWindowsDefine("STATUS_TOO_MANY_LINKS",
  sDescription =    "An attempt was made to create more links on a file than the file system supports.");
fAddWindowsDefine("STATUS_QUOTA_LIST_INCONSISTENT",
  sDescription =    "The specified quota list is internally inconsistent with its descriptor.");
fAddWindowsDefine("STATUS_FILE_IS_OFFLINE",
  sDescription =    "The specified file has been relocated to offline storage.");
fAddWindowsDefine("STATUS_EVALUATION_EXPIRATION",
  sDescription =    "The evaluation period for this installation of Windows has expired. This system will shutdown in 1 hour. To restore access to this installation of Windows, upgrade this installation by using a licensed distribution of this product.");
fAddWindowsDefine("STATUS_ILLEGAL_DLL_RELOCATION",
  sDescription =    "The system DLL %hs was relocated in memory. The application will not run properly. The relocation occurred because the DLL %hs occupied an address range that is reserved for Windows system DLLs. The vendor supplying the DLL should be contacted for a new DLL.");
fAddWindowsDefine("STATUS_LICENSE_VIOLATION",
  sDescription =    "The system has detected tampering with your registered product type. This is a violation of your software license. Tampering with the product type is not permitted.");
fAddWindowsDefine("STATUS_DLL_INIT_FAILED_LOGOFF",
  sDescription =    "The application failed to initialize because the window station is shutting down.");
fAddWindowsDefine("STATUS_DRIVER_UNABLE_TO_LOAD",
  sDescription =    "%hs device driver could not be loaded. Error Status was 0x%x.");
fAddWindowsDefine("STATUS_DFS_UNAVAILABLE",
  sDescription =    "DFS is unavailable on the contacted server.");
fAddWindowsDefine("STATUS_VOLUME_DISMOUNTED",
  sDescription =    "An operation was attempted to a volume after it was dismounted.");
fAddWindowsDefine("STATUS_WX86_INTERNAL_ERROR",
  sDescription =    "An internal error occurred in the Win32 x86 emulation subsystem.");
fAddWindowsDefine("STATUS_WX86_FLOAT_STACK_CHECK",
  sDescription =    "Win32 x86 emulation subsystem floating-point stack check.");
fAddWindowsDefine("STATUS_VALIDATE_CONTINUE",
  sDescription =    "The validation process needs to continue on to the next step.");
fAddWindowsDefine("STATUS_NO_MATCH",
  sDescription =    "There was no match for the specified key in the index.");
fAddWindowsDefine("STATUS_NO_MORE_MATCHES",
  sDescription =    "There are no more matches for the current index enumeration.");
fAddWindowsDefine("STATUS_NOT_A_REPARSE_POINT",
  sDescription =    "The NTFS file or directory is not a reparse point.");
fAddWindowsDefine("STATUS_IO_REPARSE_TAG_INVALID",
  sDescription =    "The Windows I/O reparse tag passed for the NTFS reparse point is invalid.");
fAddWindowsDefine("STATUS_IO_REPARSE_TAG_MISMATCH",
  sDescription =    "The Windows I/O reparse tag does not match the one that is in the NTFS reparse point.");
fAddWindowsDefine("STATUS_IO_REPARSE_DATA_INVALID",
  sDescription =    "The user data passed for the NTFS reparse point is invalid.");
fAddWindowsDefine("STATUS_IO_REPARSE_TAG_NOT_HANDLED",
  sDescription =    "The layered file system driver for this I/O tag did not handle it when needed.");
fAddWindowsDefine("STATUS_STOWED_EXCEPTION",
  sDescription =    "A stowed exception was encountered",
  sTypeId =         "WRTLanguage");
fAddWindowsDefine("STATUS_REPARSE_POINT_NOT_RESOLVED",
  sDescription =    "The NTFS symbolic link could not be resolved even though the initial file name is valid.");
fAddWindowsDefine("STATUS_DIRECTORY_IS_A_REPARSE_POINT",
  sDescription =    "The NTFS directory is a reparse point.");
fAddWindowsDefine("STATUS_RANGE_LIST_CONFLICT",
  sDescription =    "The range could not be added to the range list because of a conflict.");
fAddWindowsDefine("STATUS_SOURCE_ELEMENT_EMPTY",
  sDescription =    "The specified medium changer source element contains no media.");
fAddWindowsDefine("STATUS_DESTINATION_ELEMENT_FULL",
  sDescription =    "The specified medium changer destination element already contains media.");
fAddWindowsDefine("STATUS_ILLEGAL_ELEMENT_ADDRESS",
  sDescription =    "The specified medium changer element does not exist.");
fAddWindowsDefine("STATUS_MAGAZINE_NOT_PRESENT",
  sDescription =    "The specified element is contained in a magazine that is no longer present.");
fAddWindowsDefine("STATUS_REINITIALIZATION_NEEDED",
  sDescription =    "The device requires re-initialization due to hardware errors.");
fAddWindowsDefine("STATUS_ENCRYPTION_FAILED",
  sDescription =    "The file encryption attempt failed.");
fAddWindowsDefine("STATUS_DECRYPTION_FAILED",
  sDescription =    "The file decryption attempt failed.");
fAddWindowsDefine("STATUS_RANGE_NOT_FOUND",
  sDescription =    "The specified range could not be found in the range list.");
fAddWindowsDefine("STATUS_NO_RECOVERY_POLICY",
  sDescription =    "There is no encryption recovery policy configured for this system.");
fAddWindowsDefine("STATUS_NO_EFS",
  sDescription =    "The required encryption driver is not loaded for this system.");
fAddWindowsDefine("STATUS_WRONG_EFS",
  sDescription =    "The file was encrypted with a different encryption driver than is currently loaded.");
fAddWindowsDefine("STATUS_NO_USER_KEYS",
  sDescription =    "There are no EFS keys defined for the user.");
fAddWindowsDefine("STATUS_FILE_NOT_ENCRYPTED",
  sDescription =    "The specified file is not encrypted.");
fAddWindowsDefine("STATUS_NOT_EXPORT_FORMAT",
  sDescription =    "The specified file is not in the defined EFS export format.");
fAddWindowsDefine("STATUS_FILE_ENCRYPTED",
  sDescription =    "The specified file is encrypted and the user does not have the ability to decrypt it.");
fAddWindowsDefine("STATUS_WMI_GUID_NOT_FOUND",
  sDescription =    "The GUID passed was not recognized as valid by a WMI data provider.");
fAddWindowsDefine("STATUS_WMI_INSTANCE_NOT_FOUND",
  sDescription =    "The instance name passed was not recognized as valid by a WMI data provider.");
fAddWindowsDefine("STATUS_WMI_ITEMID_NOT_FOUND",
  sDescription =    "The data item ID passed was not recognized as valid by a WMI data provider.");
fAddWindowsDefine("STATUS_WMI_TRY_AGAIN",
  sDescription =    "The WMI request could not be completed and should be retried.");
fAddWindowsDefine("STATUS_SHARED_POLICY",
  sDescription =    "The policy object is shared and can only be modified at the root.");
fAddWindowsDefine("STATUS_POLICY_OBJECT_NOT_FOUND",
  sDescription =    "The policy object does not exist when it should.");
fAddWindowsDefine("STATUS_POLICY_ONLY_IN_DS",
  sDescription =    "The requested policy information only lives in the Ds.");
fAddWindowsDefine("STATUS_VOLUME_NOT_UPGRADED",
  sDescription =    "The volume must be upgraded to enable this feature.");
fAddWindowsDefine("STATUS_REMOTE_STORAGE_NOT_ACTIVE",
  sDescription =    "The remote storage service is not operational at this time.");
fAddWindowsDefine("STATUS_REMOTE_STORAGE_MEDIA_ERROR",
  sDescription =    "The remote storage service encountered a media error.");
fAddWindowsDefine("STATUS_NO_TRACKING_SERVICE",
  sDescription =    "The tracking (workstation) service is not running.");
fAddWindowsDefine("STATUS_SERVER_SID_MISMATCH",
  sDescription =    "The server process is running under a SID that is different from the SID that is required by client.");
fAddWindowsDefine("STATUS_DS_NO_ATTRIBUTE_OR_VALUE",
  sDescription =    "The specified directory service attribute or value does not exist.");
fAddWindowsDefine("STATUS_DS_INVALID_ATTRIBUTE_SYNTAX",
  sDescription =    "The attribute syntax specified to the directory service is invalid.");
fAddWindowsDefine("STATUS_DS_ATTRIBUTE_TYPE_UNDEFINED",
  sDescription =    "The attribute type specified to the directory service is not defined.");
fAddWindowsDefine("STATUS_DS_ATTRIBUTE_OR_VALUE_EXISTS",
  sDescription =    "The specified directory service attribute or value already exists.");
fAddWindowsDefine("STATUS_DS_BUSY",
  sDescription =    "The directory service is busy.");
fAddWindowsDefine("STATUS_DS_UNAVAILABLE",
  sDescription =    "The directory service is unavailable.");
fAddWindowsDefine("STATUS_DS_NO_RIDS_ALLOCATED",
  sDescription =    "The directory service was unable to allocate a relative identifier.");
fAddWindowsDefine("STATUS_DS_NO_MORE_RIDS",
  sDescription =    "The directory service has exhausted the pool of relative identifiers.");
fAddWindowsDefine("STATUS_DS_INCORRECT_ROLE_OWNER",
  sDescription =    "The requested operation could not be performed because the directory service is not the master for that type of operation.");
fAddWindowsDefine("STATUS_DS_RIDMGR_INIT_ERROR",
  sDescription =    "The directory service was unable to initialize the subsystem that allocates relative identifiers.");
fAddWindowsDefine("STATUS_DS_OBJ_CLASS_VIOLATION",
  sDescription =    "The requested operation did not satisfy one or more constraints that are associated with the class of the object.");
fAddWindowsDefine("STATUS_DS_CANT_ON_NON_LEAF",
  sDescription =    "The directory service can perform the requested operation only on a leaf object.");
fAddWindowsDefine("STATUS_DS_CANT_ON_RDN",
  sDescription =    "The directory service cannot perform the requested operation on the Relatively Defined Name (RDN) attribute of an object.");
fAddWindowsDefine("STATUS_DS_CANT_MOD_OBJ_CLASS",
  sDescription =    "The directory service detected an attempt to modify the object class of an object.");
fAddWindowsDefine("STATUS_DS_CROSS_DOM_MOVE_FAILED",
  sDescription =    "An error occurred while performing a cross domain move operation.");
fAddWindowsDefine("STATUS_DS_GC_NOT_AVAILABLE",
  sDescription =    "Unable to contact the global catalog server.");
fAddWindowsDefine("STATUS_DIRECTORY_SERVICE_REQUIRED",
  sDescription =    "The requested operation requires a directory service, and none was available.");
fAddWindowsDefine("STATUS_REPARSE_ATTRIBUTE_CONFLICT",
  sDescription =    "The reparse attribute cannot be set because it is incompatible with an existing attribute.");
fAddWindowsDefine("STATUS_CANT_ENABLE_DENY_ONLY",
  sDescription =    "A group marked \"use for deny only\" cannot be enabled.");
fAddWindowsDefine("STATUS_FLOAT_MULTIPLE_FAULTS",
  sDescription =    "Multiple floating-point faults.");
fAddWindowsDefine("STATUS_FLOAT_MULTIPLE_TRAPS",
  sDescription =    "Multiple floating-point traps.");
fAddWindowsDefine("STATUS_DEVICE_REMOVED",
  sDescription =    "The device has been removed.");
fAddWindowsDefine("STATUS_JOURNAL_DELETE_IN_PROGRESS",
  sDescription =    "The volume change journal is being deleted.");
fAddWindowsDefine("STATUS_JOURNAL_NOT_ACTIVE",
  sDescription =    "The volume change journal is not active.");
fAddWindowsDefine("STATUS_NOINTERFACE",
  sDescription =    "The requested interface is not supported.");
fAddWindowsDefine("STATUS_DS_ADMIN_LIMIT_EXCEEDED",
  sDescription =    "A directory service resource limit has been exceeded.");
fAddWindowsDefine("STATUS_DRIVER_FAILED_SLEEP",
  sDescription =    "The driver %hs does not support standby mode. Updating this driver allows the system to go to standby mode.");
fAddWindowsDefine("STATUS_MUTUAL_AUTHENTICATION_FAILED",
  sDescription =    "Mutual Authentication failed. The server password is out of date at the domain controller.");
fAddWindowsDefine("STATUS_CORRUPT_SYSTEM_FILE",
  sDescription =    "The system file %1 has become corrupt and has been replaced.");
fAddWindowsDefine("STATUS_DATATYPE_MISALIGNMENT_ERROR",
  sDescription =    "Alignment Error A data type misalignment error was detected in a load or store instruction.");
fAddWindowsDefine("STATUS_WMI_READ_ONLY",
  sDescription =    "The WMI data item or data block is read-only.");
fAddWindowsDefine("STATUS_WMI_SET_FAILURE",
  sDescription =    "The WMI data item or data block could not be changed.");
fAddWindowsDefine("STATUS_COMMITMENT_MINIMUM",
  sDescription =    "Your system is low on virtual memory. Windows is increasing the size of your virtual memory paging file. During this process, memory requests for some applications might be denied. For more information, see Help.");
fAddWindowsDefine("STATUS_REG_NAT_CONSUMPTION",
  sDescription =    "Register NaT consumption faults. A NaT value is consumed on a non-speculative instruction.");
fAddWindowsDefine("STATUS_TRANSPORT_FULL",
  sDescription =    "The transport element of the medium changer contains media, which is causing the operation to fail.");
fAddWindowsDefine("STATUS_DS_SAM_INIT_FAILURE",
  sDescription =    "Security Accounts Manager initialization failed because of the following error: %hs Error Status: 0x%x. Click OK to shut down this system and restart in Directory Services Restore Mode. Check the event log for more detailed information.");
fAddWindowsDefine("STATUS_ONLY_IF_CONNECTED",
  sDescription =    "This operation is supported only when you are connected to the server.");
fAddWindowsDefine("STATUS_DS_SENSITIVE_GROUP_VIOLATION",
  sDescription =    "Only an administrator can modify the membership list of an administrative group.");
fAddWindowsDefine("STATUS_PNP_RESTART_ENUMERATION",
  sDescription =    "A device was removed so enumeration must be restarted.");
fAddWindowsDefine("STATUS_JOURNAL_ENTRY_DELETED",
  sDescription =    "The journal entry has been deleted from the journal.");
fAddWindowsDefine("STATUS_DS_CANT_MOD_PRIMARYGROUPID",
  sDescription =    "Cannot change the primary group ID of a domain controller account.");
fAddWindowsDefine("STATUS_SYSTEM_IMAGE_BAD_SIGNATURE",
  sDescription =    "The system image %s is not properly signed. The file has been replaced with the signed file. The system has been shut down.");
fAddWindowsDefine("STATUS_PNP_REBOOT_REQUIRED",
  sDescription =    "The device will not start without a reboot.");
fAddWindowsDefine("STATUS_POWER_STATE_INVALID",
  sDescription =    "The power state of the current device cannot support this request.");
fAddWindowsDefine("STATUS_DS_INVALID_GROUP_TYPE",
  sDescription =    "The specified group type is invalid.");
fAddWindowsDefine("STATUS_DS_NO_NEST_GLOBALGROUP_IN_MIXEDDOMAIN",
  sDescription =    "In a mixed domain, no nesting of a global group if the group is security enabled.");
fAddWindowsDefine("STATUS_DS_NO_NEST_LOCALGROUP_IN_MIXEDDOMAIN",
  sDescription =    "In a mixed domain, cannot nest local groups with other local groups, if the group is security enabled.");
fAddWindowsDefine("STATUS_DS_GLOBAL_CANT_HAVE_LOCAL_MEMBER",
  sDescription =    "A global group cannot have a local group as a member.");
fAddWindowsDefine("STATUS_DS_GLOBAL_CANT_HAVE_UNIVERSAL_MEMBER",
  sDescription =    "A global group cannot have a universal group as a member.");
fAddWindowsDefine("STATUS_DS_UNIVERSAL_CANT_HAVE_LOCAL_MEMBER",
  sDescription =    "A universal group cannot have a local group as a member.");
fAddWindowsDefine("STATUS_DS_GLOBAL_CANT_HAVE_CROSSDOMAIN_MEMBER",
  sDescription =    "A global group cannot have a cross-domain member.");
fAddWindowsDefine("STATUS_DS_LOCAL_CANT_HAVE_CROSSDOMAIN_LOCAL_MEMBER",
  sDescription =    "A local group cannot have another cross-domain local group as a member.");
fAddWindowsDefine("STATUS_DS_HAVE_PRIMARY_MEMBERS",
  sDescription =    "Cannot change to a security-disabled group because primary members are in this group.");
fAddWindowsDefine("STATUS_WMI_NOT_SUPPORTED",
  sDescription =    "The WMI operation is not supported by the data block or method.");
fAddWindowsDefine("STATUS_INSUFFICIENT_POWER",
  sDescription =    "There is not enough power to complete the requested operation.");
fAddWindowsDefine("STATUS_SAM_NEED_BOOTKEY_PASSWORD",
  sDescription =    "The Security Accounts Manager needs to get the boot password.");
fAddWindowsDefine("STATUS_SAM_NEED_BOOTKEY_FLOPPY",
  sDescription =    "The Security Accounts Manager needs to get the boot key from the floppy disk.");
fAddWindowsDefine("STATUS_DS_CANT_START",
  sDescription =    "The directory service cannot start.");
fAddWindowsDefine("STATUS_DS_INIT_FAILURE",
  sDescription =    "The directory service could not start because of the following error: %hs Error Status: 0x%x. Click OK to shut down this system and restart in Directory Services Restore Mode. Check the event log for more detailed information.");
fAddWindowsDefine("STATUS_SAM_INIT_FAILURE",
  sDescription =    "The Security Accounts Manager initialization failed because of the following error: %hs Error Status: 0x%x. Click OK to shut down this system and restart in Safe Mode. Check the event log for more detailed information.");
fAddWindowsDefine("STATUS_DS_GC_REQUIRED",
  sDescription =    "The requested operation can be performed only on a global catalog server.");
fAddWindowsDefine("STATUS_DS_LOCAL_MEMBER_OF_LOCAL_ONLY",
  sDescription =    "A local group can only be a member of other local groups in the same domain.");
fAddWindowsDefine("STATUS_DS_NO_FPO_IN_UNIVERSAL_GROUPS",
  sDescription =    "Foreign security principals cannot be members of universal groups.");
fAddWindowsDefine("STATUS_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED",
  sDescription =    "Your computer could not be joined to the domain. You have exceeded the maximum number of computer accounts you are allowed to create in this domain. Contact your system administrator to have this limit reset or increased.");
fAddWindowsDefine("STATUS_CURRENT_DOMAIN_NOT_ALLOWED",
  sDescription =    "This operation cannot be performed on the current domain.");
fAddWindowsDefine("STATUS_CANNOT_MAKE",
  sDescription =    "The directory or file cannot be created.");
fAddWindowsDefine("STATUS_SYSTEM_SHUTDOWN",
  sDescription =    "The system is in the process of shutting down.");
fAddWindowsDefine("STATUS_DS_INIT_FAILURE_CONSOLE",
  sDescription =    "Directory Services could not start because of the following error: %hs Error Status: 0x%x. Click OK to shut down the system. You can use the recovery console to diagnose the system further.");
fAddWindowsDefine("STATUS_DS_SAM_INIT_FAILURE_CONSOLE",
  sDescription =    "Security Accounts Manager initialization failed because of the following error: %hs Error Status: 0x%x. Click OK to shut down the system. You can use the recovery console to diagnose the system further.");
fAddWindowsDefine("STATUS_UNFINISHED_CONTEXT_DELETED",
  sDescription =    "A security context was deleted before the context was completed. This is considered a logon failure.");
fAddWindowsDefine("STATUS_NO_TGT_REPLY",
  sDescription =    "The client is trying to negotiate a context and the server requires user-to-user but did not send a TGT reply.");
fAddWindowsDefine("STATUS_OBJECTID_NOT_FOUND",
  sDescription =    "An object ID was not found in the file.");
fAddWindowsDefine("STATUS_NO_IP_ADDRESSES",
  sDescription =    "Unable to accomplish the requested task because the local machine does not have any IP addresses.");
fAddWindowsDefine("STATUS_WRONG_CREDENTIAL_HANDLE",
  sDescription =    "The supplied credential handle does not match the credential that is associated with the security context.");
fAddWindowsDefine("STATUS_CRYPTO_SYSTEM_INVALID",
  sDescription =    "The crypto system or checksum function is invalid because a required function is unavailable.");
fAddWindowsDefine("STATUS_MAX_REFERRALS_EXCEEDED",
  sDescription =    "The number of maximum ticket referrals has been exceeded.");
fAddWindowsDefine("STATUS_MUST_BE_KDC",
  sDescription =    "The local machine must be a Kerberos KDC (domain controller) and it is not.");
fAddWindowsDefine("STATUS_STRONG_CRYPTO_NOT_SUPPORTED",
  sDescription =    "The other end of the security negotiation requires strong crypto but it is not supported on the local machine.");
fAddWindowsDefine("STATUS_TOO_MANY_PRINCIPALS",
  sDescription =    "The KDC reply contained more than one principal name.");
fAddWindowsDefine("STATUS_NO_PA_DATA",
  sDescription =    "Expected to find PA data for a hint of what etype to use, but it was not found.");
fAddWindowsDefine("STATUS_PKINIT_NAME_MISMATCH",
  sDescription =    "The client certificate does not contain a valid UPN, or does not match the client name in the logon request. Contact your administrator.");
fAddWindowsDefine("STATUS_SMARTCARD_LOGON_REQUIRED",
  sDescription =    "Smart card logon is required and was not used.");
fAddWindowsDefine("STATUS_KDC_INVALID_REQUEST",
  sDescription =    "An invalid request was sent to the KDC.");
fAddWindowsDefine("STATUS_KDC_UNABLE_TO_REFER",
  sDescription =    "The KDC was unable to generate a referral for the service requested.");
fAddWindowsDefine("STATUS_KDC_UNKNOWN_ETYPE",
  sDescription =    "The encryption type requested is not supported by the KDC.");
fAddWindowsDefine("STATUS_SHUTDOWN_IN_PROGRESS",
  sDescription =    "A system shutdown is in progress.");
fAddWindowsDefine("STATUS_SERVER_SHUTDOWN_IN_PROGRESS",
  sDescription =    "The server machine is shutting down.");
fAddWindowsDefine("STATUS_NOT_SUPPORTED_ON_SBS",
  sDescription =    "This operation is not supported on a computer running Windows Server 2003 operating system for Small Business Server.");
fAddWindowsDefine("STATUS_WMI_GUID_DISCONNECTED",
  sDescription =    "The WMI GUID is no longer available.");
fAddWindowsDefine("STATUS_WMI_ALREADY_DISABLED",
  sDescription =    "Collection or events for the WMI GUID is already disabled.");
fAddWindowsDefine("STATUS_WMI_ALREADY_ENABLED",
  sDescription =    "Collection or events for the WMI GUID is already enabled.");
fAddWindowsDefine("STATUS_MFT_TOO_FRAGMENTED",
  sDescription =    "The master file table on the volume is too fragmented to complete this operation.");
fAddWindowsDefine("STATUS_COPY_PROTECTION_FAILURE",
  sDescription =    "Copy protection failure.");
fAddWindowsDefine("STATUS_CSS_AUTHENTICATION_FAILURE",
  sDescription =    "Copy protection error-DVD CSS Authentication failed.");
fAddWindowsDefine("STATUS_CSS_KEY_NOT_PRESENT",
  sDescription =    "Copy protection error-The specified sector does not contain a valid key.");
fAddWindowsDefine("STATUS_CSS_KEY_NOT_ESTABLISHED",
  sDescription =    "Copy protection error-DVD session key not established.");
fAddWindowsDefine("STATUS_CSS_SCRAMBLED_SECTOR",
  sDescription =    "Copy protection error-The read failed because the sector is encrypted.");
fAddWindowsDefine("STATUS_CSS_REGION_MISMATCH",
  sDescription =    "Copy protection error-The region of the specified DVD does not correspond to the region setting of the drive.");
fAddWindowsDefine("STATUS_CSS_RESETS_EXHAUSTED",
  sDescription =    "Copy protection error-The region setting of the drive might be permanent.");
fAddWindowsDefine("STATUS_PKINIT_FAILURE",
  sDescription =    "The Kerberos protocol encountered an error while validating the KDC certificate during smart card logon. There is more information in the system event log.");
fAddWindowsDefine("STATUS_SMARTCARD_SUBSYSTEM_FAILURE",
  sDescription =    "The Kerberos protocol encountered an error while attempting to use the smart card subsystem.");
fAddWindowsDefine("STATUS_NO_KERB_KEY",
  sDescription =    "The target server does not have acceptable Kerberos credentials.");
fAddWindowsDefine("STATUS_HOST_DOWN",
  sDescription =    "The transport determined that the remote system is down.");
fAddWindowsDefine("STATUS_UNSUPPORTED_PREAUTH",
  sDescription =    "An unsupported pre-authentication mechanism was presented to the Kerberos package.");
fAddWindowsDefine("STATUS_EFS_ALG_BLOB_TOO_BIG",
  sDescription =    "The encryption algorithm that is used on the source file needs a bigger key buffer than the one that is used on the destination file.");
fAddWindowsDefine("STATUS_PORT_NOT_SET",
  sDescription =    "An attempt to remove a processes DebugPort was made, but a port was not already associated with the process.");
fAddWindowsDefine("STATUS_DEBUGGER_INACTIVE",
  sDescription =    "An attempt to do an operation on a debug port failed because the port is in the process of being deleted.");
fAddWindowsDefine("STATUS_DS_VERSION_CHECK_FAILURE",
  sDescription =    "This version of Windows is not compatible with the behavior version of the directory forest, domain, or domain controller.");
fAddWindowsDefine("STATUS_AUDITING_DISABLED",
  sDescription =    "The specified event is currently not being audited.");
fAddWindowsDefine("STATUS_PRENT4_MACHINE_ACCOUNT",
  sDescription =    "The machine account was created prior to Windows NT 4.0 operating system. The account needs to be recreated.");
fAddWindowsDefine("STATUS_DS_AG_CANT_HAVE_UNIVERSAL_MEMBER",
  sDescription =    "An account group cannot have a universal group as a member.");
fAddWindowsDefine("STATUS_INVALID_IMAGE_WIN_32",
  sDescription =    "The specified image file did not have the correct format; it appears to be a 32-bit Windows image.");
fAddWindowsDefine("STATUS_INVALID_IMAGE_WIN_64",
  sDescription =    "The specified image file did not have the correct format; it appears to be a 64-bit Windows image.");
fAddWindowsDefine("STATUS_BAD_BINDINGS",
  sDescription =    "The client's supplied SSPI channel bindings were incorrect.");
fAddWindowsDefine("STATUS_NETWORK_SESSION_EXPIRED",
  sDescription =    "The client session has expired; so the client must re-authenticate to continue accessing the remote resources.");
fAddWindowsDefine("STATUS_APPHELP_BLOCK",
  sDescription =    "The AppHelp dialog box canceled; thus preventing the application from starting.");
fAddWindowsDefine("STATUS_ALL_SIDS_FILTERED",
  sDescription =    "The SID filtering operation removed all SIDs.");
fAddWindowsDefine("STATUS_NOT_SAFE_MODE_DRIVER",
  sDescription =    "The driver was not loaded because the system is starting in safe mode.");
fAddWindowsDefine("STATUS_ACCESS_DISABLED_BY_POLICY_DEFAULT",
  sDescription =    "Access to %1 has been restricted by your Administrator by the default software restriction policy level.");
fAddWindowsDefine("STATUS_ACCESS_DISABLED_BY_POLICY_PATH",
  sDescription =    "Access to %1 has been restricted by your Administrator by location with policy rule %2 placed on path %3.");
fAddWindowsDefine("STATUS_ACCESS_DISABLED_BY_POLICY_PUBLISHER",
  sDescription =    "Access to %1 has been restricted by your Administrator by software publisher policy.");
fAddWindowsDefine("STATUS_ACCESS_DISABLED_BY_POLICY_OTHER",
  sDescription =    "Access to %1 has been restricted by your Administrator by policy rule %2.");
fAddWindowsDefine("STATUS_FAILED_DRIVER_ENTRY",
  sDescription =    "The driver was not loaded because it failed its initialization call.");
fAddWindowsDefine("STATUS_DEVICE_ENUMERATION_ERROR",
  sDescription =    "The device encountered an error while applying power or reading the device configuration. This might be caused by a failure of your hardware or by a poor connection.");
fAddWindowsDefine("STATUS_MOUNT_POINT_NOT_RESOLVED",
  sDescription =    "The create operation failed because the name contained at least one mount point that resolves to a volume to which the specified device object is not attached.");
fAddWindowsDefine("STATUS_INVALID_DEVICE_OBJECT_PARAMETER",
  sDescription =    "The device object parameter is either not a valid device object or is not attached to the volume that is specified by the file name.");
fAddWindowsDefine("STATUS_MCA_OCCURED",
  sDescription =    "A machine check error has occurred. Check the system event log for additional information.");
fAddWindowsDefine("STATUS_DRIVER_BLOCKED_CRITICAL",
  sDescription =    "Driver %2 has been blocked from loading.");
fAddWindowsDefine("STATUS_DRIVER_BLOCKED",
  sDescription =    "Driver %2 has been blocked from loading.");
fAddWindowsDefine("STATUS_DRIVER_DATABASE_ERROR",
  sDescription =    "There was error [%2] processing the driver database.");
fAddWindowsDefine("STATUS_SYSTEM_HIVE_TOO_LARGE",
  sDescription =    "System hive size has exceeded its limit.");
fAddWindowsDefine("STATUS_INVALID_IMPORT_OF_NON_DLL",
  sDescription =    "A dynamic link library (DLL) referenced a module that was neither a DLL nor the process's executable image.");
fAddWindowsDefine("STATUS_NO_SECRETS",
  sDescription =    "The local account store does not contain secret material for the specified account.");
fAddWindowsDefine("STATUS_ACCESS_DISABLED_NO_SAFER_UI_BY_POLICY",
  sDescription =    "Access to %1 has been restricted by your Administrator by policy rule %2.");
fAddWindowsDefine("STATUS_FAILED_STACK_SWITCH",
  sDescription =    "The system was not able to allocate enough memory to perform a stack switch.");
fAddWindowsDefine("STATUS_HEAP_CORRUPTION",
  sDescription =    "A heap has been corrupted.");
fAddWindowsDefine("STATUS_SMARTCARD_WRONG_PIN",
  sDescription =    "An incorrect PIN was presented to the smart card.");
fAddWindowsDefine("STATUS_SMARTCARD_CARD_BLOCKED",
  sDescription =    "The smart card is blocked.");
fAddWindowsDefine("STATUS_SMARTCARD_CARD_NOT_AUTHENTICATED",
  sDescription =    "No PIN was presented to the smart card.");
fAddWindowsDefine("STATUS_SMARTCARD_NO_CARD",
  sDescription =    "No smart card is available.");
fAddWindowsDefine("STATUS_SMARTCARD_NO_KEY_CONTAINER",
  sDescription =    "The requested key container does not exist on the smart card.");
fAddWindowsDefine("STATUS_SMARTCARD_NO_CERTIFICATE",
  sDescription =    "The requested certificate does not exist on the smart card.");
fAddWindowsDefine("STATUS_SMARTCARD_NO_KEYSET",
  sDescription =    "The requested keyset does not exist.");
fAddWindowsDefine("STATUS_SMARTCARD_IO_ERROR",
  sDescription =    "A communication error with the smart card has been detected.");
fAddWindowsDefine("STATUS_DOWNGRADE_DETECTED",
  sDescription =    "The system detected a possible attempt to compromise security. Ensure that you can contact the server that authenticated you.");
fAddWindowsDefine("STATUS_SMARTCARD_CERT_REVOKED",
  sDescription =    "The smart card certificate used for authentication has been revoked. Contact your system administrator. There might be additional information in the event log.");
fAddWindowsDefine("STATUS_ISSUING_CA_UNTRUSTED",
  sDescription =    "An untrusted certificate authority was detected while processing the smart card certificate that is used for authentication. Contact your system administrator.");
fAddWindowsDefine("STATUS_REVOCATION_OFFLINE_C",
  sDescription =    "The revocation status of the smart card certificate that is used for authentication could not be determined. Contact your system administrator.");
fAddWindowsDefine("STATUS_PKINIT_CLIENT_FAILURE",
  sDescription =    "The smart card certificate used for authentication was not trusted. Contact your system administrator.");
fAddWindowsDefine("STATUS_SMARTCARD_CERT_EXPIRED",
  sDescription =    "The smart card certificate used for authentication has expired. Contact your system administrator.");
fAddWindowsDefine("STATUS_DRIVER_FAILED_PRIOR_UNLOAD",
  sDescription =    "The driver could not be loaded because a previous version of the driver is still in memory.");
fAddWindowsDefine("STATUS_SMARTCARD_SILENT_CONTEXT",
  sDescription =    "The smart card provider could not perform the action because the context was acquired as silent.");
fAddWindowsDefine("STATUS_PER_USER_TRUST_QUOTA_EXCEEDED",
  sDescription =    "The delegated trust creation quota of the current user has been exceeded.");
fAddWindowsDefine("STATUS_ALL_USER_TRUST_QUOTA_EXCEEDED",
  sDescription =    "The total delegated trust creation quota has been exceeded.");
fAddWindowsDefine("STATUS_USER_DELETE_TRUST_QUOTA_EXCEEDED",
  sDescription =    "The delegated trust deletion quota of the current user has been exceeded.");
fAddWindowsDefine("STATUS_DS_NAME_NOT_UNIQUE",
  sDescription =    "The requested name already exists as a unique identifier.");
fAddWindowsDefine("STATUS_DS_DUPLICATE_ID_FOUND",
  sDescription =    "The requested object has a non-unique identifier and cannot be retrieved.");
fAddWindowsDefine("STATUS_DS_GROUP_CONVERSION_ERROR",
  sDescription =    "The group cannot be converted due to attribute restrictions on the requested group type.");
fAddWindowsDefine("STATUS_VOLSNAP_PREPARE_HIBERNATE",
  sDescription =    "Wait while the Volume Shadow Copy Service prepares volume %hs for hibernation.");
fAddWindowsDefine("STATUS_USER2USER_REQUIRED",
  sDescription =    "Kerberos sub-protocol User2User is required.");
fAddWindowsDefine("STATUS_STACK_BUFFER_OVERRUN",
  sDescription =    "The system detected an overrun of a stack-based buffer in this application. This overrun could potentially allow a malicious user to gain control of this application.",
  sTypeId =         "FailFast2",
                             sSecurityImpact = "Potentially exploitable security issue");
fAddWindowsDefine("STATUS_NO_S4U_PROT_SUPPORT",
  sDescription =    "The Kerberos subsystem encountered an error. A service for user protocol request was made against a domain controller which does not support service for user.");
fAddWindowsDefine("STATUS_CROSSREALM_DELEGATION_FAILURE",
  sDescription =    "An attempt was made by this server to make a Kerberos constrained delegation request for a target that is outside the server realm. This action is not supported and the resulting error indicates a misconfiguration on the allowed-to-delegate-to list for this server. Contact your administrator.");
fAddWindowsDefine("STATUS_REVOCATION_OFFLINE_KDC",
  sDescription =    "The revocation status of the domain controller certificate used for smart card authentication could not be determined. There is additional information in the system event log. Contact your system administrator.");
fAddWindowsDefine("STATUS_ISSUING_CA_UNTRUSTED_KDC",
  sDescription =    "An untrusted certificate authority was detected while processing the domain controller certificate used for authentication. There is additional information in the system event log. Contact your system administrator.");
fAddWindowsDefine("STATUS_KDC_CERT_EXPIRED",
  sDescription =    "The domain controller certificate used for smart card logon has expired. Contact your system administrator with the contents of your system event log.");
fAddWindowsDefine("STATUS_KDC_CERT_REVOKED",
  sDescription =    "The domain controller certificate used for smart card logon has been revoked. Contact your system administrator with the contents of your system event log.");
fAddWindowsDefine("STATUS_PARAMETER_QUOTA_EXCEEDED",
  sDescription =    "Data present in one of the parameters is more than the function can operate on.");
fAddWindowsDefine("STATUS_HIBERNATION_FAILURE",
  sDescription =    "The system has failed to hibernate (The error code is %hs). Hibernation will be disabled until the system is restarted.");
fAddWindowsDefine("STATUS_DELAY_LOAD_FAILED",
  sDescription =    "An attempt to delay-load a .dll or get a function address in a delay-loaded .dll failed.");
fAddWindowsDefine("STATUS_AUTHENTICATION_FIREWALL_FAILED",
  sDescription =    "Logon Failure: The machine you are logging onto is protected by an authentication firewall. The specified account is not allowed to authenticate to the machine.");
fAddWindowsDefine("STATUS_VDM_DISALLOWED",
  sDescription =    "%hs is a 16-bit application. You do not have permissions to execute 16-bit applications. Check your permissions with your system administrator.");
fAddWindowsDefine("STATUS_HUNG_DISPLAY_DRIVER_THREAD",
  sDescription =    "The %hs display driver has stopped working normally. Save your work and reboot the system to restore full display functionality. The next time you reboot the machine a dialog will be displayed giving you a chance to report this failure to Microsoft.");
fAddWindowsDefine("STATUS_INSUFFICIENT_RESOURCE_FOR_SPECIFIED_SHARED_SECTION_SIZE",
  sDescription =    "The Desktop heap encountered an error while allocating session memory. There is more information in the system event log.");
fAddWindowsDefine("STATUS_INVALID_CRUNTIME_PARAMETER",
  sDescription =    "An invalid parameter was passed to a C runtime function.");
fAddWindowsDefine("STATUS_NTLM_BLOCKED",
  sDescription =    "The authentication failed because NTLM was blocked.");
fAddWindowsDefine("STATUS_DS_SRC_SID_EXISTS_IN_FOREST",
  sDescription =    "The source object's SID already exists in destination forest.");
fAddWindowsDefine("STATUS_DS_DOMAIN_NAME_EXISTS_IN_FOREST",
  sDescription =    "The domain name of the trusted domain already exists in the forest.");
fAddWindowsDefine("STATUS_DS_FLAT_NAME_EXISTS_IN_FOREST",
  sDescription =    "The flat name of the trusted domain already exists in the forest.");
fAddWindowsDefine("STATUS_INVALID_USER_PRINCIPAL_NAME",
  sDescription =    "The User Principal Name (UPN) is invalid.");
fAddWindowsDefine("STATUS_FATAL_USER_CALLBACK_EXCEPTION",
  sDescription =    "An unhandled exception was encountered during a user callback.",
  sTypeId =         "Verifier",
                             sSecurityImpact = "May be a security issue");
fAddWindowsDefine("STATUS_ASSERTION_FAILURE",
  sDescription =    "There has been an assertion failure.");
fAddWindowsDefine("STATUS_VERIFIER_STOP",
  sDescription =    "Application verifier has found an error in the current process.");
fAddWindowsDefine("STATUS_CALLBACK_POP_STACK",
  sDescription =    "A user mode unwind is in progress.");
fAddWindowsDefine("STATUS_INCOMPATIBLE_DRIVER_BLOCKED",
  sDescription =    "%2 has been blocked from loading due to incompatibility with this system. Contact your software vendor for a compatible version of the driver.");
fAddWindowsDefine("STATUS_HIVE_UNLOADED",
  sDescription =    "Illegal operation attempted on a registry key which has already been unloaded.");
fAddWindowsDefine("STATUS_COMPRESSION_DISABLED",
  sDescription =    "Compression is disabled for this volume.");
fAddWindowsDefine("STATUS_FILE_SYSTEM_LIMITATION",
  sDescription =    "The requested operation could not be completed due to a file system limitation.");
fAddWindowsDefine("STATUS_INVALID_IMAGE_HASH",
  sDescription =    "The hash for image %hs cannot be found in the system catalogs. The image is likely corrupt or the victim of tampering.");
fAddWindowsDefine("STATUS_NOT_CAPABLE",
  sDescription =    "The implementation is not capable of performing the request.");
fAddWindowsDefine("STATUS_REQUEST_OUT_OF_SEQUENCE",
  sDescription =    "The requested operation is out of order with respect to other operations.");
fAddWindowsDefine("STATUS_IMPLEMENTATION_LIMIT",
  sDescription =    "An operation attempted to exceed an implementation-defined limit.");
fAddWindowsDefine("STATUS_ELEVATION_REQUIRED",
  sDescription =    "The requested operation requires elevation.");
fAddWindowsDefine("STATUS_NO_SECURITY_CONTEXT",
  sDescription =    "The required security context does not exist.");
fAddWindowsDefine("STATUS_PKU2U_CERT_FAILURE",
  sDescription =    "The PKU2U protocol encountered an error while attempting to utilize the associated certificates.");
fAddWindowsDefine("STATUS_BEYOND_VDL",
  sDescription =    "The operation was attempted beyond the valid data length of the file.");
fAddWindowsDefine("STATUS_ENCOUNTERED_WRITE_IN_PROGRESS",
  sDescription =    "The attempted write operation encountered a write already in progress for some portion of the range.");
fAddWindowsDefine("STATUS_PTE_CHANGED",
  sDescription =    "The page fault mappings changed in the middle of processing a fault so the operation must be retried.");
fAddWindowsDefine("STATUS_PURGE_FAILED",
  sDescription =    "The attempt to purge this file from memory failed to purge some or all the data from memory.");
fAddWindowsDefine("STATUS_CRED_REQUIRES_CONFIRMATION",
  sDescription =    "The requested credential requires confirmation.");
fAddWindowsDefine("STATUS_CS_ENCRYPTION_INVALID_SERVER_RESPONSE",
  sDescription =    "The remote server sent an invalid response for a file being opened with Client Side Encryption.");
fAddWindowsDefine("STATUS_CS_ENCRYPTION_UNSUPPORTED_SERVER",
  sDescription =    "Client Side Encryption is not supported by the remote server even though it claims to support it.");
fAddWindowsDefine("STATUS_CS_ENCRYPTION_EXISTING_ENCRYPTED_FILE",
  sDescription =    "File is encrypted and should be opened in Client Side Encryption mode.");
fAddWindowsDefine("STATUS_CS_ENCRYPTION_NEW_ENCRYPTED_FILE",
  sDescription =    "A new encrypted file is being created and a $EFS needs to be provided.");
fAddWindowsDefine("STATUS_CS_ENCRYPTION_FILE_NOT_CSE",
  sDescription =    "The SMB client requested a CSE FSCTL on a non-CSE file.");
fAddWindowsDefine("STATUS_INVALID_LABEL",
  sDescription =    "Indicates a particular Security ID cannot be assigned as the label of an object.");
fAddWindowsDefine("STATUS_DRIVER_PROCESS_TERMINATED",
  sDescription =    "The process hosting the driver for this device has terminated.");
fAddWindowsDefine("STATUS_AMBIGUOUS_SYSTEM_DEVICE",
  sDescription =    "The requested system device cannot be identified due to multiple indistinguishable devices potentially matching the identification criteria.");
fAddWindowsDefine("STATUS_SYSTEM_DEVICE_NOT_FOUND",
  sDescription =    "The requested system device cannot be found.");
fAddWindowsDefine("STATUS_RESTART_BOOT_APPLICATION",
  sDescription =    "This boot application must be restarted.");
fAddWindowsDefine("STATUS_INSUFFICIENT_NVRAM_RESOURCES",
  sDescription =    "Insufficient NVRAM resources exist to complete the API.  A reboot might be required.");
fAddWindowsDefine("STATUS_NO_RANGES_PROCESSED",
  sDescription =    "No ranges for the specified operation were able to be processed.");
fAddWindowsDefine("STATUS_DEVICE_FEATURE_NOT_SUPPORTED",
  sDescription =    "The storage device does not support Offload Write.");
fAddWindowsDefine("STATUS_DEVICE_UNREACHABLE",
  sDescription =    "Data cannot be moved because the source device cannot communicate with the destination device.");
fAddWindowsDefine("STATUS_INVALID_TOKEN",
  sDescription =    "The token representing the data is invalid or expired.");
fAddWindowsDefine("STATUS_SERVER_UNAVAILABLE",
  sDescription =    "The file server is temporarily unavailable.");
fAddWindowsDefine("STATUS_FILE_NOT_AVAILABLE",
  sDescription =    "The file is temporarily unavailable.");
fAddWindowsDefine("STATUS_SHARE_UNAVAILABLE",
  sDescription =    "The share is temporarily unavailable.");
fAddWindowsDefine("STATUS_INVALID_TASK_NAME",
  sDescription =    "The specified task name is invalid.");
fAddWindowsDefine("STATUS_INVALID_TASK_INDEX",
  sDescription =    "The specified task index is invalid.");
fAddWindowsDefine("STATUS_THREAD_ALREADY_IN_TASK",
  sDescription =    "The specified thread is already joining a task.");
fAddWindowsDefine("STATUS_CALLBACK_BYPASS",
  sDescription =    "A callback has requested to bypass native code.");
fAddWindowsDefine("STATUS_FAIL_FAST_EXCEPTION",
  sDescription =    "A fail fast exception occurred. Exception handlers will not be invoked and the process will be terminated immediately.",
  sTypeId =         "FailFast",
                             sSecurityImpact = "May be a security issue");
fAddWindowsDefine("STATUS_IMAGE_CERT_REVOKED",
  sDescription =    "Windows cannot verify the digital signature for this file. The signing certificate for this file has been revoked.");
fAddWindowsDefine("STATUS_PORT_CLOSED",
  sDescription =    "The ALPC port is closed.");
fAddWindowsDefine("STATUS_MESSAGE_LOST",
  sDescription =    "The ALPC message requested is no longer available.");
fAddWindowsDefine("STATUS_INVALID_MESSAGE",
  sDescription =    "The ALPC message supplied is invalid.");
fAddWindowsDefine("STATUS_REQUEST_CANCELED",
  sDescription =    "The ALPC message has been canceled.");
fAddWindowsDefine("STATUS_RECURSIVE_DISPATCH",
  sDescription =    "Invalid recursive dispatch attempt.");
fAddWindowsDefine("STATUS_LPC_RECEIVE_BUFFER_EXPECTED",
  sDescription =    "No receive buffer has been supplied in a synchronous request.");
fAddWindowsDefine("STATUS_LPC_INVALID_CONNECTION_USAGE",
  sDescription =    "The connection port is used in an invalid context.");
fAddWindowsDefine("STATUS_LPC_REQUESTS_NOT_ALLOWED",
  sDescription =    "The ALPC port does not accept new request messages.");
fAddWindowsDefine("STATUS_RESOURCE_IN_USE",
  sDescription =    "The resource requested is already in use.");
fAddWindowsDefine("STATUS_HARDWARE_MEMORY_ERROR",
  sDescription =    "The hardware has reported an uncorrectable memory error.");
fAddWindowsDefine("STATUS_THREADPOOL_HANDLE_EXCEPTION",
  sDescription =    "Status 0x%08x was returned, waiting on handle 0x%x for wait 0x%p, in waiter 0x%p.");
fAddWindowsDefine("STATUS_THREADPOOL_SET_EVENT_ON_COMPLETION_FAILED",
  sDescription =    "After a callback to 0x%p(0x%p), a completion call to Set event(0x%p) failed with status 0x%08x.");
fAddWindowsDefine("STATUS_THREADPOOL_RELEASE_SEMAPHORE_ON_COMPLETION_FAILED",
  sDescription =    "After a callback to 0x%p(0x%p), a completion call to ReleaseSemaphore(0x%p, %d) failed with status 0x%08x.");
fAddWindowsDefine("STATUS_THREADPOOL_RELEASE_MUTEX_ON_COMPLETION_FAILED",
  sDescription =    "After a callback to 0x%p(0x%p), a completion call to ReleaseMutex(%p) failed with status 0x%08x.");
fAddWindowsDefine("STATUS_THREADPOOL_FREE_LIBRARY_ON_COMPLETION_FAILED",
  sDescription =    "After a callback to 0x%p(0x%p), a completion call to FreeLibrary(%p) failed with status 0x%08x.");
fAddWindowsDefine("STATUS_THREADPOOL_RELEASED_DURING_OPERATION",
  sDescription =    "The thread pool 0x%p was released while a thread was posting a callback to 0x%p(0x%p) to it.");
fAddWindowsDefine("STATUS_CALLBACK_RETURNED_WHILE_IMPERSONATING",
  sDescription =    "A thread pool worker thread is impersonating a client, after a callback to 0x%p(0x%p). This is unexpected, indicating that the callback is missing a call to revert the impersonation.");
fAddWindowsDefine("STATUS_APC_RETURNED_WHILE_IMPERSONATING",
  sDescription =    "A thread pool worker thread is impersonating a client, after executing an APC. This is unexpected, indicating that the APC is missing a call to revert the impersonation.");
fAddWindowsDefine("STATUS_PROCESS_IS_PROTECTED",
  sDescription =    "Either the target process, or the target thread's containing process, is a protected process.");
fAddWindowsDefine("STATUS_MCA_EXCEPTION",
  sDescription =    "A thread is getting dispatched with MCA EXCEPTION because of MCA.");
fAddWindowsDefine("STATUS_CERTIFICATE_MAPPING_NOT_UNIQUE",
  sDescription =    "The client certificate account mapping is not unique.");
fAddWindowsDefine("STATUS_SYMLINK_CLASS_DISABLED",
  sDescription =    "The symbolic link cannot be followed because its type is disabled.");
fAddWindowsDefine("STATUS_INVALID_IDN_NORMALIZATION",
  sDescription =    "Indicates that the specified string is not valid for IDN normalization.");
fAddWindowsDefine("STATUS_NO_UNICODE_TRANSLATION",
  sDescription =    "No mapping for the Unicode character exists in the target multi-byte code page.");
fAddWindowsDefine("STATUS_ALREADY_REGISTERED",
  sDescription =    "The provided callback is already registered.");
fAddWindowsDefine("STATUS_CONTEXT_MISMATCH",
  sDescription =    "The provided context did not match the target.");
fAddWindowsDefine("STATUS_PORT_ALREADY_HAS_COMPLETION_LIST",
  sDescription =    "The specified port already has a completion list.");
fAddWindowsDefine("STATUS_CALLBACK_RETURNED_THREAD_PRIORITY",
  sDescription =    "A threadpool worker thread entered a callback at thread base priority 0x%x and exited at priority 0x%x. This is unexpected, indicating that the callback missed restoring the priority.");
fAddWindowsDefine("STATUS_INVALID_THREAD",
  sDescription =    "An invalid thread, handle %p, is specified for this operation. Possibly, a threadpool worker thread was specified.");
fAddWindowsDefine("STATUS_CALLBACK_RETURNED_TRANSACTION",
  sDescription =    "A threadpool worker thread entered a callback, which left transaction state. This is unexpected, indicating that the callback missed clearing the transaction.");
fAddWindowsDefine("STATUS_CALLBACK_RETURNED_LDR_LOCK",
  sDescription =    "A threadpool worker thread entered a callback, which left the loader lock held. This is unexpected, indicating that the callback missed releasing the lock.");
fAddWindowsDefine("STATUS_CALLBACK_RETURNED_LANG",
  sDescription =    "A threadpool worker thread entered a callback, which left with preferred languages set. This is unexpected, indicating that the callback missed clearing them.");
fAddWindowsDefine("STATUS_CALLBACK_RETURNED_PRI_BACK",
  sDescription =    "A threadpool worker thread entered a callback, which left with background priorities set. This is unexpected, indicating that the callback missed restoring the original priorities.");
fAddWindowsDefine("STATUS_CALLBACK_RETURNED_THREAD_AFFINITY",
  sDescription =    "A threadpool worker thread entered a callback at thread affinity %p and exited at affinity %p. This is unexpected, indicating that the callback missed restoring the priority.");
fAddWindowsDefine("STATUS_DISK_REPAIR_DISABLED",
  sDescription =    "The attempted operation required self healing to be enabled.");
fAddWindowsDefine("STATUS_DS_DOMAIN_RENAME_IN_PROGRESS",
  sDescription =    "The directory service cannot perform the requested operation because a domain rename operation is in progress.");
fAddWindowsDefine("STATUS_DISK_QUOTA_EXCEEDED",
  sDescription =    "An operation failed because the storage quota was exceeded.");
fAddWindowsDefine("STATUS_CONTENT_BLOCKED",
  sDescription =    "An operation failed because the content was blocked.");
fAddWindowsDefine("STATUS_BAD_CLUSTERS",
  sDescription =    "The operation could not be completed due to bad clusters on disk.");
fAddWindowsDefine("STATUS_VOLUME_DIRTY",
  sDescription =    "The operation could not be completed because the volume is dirty. Please run the Chkdsk utility and try again.");
fAddWindowsDefine("STATUS_FILE_CHECKED_OUT",
  sDescription =    "This file is checked out or locked for editing by another user.");
fAddWindowsDefine("STATUS_CHECKOUT_REQUIRED",
  sDescription =    "The file must be checked out before saving changes.");
fAddWindowsDefine("STATUS_BAD_FILE_TYPE",
  sDescription =    "The file type being saved or retrieved has been blocked.");
fAddWindowsDefine("STATUS_FILE_TOO_LARGE",
  sDescription =    "The file size exceeds the limit allowed and cannot be saved.");
fAddWindowsDefine("STATUS_FORMS_AUTH_REQUIRED",
  sDescription =    "Access Denied. Before opening files in this location, you must first browse to the e.g. site and select the option to log on automatically.");
fAddWindowsDefine("STATUS_VIRUS_INFECTED",
  sDescription =    "The operation did not complete successfully because the file contains a virus.");
fAddWindowsDefine("STATUS_VIRUS_DELETED",
  sDescription =    "This file contains a virus and cannot be opened. Due to the nature of this virus, the file has been removed from this location.");
fAddWindowsDefine("STATUS_BAD_MCFG_TABLE",
  sDescription =    "The resources required for this device conflict with the MCFG table.");
fAddWindowsDefine("STATUS_CANNOT_BREAK_OPLOCK",
  sDescription =    "The operation did not complete successfully because it would cause an oplock to be broken. The caller has requested that existing oplocks not be broken.");
fAddWindowsDefine("STATUS_WOW_ASSERTION",
  sDescription =    "WOW Assertion Error.");
fAddWindowsDefine("STATUS_INVALID_SIGNATURE",
  sDescription =    "The cryptographic signature is invalid.");
fAddWindowsDefine("STATUS_HMAC_NOT_SUPPORTED",
  sDescription =    "The cryptographic provider does not support HMAC.");
fAddWindowsDefine("STATUS_IPSEC_QUEUE_OVERFLOW",
  sDescription =    "The IPsec queue overflowed.");
fAddWindowsDefine("STATUS_ND_QUEUE_OVERFLOW",
  sDescription =    "The neighbor discovery queue overflowed.");
fAddWindowsDefine("STATUS_HOPLIMIT_EXCEEDED",
  sDescription =    "An Internet Control Message Protocol (ICMP) hop limit exceeded error was received.");
fAddWindowsDefine("STATUS_PROTOCOL_NOT_SUPPORTED",
  sDescription =    "The protocol is not installed on the local machine.");
fAddWindowsDefine("STATUS_LOST_WRITEBEHIND_DATA_NETWORK_DISCONNECTED",
  sDescription =    "Windows was unable to save all the data for the file %hs; the data has been lost. This error might be caused by network connectivity issues. Try to save this file elsewhere.");
fAddWindowsDefine("STATUS_LOST_WRITEBEHIND_DATA_NETWORK_SERVER_ERROR",
  sDescription =    "Windows was unable to save all the data for the file %hs; the data has been lost. This error was returned by the server on which the file exists. Try to save this file elsewhere.");
fAddWindowsDefine("STATUS_LOST_WRITEBEHIND_DATA_LOCAL_DISK_ERROR",
  sDescription =    "Windows was unable to save all the data for the file %hs; the data has been lost. This error might be caused if the device has been removed or the media is write-protected.");
fAddWindowsDefine("STATUS_XML_PARSE_ERROR",
  sDescription =    "Windows was unable to parse the requested XML data.");
fAddWindowsDefine("STATUS_XMLDSIG_ERROR",
  sDescription =    "An error was encountered while processing an XML digital signature.");
fAddWindowsDefine("STATUS_WRONG_COMPARTMENT",
  sDescription =    "This indicates that the caller made the connection request in the wrong routing compartment.");
fAddWindowsDefine("STATUS_AUTHIP_FAILURE",
  sDescription =    "This indicates that there was an AuthIP failure when attempting to connect to the remote host.");
fAddWindowsDefine("STATUS_DS_OID_MAPPED_GROUP_CANT_HAVE_MEMBERS",
  sDescription =    "OID mapped groups cannot have members.");
fAddWindowsDefine("STATUS_DS_OID_NOT_FOUND",
  sDescription =    "The specified OID cannot be found.");
fAddWindowsDefine("STATUS_HASH_NOT_SUPPORTED",
  sDescription =    "Hash generation for the specified version and hash type is not enabled on server.");
fAddWindowsDefine("STATUS_HASH_NOT_PRESENT",
  sDescription =    "The hash requests is not present or not up to date with the current file contents.");
fAddWindowsDefine("STATUS_OFFLOAD_READ_FLT_NOT_SUPPORTED",
  sDescription =    "A file system filter on the server has not opted in for Offload Read support.");
fAddWindowsDefine("STATUS_OFFLOAD_WRITE_FLT_NOT_SUPPORTED",
  sDescription =    "A file system filter on the server has not opted in for Offload Write support.");
fAddWindowsDefine("STATUS_OFFLOAD_READ_FILE_NOT_SUPPORTED",
  sDescription =    "Offload read operations cannot be performed on: Compressed files, Sparse files, Encrypted files, File system metadata files");
fAddWindowsDefine("STATUS_OFFLOAD_WRITE_FILE_NOT_SUPPORTED",
  sDescription =    "Offload write operations cannot be performed on: Compressed files, Sparse files, Encrypted files, File system metadata files");
fAddWindowsDefine("DBG_NO_STATE_CHANGE",
  sDescription =    "The debugger did not perform a state change.");
fAddWindowsDefine("DBG_APP_NOT_IDLE",
  sDescription =    "The debugger found that the application is not idle.");
fAddWindowsDefine("RPC_NT_INVALID_STRING_BINDING",
  sDescription =    "The string binding is invalid.");
fAddWindowsDefine("RPC_NT_WRONG_KIND_OF_BINDING",
  sDescription =    "The binding handle is not the correct type.");
fAddWindowsDefine("RPC_NT_INVALID_BINDING",
  sDescription =    "The binding handle is invalid.");
fAddWindowsDefine("RPC_NT_PROTSEQ_NOT_SUPPORTED",
  sDescription =    "The RPC protocol sequence is not supported.");
fAddWindowsDefine("RPC_NT_INVALID_RPC_PROTSEQ",
  sDescription =    "The RPC protocol sequence is invalid.");
fAddWindowsDefine("RPC_NT_INVALID_STRING_UUID",
  sDescription =    "The string UUID is invalid.");
fAddWindowsDefine("RPC_NT_INVALID_ENDPOINT_FORMAT",
  sDescription =    "The endpoint format is invalid.");
fAddWindowsDefine("RPC_NT_INVALID_NET_ADDR",
  sDescription =    "The network address is invalid.");
fAddWindowsDefine("RPC_NT_NO_ENDPOINT_FOUND",
  sDescription =    "No endpoint was found.");
fAddWindowsDefine("RPC_NT_INVALID_TIMEOUT",
  sDescription =    "The time-out value is invalid.");
fAddWindowsDefine("RPC_NT_OBJECT_NOT_FOUND",
  sDescription =    "The object UUID was not found.");
fAddWindowsDefine("RPC_NT_ALREADY_REGISTERED",
  sDescription =    "The object UUID has already been registered.");
fAddWindowsDefine("RPC_NT_TYPE_ALREADY_REGISTERED",
  sDescription =    "The type UUID has already been registered.");
fAddWindowsDefine("RPC_NT_ALREADY_LISTENING",
  sDescription =    "The RPC server is already listening.");
fAddWindowsDefine("RPC_NT_NO_PROTSEQS_REGISTERED",
  sDescription =    "No protocol sequences have been registered.");
fAddWindowsDefine("RPC_NT_NOT_LISTENING",
  sDescription =    "The RPC server is not listening.");
fAddWindowsDefine("RPC_NT_UNKNOWN_MGR_TYPE",
  sDescription =    "The manager type is unknown.");
fAddWindowsDefine("RPC_NT_UNKNOWN_IF",
  sDescription =    "The interface is unknown.");
fAddWindowsDefine("RPC_NT_NO_BINDINGS",
  sDescription =    "There are no bindings.");
fAddWindowsDefine("RPC_NT_NO_PROTSEQS",
  sDescription =    "There are no protocol sequences.");
fAddWindowsDefine("RPC_NT_CANT_CREATE_ENDPOINT",
  sDescription =    "The endpoint cannot be created.");
fAddWindowsDefine("RPC_NT_OUT_OF_RESOURCES",
  sDescription =    "Insufficient resources are available to complete this operation.");
fAddWindowsDefine("RPC_NT_SERVER_UNAVAILABLE",
  sDescription =    "The RPC server is unavailable.");
fAddWindowsDefine("RPC_NT_SERVER_TOO_BUSY",
  sDescription =    "The RPC server is too busy to complete this operation.");
fAddWindowsDefine("RPC_NT_INVALID_NETWORK_OPTIONS",
  sDescription =    "The network options are invalid.");
fAddWindowsDefine("RPC_NT_NO_CALL_ACTIVE",
  sDescription =    "No RPCs are active on this thread.");
fAddWindowsDefine("RPC_NT_CALL_FAILED",
  sDescription =    "The RPC failed.");
fAddWindowsDefine("RPC_NT_CALL_FAILED_DNE",
  sDescription =    "The RPC failed and did not execute.");
fAddWindowsDefine("RPC_NT_PROTOCOL_ERROR",
  sDescription =    "An RPC protocol error occurred.");
fAddWindowsDefine("RPC_NT_UNSUPPORTED_TRANS_SYN",
  sDescription =    "The RPC server does not support the transfer syntax.");
fAddWindowsDefine("RPC_NT_UNSUPPORTED_TYPE",
  sDescription =    "The type UUID is not supported.");
fAddWindowsDefine("RPC_NT_INVALID_TAG",
  sDescription =    "The tag is invalid.");
fAddWindowsDefine("RPC_NT_INVALID_BOUND",
  sDescription =    "The array bounds are invalid.");
fAddWindowsDefine("RPC_NT_NO_ENTRY_NAME",
  sDescription =    "The binding does not contain an entry name.");
fAddWindowsDefine("RPC_NT_INVALID_NAME_SYNTAX",
  sDescription =    "The name syntax is invalid.");
fAddWindowsDefine("RPC_NT_UNSUPPORTED_NAME_SYNTAX",
  sDescription =    "The name syntax is not supported.");
fAddWindowsDefine("RPC_NT_UUID_NO_ADDRESS",
  sDescription =    "No network address is available to construct a UUID.");
fAddWindowsDefine("RPC_NT_DUPLICATE_ENDPOINT",
  sDescription =    "The endpoint is a duplicate.");
fAddWindowsDefine("RPC_NT_UNKNOWN_AUTHN_TYPE",
  sDescription =    "The authentication type is unknown.");
fAddWindowsDefine("RPC_NT_MAX_CALLS_TOO_SMALL",
  sDescription =    "The maximum number of calls is too small.");
fAddWindowsDefine("RPC_NT_STRING_TOO_LONG",
  sDescription =    "The string is too long.");
fAddWindowsDefine("RPC_NT_PROTSEQ_NOT_FOUND",
  sDescription =    "The RPC protocol sequence was not found.");
fAddWindowsDefine("RPC_NT_PROCNUM_OUT_OF_RANGE",
  sDescription =    "The procedure number is out of range.");
fAddWindowsDefine("RPC_NT_BINDING_HAS_NO_AUTH",
  sDescription =    "The binding does not contain any authentication information.");
fAddWindowsDefine("RPC_NT_UNKNOWN_AUTHN_SERVICE",
  sDescription =    "The authentication service is unknown.");
fAddWindowsDefine("RPC_NT_UNKNOWN_AUTHN_LEVEL",
  sDescription =    "The authentication level is unknown.");
fAddWindowsDefine("RPC_NT_INVALID_AUTH_IDENTITY",
  sDescription =    "The security context is invalid.");
fAddWindowsDefine("RPC_NT_UNKNOWN_AUTHZ_SERVICE",
  sDescription =    "The authorization service is unknown.");
fAddWindowsDefine("EPT_NT_INVALID_ENTRY",
  sDescription =    "The entry is invalid.");
fAddWindowsDefine("EPT_NT_CANT_PERFORM_OP",
  sDescription =    "The operation cannot be performed.");
fAddWindowsDefine("EPT_NT_NOT_REGISTERED",
  sDescription =    "No more endpoints are available from the endpoint mapper.");
fAddWindowsDefine("RPC_NT_NOTHING_TO_EXPORT",
  sDescription =    "No interfaces have been exported.");
fAddWindowsDefine("RPC_NT_INCOMPLETE_NAME",
  sDescription =    "The entry name is incomplete.");
fAddWindowsDefine("RPC_NT_INVALID_VERS_OPTION",
  sDescription =    "The version option is invalid.");
fAddWindowsDefine("RPC_NT_NO_MORE_MEMBERS",
  sDescription =    "There are no more members.");
fAddWindowsDefine("RPC_NT_NOT_ALL_OBJS_UNEXPORTED",
  sDescription =    "There is nothing to unexport.");
fAddWindowsDefine("RPC_NT_INTERFACE_NOT_FOUND",
  sDescription =    "The interface was not found.");
fAddWindowsDefine("RPC_NT_ENTRY_ALREADY_EXISTS",
  sDescription =    "The entry already exists.");
fAddWindowsDefine("RPC_NT_ENTRY_NOT_FOUND",
  sDescription =    "The entry was not found.");
fAddWindowsDefine("RPC_NT_NAME_SERVICE_UNAVAILABLE",
  sDescription =    "The name service is unavailable.");
fAddWindowsDefine("RPC_NT_INVALID_NAF_ID",
  sDescription =    "The network address family is invalid.");
fAddWindowsDefine("RPC_NT_CANNOT_SUPPORT",
  sDescription =    "The requested operation is not supported.");
fAddWindowsDefine("RPC_NT_NO_CONTEXT_AVAILABLE",
  sDescription =    "No security context is available to allow impersonation.");
fAddWindowsDefine("RPC_NT_INTERNAL_ERROR",
  sDescription =    "An internal error occurred in the RPC.");
fAddWindowsDefine("RPC_NT_ZERO_DIVIDE",
  sDescription =    "The RPC server attempted to divide an integer by zero.");
fAddWindowsDefine("RPC_NT_ADDRESS_ERROR",
  sDescription =    "An addressing error occurred in the RPC server.");
fAddWindowsDefine("RPC_NT_FP_DIV_ZERO",
  sDescription =    "A floating point operation at the RPC server caused a divide by zero.");
fAddWindowsDefine("RPC_NT_FP_UNDERFLOW",
  sDescription =    "A floating point underflow occurred at the RPC server.");
fAddWindowsDefine("RPC_NT_FP_OVERFLOW",
  sDescription =    "A floating point overflow occurred at the RPC server.");
fAddWindowsDefine("RPC_NT_CALL_IN_PROGRESS",
  sDescription =    "An RPC is already in progress for this thread.");
fAddWindowsDefine("RPC_NT_NO_MORE_BINDINGS",
  sDescription =    "There are no more bindings.");
fAddWindowsDefine("RPC_NT_GROUP_MEMBER_NOT_FOUND",
  sDescription =    "The group member was not found.");
fAddWindowsDefine("EPT_NT_CANT_CREATE",
  sDescription =    "The endpoint mapper database entry could not be created.");
fAddWindowsDefine("RPC_NT_INVALID_OBJECT",
  sDescription =    "The object UUID is the nil UUID.");
fAddWindowsDefine("RPC_NT_NO_INTERFACES",
  sDescription =    "No interfaces have been registered.");
fAddWindowsDefine("RPC_NT_CALL_CANCELLED",
  sDescription =    "The RPC was canceled.");
fAddWindowsDefine("RPC_NT_BINDING_INCOMPLETE",
  sDescription =    "The binding handle does not contain all the required information.");
fAddWindowsDefine("RPC_NT_COMM_FAILURE",
  sDescription =    "A communications failure occurred during an RPC.");
fAddWindowsDefine("RPC_NT_UNSUPPORTED_AUTHN_LEVEL",
  sDescription =    "The requested authentication level is not supported.");
fAddWindowsDefine("RPC_NT_NO_PRINC_NAME",
  sDescription =    "No principal name was registered.");
fAddWindowsDefine("RPC_NT_NOT_RPC_ERROR",
  sDescription =    "The error specified is not a valid Windows RPC error code.");
fAddWindowsDefine("RPC_NT_SEC_PKG_ERROR",
  sDescription =    "A security package-specific error occurred.");
fAddWindowsDefine("RPC_NT_NOT_CANCELLED",
  sDescription =    "The thread was not canceled.");
fAddWindowsDefine("RPC_NT_INVALID_ASYNC_HANDLE",
  sDescription =    "Invalid asynchronous RPC handle.");
fAddWindowsDefine("RPC_NT_INVALID_ASYNC_CALL",
  sDescription =    "Invalid asynchronous RPC call handle for this operation.");
fAddWindowsDefine("RPC_NT_PROXY_ACCESS_DENIED",
  sDescription =    "Access to the HTTP proxy is denied.");
fAddWindowsDefine("RPC_NT_NO_MORE_ENTRIES",
  sDescription =    "The list of RPC servers available for auto-handle binding has been exhausted.");
fAddWindowsDefine("RPC_NT_SS_CHAR_TRANS_OPEN_FAIL",
  sDescription =    "The file designated by DCERPCCHARTRANS cannot be opened.");
fAddWindowsDefine("RPC_NT_SS_CHAR_TRANS_SHORT_FILE",
  sDescription =    "The file containing the character translation table has fewer than 512 bytes.");
fAddWindowsDefine("RPC_NT_SS_IN_NULL_CONTEXT",
  sDescription =    "A null context handle is passed as an [in] parameter.");
fAddWindowsDefine("RPC_NT_SS_CONTEXT_MISMATCH",
  sDescription =    "The context handle does not match any known context handles.");
fAddWindowsDefine("RPC_NT_SS_CONTEXT_DAMAGED",
  sDescription =    "The context handle changed during a call.");
fAddWindowsDefine("RPC_NT_SS_HANDLES_MISMATCH",
  sDescription =    "The binding handles passed to an RPC do not match.");
fAddWindowsDefine("RPC_NT_SS_CANNOT_GET_CALL_HANDLE",
  sDescription =    "The stub is unable to get the call handle.");
fAddWindowsDefine("RPC_NT_NULL_REF_POINTER",
  sDescription =    "A null reference pointer was passed to the stub.");
fAddWindowsDefine("RPC_NT_ENUM_VALUE_OUT_OF_RANGE",
  sDescription =    "The enumeration value is out of range.");
fAddWindowsDefine("RPC_NT_BYTE_COUNT_TOO_SMALL",
  sDescription =    "The byte count is too small.");
fAddWindowsDefine("RPC_NT_BAD_STUB_DATA",
  sDescription =    "The stub received bad data.");
fAddWindowsDefine("RPC_NT_INVALID_ES_ACTION",
  sDescription =    "Invalid operation on the encoding/decoding handle.");
fAddWindowsDefine("RPC_NT_WRONG_ES_VERSION",
  sDescription =    "Incompatible version of the serializing package.");
fAddWindowsDefine("RPC_NT_WRONG_STUB_VERSION",
  sDescription =    "Incompatible version of the RPC stub.");
fAddWindowsDefine("RPC_NT_INVALID_PIPE_OBJECT",
  sDescription =    "The RPC pipe object is invalid or corrupt.");
fAddWindowsDefine("RPC_NT_INVALID_PIPE_OPERATION",
  sDescription =    "An invalid operation was attempted on an RPC pipe object.");
fAddWindowsDefine("RPC_NT_WRONG_PIPE_VERSION",
  sDescription =    "Unsupported RPC pipe version.");
fAddWindowsDefine("RPC_NT_PIPE_CLOSED",
  sDescription =    "The RPC pipe object has already been closed.");
fAddWindowsDefine("RPC_NT_PIPE_DISCIPLINE_ERROR",
  sDescription =    "The RPC call completed before all pipes were processed.");
fAddWindowsDefine("RPC_NT_PIPE_EMPTY",
  sDescription =    "No more data is available from the RPC pipe.");
fAddWindowsDefine("STATUS_PNP_BAD_MPS_TABLE",
  sDescription =    "A device is missing in the system BIOS MPS table. This device will not be used. Contact your system vendor for a system BIOS update.");
fAddWindowsDefine("STATUS_PNP_TRANSLATION_FAILED",
  sDescription =    "A translator failed to translate resources.");
fAddWindowsDefine("STATUS_PNP_IRQ_TRANSLATION_FAILED",
  sDescription =    "An IRQ translator failed to translate resources.");
fAddWindowsDefine("STATUS_PNP_INVALID_ID",
  sDescription =    "Driver %2 returned an invalid ID for a child device (%3).");
fAddWindowsDefine("STATUS_IO_REISSUE_AS_CACHED",
  sDescription =    "Reissue the given operation as a cached I/O operation");
fAddWindowsDefine("STATUS_CTX_WINSTATION_NAME_INVALID",
  sDescription =    "Session name %1 is invalid.");
fAddWindowsDefine("STATUS_CTX_INVALID_PD",
  sDescription =    "The protocol driver %1 is invalid.");
fAddWindowsDefine("STATUS_CTX_PD_NOT_FOUND",
  sDescription =    "The protocol driver %1 was not found in the system path.");
fAddWindowsDefine("STATUS_CTX_CLOSE_PENDING",
  sDescription =    "A close operation is pending on the terminal connection.");
fAddWindowsDefine("STATUS_CTX_NO_OUTBUF",
  sDescription =    "No free output buffers are available.");
fAddWindowsDefine("STATUS_CTX_MODEM_INF_NOT_FOUND",
  sDescription =    "The MODEM.INF file was not found.");
fAddWindowsDefine("STATUS_CTX_INVALID_MODEMNAME",
  sDescription =    "The modem (%1) was not found in the MODEM.INF file.");
fAddWindowsDefine("STATUS_CTX_RESPONSE_ERROR",
  sDescription =    "The modem did not accept the command sent to it. Verify that the configured modem name matches the attached modem.");
fAddWindowsDefine("STATUS_CTX_MODEM_RESPONSE_TIMEOUT",
  sDescription =    "The modem did not respond to the command sent to it. Verify that the modem cable is properly attached and the modem is turned on.");
fAddWindowsDefine("STATUS_CTX_MODEM_RESPONSE_NO_CARRIER",
  sDescription =    "Carrier detection has failed or the carrier has been dropped due to disconnection.");
fAddWindowsDefine("STATUS_CTX_MODEM_RESPONSE_NO_DIALTONE",
  sDescription =    "A dial tone was not detected within the required time. Verify that the phone cable is properly attached and functional.");
fAddWindowsDefine("STATUS_CTX_MODEM_RESPONSE_BUSY",
  sDescription =    "A busy signal was detected at a remote site on callback.");
fAddWindowsDefine("STATUS_CTX_MODEM_RESPONSE_VOICE",
  sDescription =    "A voice was detected at a remote site on callback.");
fAddWindowsDefine("STATUS_CTX_TD_ERROR",
  sDescription =    "Transport driver error.");
fAddWindowsDefine("STATUS_CTX_LICENSE_CLIENT_INVALID",
  sDescription =    "The client you are using is not licensed to use this system. Your logon request is denied.");
fAddWindowsDefine("STATUS_CTX_LICENSE_NOT_AVAILABLE",
  sDescription =    "The system has reached its licensed logon limit. Try again later.");
fAddWindowsDefine("STATUS_CTX_LICENSE_EXPIRED",
  sDescription =    "The system license has expired. Your logon request is denied.");
fAddWindowsDefine("STATUS_CTX_WINSTATION_NOT_FOUND",
  sDescription =    "The specified session cannot be found.");
fAddWindowsDefine("STATUS_CTX_WINSTATION_NAME_COLLISION",
  sDescription =    "The specified session name is already in use.");
fAddWindowsDefine("STATUS_CTX_WINSTATION_BUSY",
  sDescription =    "The requested operation cannot be completed because the terminal connection is currently processing a connect, disconnect, reset, or delete operation.");
fAddWindowsDefine("STATUS_CTX_BAD_VIDEO_MODE",
  sDescription =    "An attempt has been made to connect to a session whose video mode is not supported by the current client.");
fAddWindowsDefine("STATUS_CTX_GRAPHICS_INVALID",
  sDescription =    "The application attempted to enable DOS graphics mode. DOS graphics mode is not supported.");
fAddWindowsDefine("STATUS_CTX_NOT_CONSOLE",
  sDescription =    "The requested operation can be performed only on the system console. This is most often the result of a driver or system DLL requiring direct console access.");
fAddWindowsDefine("STATUS_CTX_CLIENT_QUERY_TIMEOUT",
  sDescription =    "The client failed to respond to the server connect message.");
fAddWindowsDefine("STATUS_CTX_CONSOLE_DISCONNECT",
  sDescription =    "Disconnecting the console session is not supported.");
fAddWindowsDefine("STATUS_CTX_CONSOLE_CONNECT",
  sDescription =    "Reconnecting a disconnected session to the console is not supported.");
fAddWindowsDefine("STATUS_CTX_SHADOW_DENIED",
  sDescription =    "The request to control another session remotely was denied.");
fAddWindowsDefine("STATUS_CTX_WINSTATION_ACCESS_DENIED",
  sDescription =    "A process has requested access to a session, but has not been granted those access rights.");
fAddWindowsDefine("STATUS_CTX_INVALID_WD",
  sDescription =    "The terminal connection driver %1 is invalid.");
fAddWindowsDefine("STATUS_CTX_WD_NOT_FOUND",
  sDescription =    "The terminal connection driver %1 was not found in the system path.");
fAddWindowsDefine("STATUS_CTX_SHADOW_INVALID",
  sDescription =    "The requested session cannot be controlled remotely. You cannot control your own session, a session that is trying to control your session, a session that has no user logged on, or other sessions from the console.");
fAddWindowsDefine("STATUS_CTX_SHADOW_DISABLED",
  sDescription =    "The requested session is not configured to allow remote control.");
fAddWindowsDefine("STATUS_RDP_PROTOCOL_ERROR",
  sDescription =    "The RDP protocol component %2 detected an error in the protocol stream and has disconnected the client.");
fAddWindowsDefine("STATUS_CTX_CLIENT_LICENSE_NOT_SET",
  sDescription =    "Your request to connect to this terminal server has been rejected. Your terminal server client license number has not been entered for this copy of the terminal client. Contact your system administrator for help in entering a valid, unique license number for this terminal server client. Click OK to continue.");
fAddWindowsDefine("STATUS_CTX_CLIENT_LICENSE_IN_USE",
  sDescription =    "Your request to connect to this terminal server has been rejected. Your terminal server client license number is currently being used by another user. Contact your system administrator to obtain a new copy of the terminal server client with a valid, unique license number. Click OK to continue.");
fAddWindowsDefine("STATUS_CTX_SHADOW_ENDED_BY_MODE_CHANGE",
  sDescription =    "The remote control of the console was terminated because the display mode was changed. Changing the display mode in a remote control session is not supported.");
fAddWindowsDefine("STATUS_CTX_SHADOW_NOT_RUNNING",
  sDescription =    "Remote control could not be terminated because the specified session is not currently being remotely controlled.");
fAddWindowsDefine("STATUS_CTX_LOGON_DISABLED",
  sDescription =    "Your interactive logon privilege has been disabled. Contact your system administrator.");
fAddWindowsDefine("STATUS_CTX_SECURITY_LAYER_ERROR",
  sDescription =    "The terminal server security layer detected an error in the protocol stream and has disconnected the client.");
fAddWindowsDefine("STATUS_TS_INCOMPATIBLE_SESSIONS",
  sDescription =    "The target session is incompatible with the current session.");
fAddWindowsDefine("STATUS_MUI_FILE_NOT_FOUND",
  sDescription =    "The resource loader failed to find an MUI file.");
fAddWindowsDefine("STATUS_MUI_INVALID_FILE",
  sDescription =    "The resource loader failed to load an MUI file because the file failed to pass validation.");
fAddWindowsDefine("STATUS_MUI_INVALID_RC_CONFIG",
  sDescription =    "The RC manifest is corrupted with garbage data, is an unsupported version, or is missing a required item.");
fAddWindowsDefine("STATUS_MUI_INVALID_LOCALE_NAME",
  sDescription =    "The RC manifest has an invalid culture name.");
fAddWindowsDefine("STATUS_MUI_INVALID_ULTIMATEFALLBACK_NAME",
  sDescription =    "The RC manifest has and invalid ultimate fallback name.");
fAddWindowsDefine("STATUS_MUI_FILE_NOT_LOADED",
  sDescription =    "The resource loader cache does not have a loaded MUI entry.");
fAddWindowsDefine("STATUS_RESOURCE_ENUM_USER_STOP",
  sDescription =    "The user stopped resource enumeration.");
fAddWindowsDefine("STATUS_CLUSTER_INVALID_NODE",
  sDescription =    "The cluster node is not valid.");
fAddWindowsDefine("STATUS_CLUSTER_NODE_EXISTS",
  sDescription =    "The cluster node already exists.");
fAddWindowsDefine("STATUS_CLUSTER_JOIN_IN_PROGRESS",
  sDescription =    "A node is in the process of joining the cluster.");
fAddWindowsDefine("STATUS_CLUSTER_NODE_NOT_FOUND",
  sDescription =    "The cluster node was not found.");
fAddWindowsDefine("STATUS_CLUSTER_LOCAL_NODE_NOT_FOUND",
  sDescription =    "The cluster local node information was not found.");
fAddWindowsDefine("STATUS_CLUSTER_NETWORK_EXISTS",
  sDescription =    "The cluster network already exists.");
fAddWindowsDefine("STATUS_CLUSTER_NETWORK_NOT_FOUND",
  sDescription =    "The cluster network was not found.");
fAddWindowsDefine("STATUS_CLUSTER_NETINTERFACE_EXISTS",
  sDescription =    "The cluster network interface already exists.");
fAddWindowsDefine("STATUS_CLUSTER_NETINTERFACE_NOT_FOUND",
  sDescription =    "The cluster network interface was not found.");
fAddWindowsDefine("STATUS_CLUSTER_INVALID_REQUEST",
  sDescription =    "The cluster request is not valid for this object.");
fAddWindowsDefine("STATUS_CLUSTER_INVALID_NETWORK_PROVIDER",
  sDescription =    "The cluster network provider is not valid.");
fAddWindowsDefine("STATUS_CLUSTER_NODE_DOWN",
  sDescription =    "The cluster node is down.");
fAddWindowsDefine("STATUS_CLUSTER_NODE_UNREACHABLE",
  sDescription =    "The cluster node is not reachable.");
fAddWindowsDefine("STATUS_CLUSTER_NODE_NOT_MEMBER",
  sDescription =    "The cluster node is not a member of the cluster.");
fAddWindowsDefine("STATUS_CLUSTER_JOIN_NOT_IN_PROGRESS",
  sDescription =    "A cluster join operation is not in progress.");
fAddWindowsDefine("STATUS_CLUSTER_INVALID_NETWORK",
  sDescription =    "The cluster network is not valid.");
fAddWindowsDefine("STATUS_CLUSTER_NO_NET_ADAPTERS",
  sDescription =    "No network adapters are available.");
fAddWindowsDefine("STATUS_CLUSTER_NODE_UP",
  sDescription =    "The cluster node is up.");
fAddWindowsDefine("STATUS_CLUSTER_NODE_PAUSED",
  sDescription =    "The cluster node is paused.");
fAddWindowsDefine("STATUS_CLUSTER_NODE_NOT_PAUSED",
  sDescription =    "The cluster node is not paused.");
fAddWindowsDefine("STATUS_CLUSTER_NO_SECURITY_CONTEXT",
  sDescription =    "No cluster security context is available.");
fAddWindowsDefine("STATUS_CLUSTER_NETWORK_NOT_INTERNAL",
  sDescription =    "The cluster network is not configured for internal cluster communication.");
fAddWindowsDefine("STATUS_CLUSTER_POISONED",
  sDescription =    "The cluster node has been poisoned.");
fAddWindowsDefine("STATUS_ACPI_INVALID_OPCODE",
  sDescription =    "An attempt was made to run an invalid AML opcode.");
fAddWindowsDefine("STATUS_ACPI_STACK_OVERFLOW",
  sDescription =    "The AML interpreter stack has overflowed.");
fAddWindowsDefine("STATUS_ACPI_ASSERT_FAILED",
  sDescription =    "An inconsistent state has occurred.");
fAddWindowsDefine("STATUS_ACPI_INVALID_INDEX",
  sDescription =    "An attempt was made to access an array outside its bounds.");
fAddWindowsDefine("STATUS_ACPI_INVALID_ARGUMENT",
  sDescription =    "A required argument was not specified.");
fAddWindowsDefine("STATUS_ACPI_FATAL",
  sDescription =    "A fatal error has occurred.");
fAddWindowsDefine("STATUS_ACPI_INVALID_SUPERNAME",
  sDescription =    "An invalid SuperName was specified.");
fAddWindowsDefine("STATUS_ACPI_INVALID_ARGTYPE",
  sDescription =    "An argument with an incorrect type was specified.");
fAddWindowsDefine("STATUS_ACPI_INVALID_OBJTYPE",
  sDescription =    "An object with an incorrect type was specified.");
fAddWindowsDefine("STATUS_ACPI_INVALID_TARGETTYPE",
  sDescription =    "A target with an incorrect type was specified.");
fAddWindowsDefine("STATUS_ACPI_INCORRECT_ARGUMENT_COUNT",
  sDescription =    "An incorrect number of arguments was specified.");
fAddWindowsDefine("STATUS_ACPI_ADDRESS_NOT_MAPPED",
  sDescription =    "An address failed to translate.");
fAddWindowsDefine("STATUS_ACPI_INVALID_EVENTTYPE",
  sDescription =    "An incorrect event type was specified.");
fAddWindowsDefine("STATUS_ACPI_HANDLER_COLLISION",
  sDescription =    "A handler for the target already exists.");
fAddWindowsDefine("STATUS_ACPI_INVALID_DATA",
  sDescription =    "Invalid data for the target was specified.");
fAddWindowsDefine("STATUS_ACPI_INVALID_REGION",
  sDescription =    "An invalid region for the target was specified.");
fAddWindowsDefine("STATUS_ACPI_INVALID_ACCESS_SIZE",
  sDescription =    "An attempt was made to access a field outside the defined range.");
fAddWindowsDefine("STATUS_ACPI_ACQUIRE_GLOBAL_LOCK",
  sDescription =    "The global system lock could not be acquired.");
fAddWindowsDefine("STATUS_ACPI_ALREADY_INITIALIZED",
  sDescription =    "An attempt was made to reinitialize the ACPI subsystem.");
fAddWindowsDefine("STATUS_ACPI_NOT_INITIALIZED",
  sDescription =    "The ACPI subsystem has not been initialized.");
fAddWindowsDefine("STATUS_ACPI_INVALID_MUTEX_LEVEL",
  sDescription =    "An incorrect mutex was specified.");
fAddWindowsDefine("STATUS_ACPI_MUTEX_NOT_OWNED",
  sDescription =    "The mutex is not currently owned.");
fAddWindowsDefine("STATUS_ACPI_MUTEX_NOT_OWNER",
  sDescription =    "An attempt was made to access the mutex by a process that was not the owner.");
fAddWindowsDefine("STATUS_ACPI_RS_ACCESS",
  sDescription =    "An error occurred during an access to region space.");
fAddWindowsDefine("STATUS_ACPI_INVALID_TABLE",
  sDescription =    "An attempt was made to use an incorrect table.");
fAddWindowsDefine("STATUS_ACPI_REG_HANDLER_FAILED",
  sDescription =    "The registration of an ACPI event failed.");
fAddWindowsDefine("STATUS_ACPI_POWER_REQUEST_FAILED",
  sDescription =    "An ACPI power object failed to transition state.");
fAddWindowsDefine("STATUS_SXS_SECTION_NOT_FOUND",
  sDescription =    "The requested section is not present in the activation context.");
fAddWindowsDefine("STATUS_SXS_CANT_GEN_ACTCTX",
  sDescription =    "Windows was unble to process the application binding information. Refer to the system event log for further information.");
fAddWindowsDefine("STATUS_SXS_INVALID_ACTCTXDATA_FORMAT",
  sDescription =    "The application binding data format is invalid.");
fAddWindowsDefine("STATUS_SXS_ASSEMBLY_NOT_FOUND",
  sDescription =    "The referenced assembly is not installed on the system.");
fAddWindowsDefine("STATUS_SXS_MANIFEST_FORMAT_ERROR",
  sDescription =    "The manifest file does not begin with the required tag and format information.");
fAddWindowsDefine("STATUS_SXS_MANIFEST_PARSE_ERROR",
  sDescription =    "The manifest file contains one or more syntax errors.");
fAddWindowsDefine("STATUS_SXS_ACTIVATION_CONTEXT_DISABLED",
  sDescription =    "The application attempted to activate a disabled activation context.");
fAddWindowsDefine("STATUS_SXS_KEY_NOT_FOUND",
  sDescription =    "The requested lookup key was not found in any active activation context.");
fAddWindowsDefine("STATUS_SXS_VERSION_CONFLICT",
  sDescription =    "A component version required by the application conflicts with another component version that is already active.");
fAddWindowsDefine("STATUS_SXS_WRONG_SECTION_TYPE",
  sDescription =    "The type requested activation context section does not match the query API used.");
fAddWindowsDefine("STATUS_SXS_THREAD_QUERIES_DISABLED",
  sDescription =    "Lack of system resources has required isolated activation to be disabled for the current thread of execution.");
fAddWindowsDefine("STATUS_SXS_ASSEMBLY_MISSING",
  sDescription =    "The referenced assembly could not be found.");
fAddWindowsDefine("STATUS_SXS_PROCESS_DEFAULT_ALREADY_SET",
  sDescription =    "An attempt to set the process default activation context failed because the process default activation context was already set.");
fAddWindowsDefine("STATUS_SXS_EARLY_DEACTIVATION",
  sDescription =    "The activation context being deactivated is not the most recently activated one.");
fAddWindowsDefine("STATUS_SXS_INVALID_DEACTIVATION",
  sDescription =    "The activation context being deactivated is not active for the current thread of execution.");
fAddWindowsDefine("STATUS_SXS_MULTIPLE_DEACTIVATION",
  sDescription =    "The activation context being deactivated has already been deactivated.");
fAddWindowsDefine("STATUS_SXS_SYSTEM_DEFAULT_ACTIVATION_CONTEXT_EMPTY",
  sDescription =    "The activation context of the system default assembly could not be generated.");
fAddWindowsDefine("STATUS_SXS_PROCESS_TERMINATION_REQUESTED",
  sDescription =    "A component used by the isolation facility has requested that the process be terminated.");
fAddWindowsDefine("STATUS_SXS_CORRUPT_ACTIVATION_STACK",
  sDescription =    "The activation context activation stack for the running thread of execution is corrupt.");
fAddWindowsDefine("STATUS_SXS_CORRUPTION",
  sDescription =    "The application isolation metadata for this process or thread has become corrupt.");
fAddWindowsDefine("STATUS_SXS_INVALID_IDENTITY_ATTRIBUTE_VALUE",
  sDescription =    "The value of an attribute in an identity is not within the legal range.");
fAddWindowsDefine("STATUS_SXS_INVALID_IDENTITY_ATTRIBUTE_NAME",
  sDescription =    "The name of an attribute in an identity is not within the legal range.");
fAddWindowsDefine("STATUS_SXS_IDENTITY_DUPLICATE_ATTRIBUTE",
  sDescription =    "An identity contains two definitions for the same attribute.");
fAddWindowsDefine("STATUS_SXS_IDENTITY_PARSE_ERROR",
  sDescription =    "The identity string is malformed. This might be due to a trailing comma, more than two unnamed attributes, a missing attribute name, or a missing attribute value.");
fAddWindowsDefine("STATUS_SXS_COMPONENT_STORE_CORRUPT",
  sDescription =    "The component store has become corrupted.");
fAddWindowsDefine("STATUS_SXS_FILE_HASH_MISMATCH",
  sDescription =    "A component's file does not match the verification information present in the component manifest.");
fAddWindowsDefine("STATUS_SXS_MANIFEST_IDENTITY_SAME_BUT_CONTENTS_DIFFERENT",
  sDescription =    "The identities of the manifests are identical, but their contents are different.");
fAddWindowsDefine("STATUS_SXS_IDENTITIES_DIFFERENT",
  sDescription =    "The component identities are different.");
fAddWindowsDefine("STATUS_SXS_ASSEMBLY_IS_NOT_A_DEPLOYMENT",
  sDescription =    "The assembly is not a deployment.");
fAddWindowsDefine("STATUS_SXS_FILE_NOT_PART_OF_ASSEMBLY",
  sDescription =    "The file is not a part of the assembly.");
fAddWindowsDefine("STATUS_ADVANCED_INSTALLER_FAILED",
  sDescription =    "An advanced installer failed during setup or servicing.");
fAddWindowsDefine("STATUS_XML_ENCODING_MISMATCH",
  sDescription =    "The character encoding in the XML declaration did not match the encoding used in the document.");
fAddWindowsDefine("STATUS_SXS_MANIFEST_TOO_BIG",
  sDescription =    "The size of the manifest exceeds the maximum allowed.");
fAddWindowsDefine("STATUS_SXS_SETTING_NOT_REGISTERED",
  sDescription =    "The setting is not registered.");
fAddWindowsDefine("STATUS_SXS_TRANSACTION_CLOSURE_INCOMPLETE",
  sDescription =    "One or more required transaction members are not present.");
fAddWindowsDefine("STATUS_SMI_PRIMITIVE_INSTALLER_FAILED",
  sDescription =    "The SMI primitive installer failed during setup or servicing.");
fAddWindowsDefine("STATUS_GENERIC_COMMAND_FAILED",
  sDescription =    "A generic command executable returned a result that indicates failure.");
fAddWindowsDefine("STATUS_SXS_FILE_HASH_MISSING",
  sDescription =    "A component is missing file verification information in its manifest.");
fAddWindowsDefine("STATUS_TRANSACTIONAL_CONFLICT",
  sDescription =    "The function attempted to use a name that is reserved for use by another transaction.");
fAddWindowsDefine("STATUS_INVALID_TRANSACTION",
  sDescription =    "The transaction handle associated with this operation is invalid.");
fAddWindowsDefine("STATUS_TRANSACTION_NOT_ACTIVE",
  sDescription =    "The requested operation was made in the context of a transaction that is no longer active.");
fAddWindowsDefine("STATUS_TM_INITIALIZATION_FAILED",
  sDescription =    "The transaction manager was unable to be successfully initialized. Transacted operations are not supported.");
fAddWindowsDefine("STATUS_RM_NOT_ACTIVE",
  sDescription =    "Transaction support within the specified file system resource manager was not started or was shut down due to an error.");
fAddWindowsDefine("STATUS_RM_METADATA_CORRUPT",
  sDescription =    "The metadata of the resource manager has been corrupted. The resource manager will not function.");
fAddWindowsDefine("STATUS_TRANSACTION_NOT_JOINED",
  sDescription =    "The resource manager attempted to prepare a transaction that it has not successfully joined.");
fAddWindowsDefine("STATUS_DIRECTORY_NOT_RM",
  sDescription =    "The specified directory does not contain a file system resource manager.");
fAddWindowsDefine("STATUS_TRANSACTIONS_UNSUPPORTED_REMOTE",
  sDescription =    "The remote server or share does not support transacted file operations.");
fAddWindowsDefine("STATUS_LOG_RESIZE_INVALID_SIZE",
  sDescription =    "The requested log size for the file system resource manager is invalid.");
fAddWindowsDefine("STATUS_REMOTE_FILE_VERSION_MISMATCH",
  sDescription =    "The remote server sent mismatching version number or Fid for a file opened with transactions.");
fAddWindowsDefine("STATUS_CRM_PROTOCOL_ALREADY_EXISTS",
  sDescription =    "The resource manager tried to register a protocol that already exists.");
fAddWindowsDefine("STATUS_TRANSACTION_PROPAGATION_FAILED",
  sDescription =    "The attempt to propagate the transaction failed.");
fAddWindowsDefine("STATUS_CRM_PROTOCOL_NOT_FOUND",
  sDescription =    "The requested propagation protocol was not registered as a CRM.");
fAddWindowsDefine("STATUS_TRANSACTION_SUPERIOR_EXISTS",
  sDescription =    "The transaction object already has a superior enlistment, and the caller attempted an operation that would have created a new superior. Only a single superior enlistment is allowed.");
fAddWindowsDefine("STATUS_TRANSACTION_REQUEST_NOT_VALID",
  sDescription =    "The requested operation is not valid on the transaction object in its current state.");
fAddWindowsDefine("STATUS_TRANSACTION_NOT_REQUESTED",
  sDescription =    "The caller has called a response API, but the response is not expected because the transaction manager did not issue the corresponding request to the caller.");
fAddWindowsDefine("STATUS_TRANSACTION_ALREADY_ABORTED",
  sDescription =    "It is too late to perform the requested operation, because the transaction has already been aborted.");
fAddWindowsDefine("STATUS_TRANSACTION_ALREADY_COMMITTED",
  sDescription =    "It is too late to perform the requested operation, because the transaction has already been committed.");
fAddWindowsDefine("STATUS_TRANSACTION_INVALID_MARSHALL_BUFFER",
  sDescription =    "The buffer passed in to NtPushTransaction or NtPullTransaction is not in a valid format.");
fAddWindowsDefine("STATUS_CURRENT_TRANSACTION_NOT_VALID",
  sDescription =    "The current transaction context associated with the thread is not a valid handle to a transaction object.");
fAddWindowsDefine("STATUS_LOG_GROWTH_FAILED",
  sDescription =    "An attempt to create space in the transactional resource manager's log failed. The failure status has been recorded in the event log.");
fAddWindowsDefine("STATUS_OBJECT_NO_LONGER_EXISTS",
  sDescription =    "The object (file, stream, or link) that corresponds to the handle has been deleted by a transaction savepoint rollback.");
fAddWindowsDefine("STATUS_STREAM_MINIVERSION_NOT_FOUND",
  sDescription =    "The specified file miniversion was not found for this transacted file open.");
fAddWindowsDefine("STATUS_STREAM_MINIVERSION_NOT_VALID",
  sDescription =    "The specified file miniversion was found but has been invalidated. The most likely cause is a transaction savepoint rollback.");
fAddWindowsDefine("STATUS_MINIVERSION_INACCESSIBLE_FROM_SPECIFIED_TRANSACTION",
  sDescription =    "A miniversion can be opened only in the context of the transaction that created it.");
fAddWindowsDefine("STATUS_CANT_OPEN_MINIVERSION_WITH_MODIFY_INTENT",
  sDescription =    "It is not possible to open a miniversion with modify access.");
fAddWindowsDefine("STATUS_CANT_CREATE_MORE_STREAM_MINIVERSIONS",
  sDescription =    "It is not possible to create any more miniversions for this stream.");
fAddWindowsDefine("STATUS_HANDLE_NO_LONGER_VALID",
  sDescription =    "The handle has been invalidated by a transaction. The most likely cause is the presence of memory mapping on a file or an open handle when the transaction ended or rolled back to savepoint.");
fAddWindowsDefine("STATUS_LOG_CORRUPTION_DETECTED",
  sDescription =    "The log data is corrupt.");
fAddWindowsDefine("STATUS_RM_DISCONNECTED",
  sDescription =    "The transaction outcome is unavailable because the resource manager responsible for it is disconnected.");
fAddWindowsDefine("STATUS_ENLISTMENT_NOT_SUPERIOR",
  sDescription =    "The request was rejected because the enlistment in question is not a superior enlistment.");
fAddWindowsDefine("STATUS_FILE_IDENTITY_NOT_PERSISTENT",
  sDescription =    "The file cannot be opened in a transaction because its identity depends on the outcome of an unresolved transaction.");
fAddWindowsDefine("STATUS_CANT_BREAK_TRANSACTIONAL_DEPENDENCY",
  sDescription =    "The operation cannot be performed because another transaction is depending on this property not changing.");
fAddWindowsDefine("STATUS_CANT_CROSS_RM_BOUNDARY",
  sDescription =    "The operation would involve a single file with two transactional resource managers and is, therefore, not allowed.");
fAddWindowsDefine("STATUS_TXF_DIR_NOT_EMPTY",
  sDescription =    "The $Txf directory must be empty for this operation to succeed.");
fAddWindowsDefine("STATUS_INDOUBT_TRANSACTIONS_EXIST",
  sDescription =    "The operation would leave a transactional resource manager in an inconsistent state and is therefore not allowed.");
fAddWindowsDefine("STATUS_TM_VOLATILE",
  sDescription =    "The operation could not be completed because the transaction manager does not have a log.");
fAddWindowsDefine("STATUS_ROLLBACK_TIMER_EXPIRED",
  sDescription =    "A rollback could not be scheduled because a previously scheduled rollback has already executed or been queued for execution.");
fAddWindowsDefine("STATUS_TXF_ATTRIBUTE_CORRUPT",
  sDescription =    "The transactional metadata attribute on the file or directory %hs is corrupt and unreadable.");
fAddWindowsDefine("STATUS_EFS_NOT_ALLOWED_IN_TRANSACTION",
  sDescription =    "The encryption operation could not be completed because a transaction is active.");
fAddWindowsDefine("STATUS_TRANSACTIONAL_OPEN_NOT_ALLOWED",
  sDescription =    "This object is not allowed to be opened in a transaction.");
fAddWindowsDefine("STATUS_TRANSACTED_MAPPING_UNSUPPORTED_REMOTE",
  sDescription =    "Memory mapping (creating a mapped section) a remote file under a transaction is not supported.");
fAddWindowsDefine("STATUS_TRANSACTION_REQUIRED_PROMOTION",
  sDescription =    "Promotion was required to allow the resource manager to enlist, but the transaction was set to disallow it.");
fAddWindowsDefine("STATUS_CANNOT_EXECUTE_FILE_IN_TRANSACTION",
  sDescription =    "This file is open for modification in an unresolved transaction and can be opened for execute only by a transacted reader.");
fAddWindowsDefine("STATUS_TRANSACTIONS_NOT_FROZEN",
  sDescription =    "The request to thaw frozen transactions was ignored because transactions were not previously frozen.");
fAddWindowsDefine("STATUS_TRANSACTION_FREEZE_IN_PROGRESS",
  sDescription =    "Transactions cannot be frozen because a freeze is already in progress.");
fAddWindowsDefine("STATUS_NOT_SNAPSHOT_VOLUME",
  sDescription =    "The target volume is not a snapshot volume. This operation is valid only on a volume mounted as a snapshot.");
fAddWindowsDefine("STATUS_NO_SAVEPOINT_WITH_OPEN_FILES",
  sDescription =    "The savepoint operation failed because files are open on the transaction, which is not permitted.");
fAddWindowsDefine("STATUS_SPARSE_NOT_ALLOWED_IN_TRANSACTION",
  sDescription =    "The sparse operation could not be completed because a transaction is active on the file.");
fAddWindowsDefine("STATUS_TM_IDENTITY_MISMATCH",
  sDescription =    "The call to create a transaction manager object failed because the Tm Identity that is stored in the log file does not match the Tm Identity that was passed in as an argument.");
fAddWindowsDefine("STATUS_FLOATED_SECTION",
  sDescription =    "I/O was attempted on a section object that has been floated as a result of a transaction ending. There is no valid data.");
fAddWindowsDefine("STATUS_CANNOT_ACCEPT_TRANSACTED_WORK",
  sDescription =    "The transactional resource manager cannot currently accept transacted work due to a transient condition, such as low resources.");
fAddWindowsDefine("STATUS_CANNOT_ABORT_TRANSACTIONS",
  sDescription =    "The transactional resource manager had too many transactions outstanding that could not be aborted. The transactional resource manager has been shut down.");
fAddWindowsDefine("STATUS_TRANSACTION_NOT_FOUND",
  sDescription =    "The specified transaction was unable to be opened because it was not found.");
fAddWindowsDefine("STATUS_RESOURCEMANAGER_NOT_FOUND",
  sDescription =    "The specified resource manager was unable to be opened because it was not found.");
fAddWindowsDefine("STATUS_ENLISTMENT_NOT_FOUND",
  sDescription =    "The specified enlistment was unable to be opened because it was not found.");
fAddWindowsDefine("STATUS_TRANSACTIONMANAGER_NOT_FOUND",
  sDescription =    "The specified transaction manager was unable to be opened because it was not found.");
fAddWindowsDefine("STATUS_TRANSACTIONMANAGER_NOT_ONLINE",
  sDescription =    "The specified resource manager was unable to create an enlistment because its associated transaction manager is not online.");
fAddWindowsDefine("STATUS_TRANSACTIONMANAGER_RECOVERY_NAME_COLLISION",
  sDescription =    "The specified transaction manager was unable to create the objects contained in its log file in the Ob namespace. Therefore, the transaction manager was unable to recover.");
fAddWindowsDefine("STATUS_TRANSACTION_NOT_ROOT",
  sDescription =    "The call to create a superior enlistment on this transaction object could not be completed because the transaction object specified for the enlistment is a subordinate branch of the transaction. Only the root of the transaction can be enlisted as a superior.");
fAddWindowsDefine("STATUS_TRANSACTION_OBJECT_EXPIRED",
  sDescription =    "Because the associated transaction manager or resource manager has been closed, the handle is no longer valid.");
fAddWindowsDefine("STATUS_COMPRESSION_NOT_ALLOWED_IN_TRANSACTION",
  sDescription =    "The compression operation could not be completed because a transaction is active on the file.");
fAddWindowsDefine("STATUS_TRANSACTION_RESPONSE_NOT_ENLISTED",
  sDescription =    "The specified operation could not be performed on this superior enlistment because the enlistment was not created with the corresponding completion response in the NotificationMask.");
fAddWindowsDefine("STATUS_TRANSACTION_RECORD_TOO_LONG",
  sDescription =    "The specified operation could not be performed because the record to be logged was too long. This can occur because either there are too many enlistments on this transaction or the combined RecoveryInformation being logged on behalf of those enlistments is too long.");
fAddWindowsDefine("STATUS_NO_LINK_TRACKING_IN_TRANSACTION",
  sDescription =    "The link-tracking operation could not be completed because a transaction is active.");
fAddWindowsDefine("STATUS_OPERATION_NOT_SUPPORTED_IN_TRANSACTION",
  sDescription =    "This operation cannot be performed in a transaction.");
fAddWindowsDefine("STATUS_TRANSACTION_INTEGRITY_VIOLATED",
  sDescription =    "The kernel transaction manager had to abort or forget the transaction because it blocked forward progress.");
fAddWindowsDefine("STATUS_EXPIRED_HANDLE",
  sDescription =    "The handle is no longer properly associated with its transaction.  It might have been opened in a transactional resource manager that was subsequently forced to restart.  Please close the handle and open a new one.");
fAddWindowsDefine("STATUS_TRANSACTION_NOT_ENLISTED",
  sDescription =    "The specified operation could not be performed because the resource manager is not enlisted in the transaction.");
fAddWindowsDefine("STATUS_LOG_SECTOR_INVALID",
  sDescription =    "The log service found an invalid log sector.");
fAddWindowsDefine("STATUS_LOG_SECTOR_PARITY_INVALID",
  sDescription =    "The log service encountered a log sector with invalid block parity.");
fAddWindowsDefine("STATUS_LOG_SECTOR_REMAPPED",
  sDescription =    "The log service encountered a remapped log sector.");
fAddWindowsDefine("STATUS_LOG_BLOCK_INCOMPLETE",
  sDescription =    "The log service encountered a partial or incomplete log block.");
fAddWindowsDefine("STATUS_LOG_INVALID_RANGE",
  sDescription =    "The log service encountered an attempt to access data outside the active log range.");
fAddWindowsDefine("STATUS_LOG_BLOCKS_EXHAUSTED",
  sDescription =    "The log service user-log marshaling buffers are exhausted.");
fAddWindowsDefine("STATUS_LOG_READ_CONTEXT_INVALID",
  sDescription =    "The log service encountered an attempt to read from a marshaling area with an invalid read context.");
fAddWindowsDefine("STATUS_LOG_RESTART_INVALID",
  sDescription =    "The log service encountered an invalid log restart area.");
fAddWindowsDefine("STATUS_LOG_BLOCK_VERSION",
  sDescription =    "The log service encountered an invalid log block version.");
fAddWindowsDefine("STATUS_LOG_BLOCK_INVALID",
  sDescription =    "The log service encountered an invalid log block.");
fAddWindowsDefine("STATUS_LOG_READ_MODE_INVALID",
  sDescription =    "The log service encountered an attempt to read the log with an invalid read mode.");
fAddWindowsDefine("STATUS_LOG_METADATA_CORRUPT",
  sDescription =    "The log service encountered a corrupted metadata file.");
fAddWindowsDefine("STATUS_LOG_METADATA_INVALID",
  sDescription =    "The log service encountered a metadata file that could not be created by the log file system.");
fAddWindowsDefine("STATUS_LOG_METADATA_INCONSISTENT",
  sDescription =    "The log service encountered a metadata file with inconsistent data.");
fAddWindowsDefine("STATUS_LOG_RESERVATION_INVALID",
  sDescription =    "The log service encountered an attempt to erroneously allocate or dispose reservation space.");
fAddWindowsDefine("STATUS_LOG_CANT_DELETE",
  sDescription =    "The log service cannot delete the log file or the file system container.");
fAddWindowsDefine("STATUS_LOG_CONTAINER_LIMIT_EXCEEDED",
  sDescription =    "The log service has reached the maximum allowable containers allocated to a log file.");
fAddWindowsDefine("STATUS_LOG_START_OF_LOG",
  sDescription =    "The log service has attempted to read or write backward past the start of the log.");
fAddWindowsDefine("STATUS_LOG_POLICY_ALREADY_INSTALLED",
  sDescription =    "The log policy could not be installed because a policy of the same type is already present.");
fAddWindowsDefine("STATUS_LOG_POLICY_NOT_INSTALLED",
  sDescription =    "The log policy in question was not installed at the time of the request.");
fAddWindowsDefine("STATUS_LOG_POLICY_INVALID",
  sDescription =    "The installed set of policies on the log is invalid.");
fAddWindowsDefine("STATUS_LOG_POLICY_CONFLICT",
  sDescription =    "A policy on the log in question prevented the operation from completing.");
fAddWindowsDefine("STATUS_LOG_PINNED_ARCHIVE_TAIL",
  sDescription =    "The log space cannot be reclaimed because the log is pinned by the archive tail.");
fAddWindowsDefine("STATUS_LOG_RECORD_NONEXISTENT",
  sDescription =    "The log record is not a record in the log file.");
fAddWindowsDefine("STATUS_LOG_RECORDS_RESERVED_INVALID",
  sDescription =    "The number of reserved log records or the adjustment of the number of reserved log records is invalid.");
fAddWindowsDefine("STATUS_LOG_SPACE_RESERVED_INVALID",
  sDescription =    "The reserved log space or the adjustment of the log space is invalid.");
fAddWindowsDefine("STATUS_LOG_TAIL_INVALID",
  sDescription =    "A new or existing archive tail or the base of the active log is invalid.");
fAddWindowsDefine("STATUS_LOG_FULL",
  sDescription =    "The log space is exhausted.");
fAddWindowsDefine("STATUS_LOG_MULTIPLEXED",
  sDescription =    "The log is multiplexed; no direct writes to the physical log are allowed.");
fAddWindowsDefine("STATUS_LOG_DEDICATED",
  sDescription =    "The operation failed because the log is dedicated.");
fAddWindowsDefine("STATUS_LOG_ARCHIVE_NOT_IN_PROGRESS",
  sDescription =    "The operation requires an archive context.");
fAddWindowsDefine("STATUS_LOG_ARCHIVE_IN_PROGRESS",
  sDescription =    "Log archival is in progress.");
fAddWindowsDefine("STATUS_LOG_EPHEMERAL",
  sDescription =    "The operation requires a nonephemeral log, but the log is ephemeral.");
fAddWindowsDefine("STATUS_LOG_NOT_ENOUGH_CONTAINERS",
  sDescription =    "The log must have at least two containers before it can be read from or written to.");
fAddWindowsDefine("STATUS_LOG_CLIENT_ALREADY_REGISTERED",
  sDescription =    "A log client has already registered on the stream.");
fAddWindowsDefine("STATUS_LOG_CLIENT_NOT_REGISTERED",
  sDescription =    "A log client has not been registered on the stream.");
fAddWindowsDefine("STATUS_LOG_FULL_HANDLER_IN_PROGRESS",
  sDescription =    "A request has already been made to handle the log full condition.");
fAddWindowsDefine("STATUS_LOG_CONTAINER_READ_FAILED",
  sDescription =    "The log service encountered an error when attempting to read from a log container.");
fAddWindowsDefine("STATUS_LOG_CONTAINER_WRITE_FAILED",
  sDescription =    "The log service encountered an error when attempting to write to a log container.");
fAddWindowsDefine("STATUS_LOG_CONTAINER_OPEN_FAILED",
  sDescription =    "The log service encountered an error when attempting to open a log container.");
fAddWindowsDefine("STATUS_LOG_CONTAINER_STATE_INVALID",
  sDescription =    "The log service encountered an invalid container state when attempting a requested action.");
fAddWindowsDefine("STATUS_LOG_STATE_INVALID",
  sDescription =    "The log service is not in the correct state to perform a requested action.");
fAddWindowsDefine("STATUS_LOG_PINNED",
  sDescription =    "The log space cannot be reclaimed because the log is pinned.");
fAddWindowsDefine("STATUS_LOG_METADATA_FLUSH_FAILED",
  sDescription =    "The log metadata flush failed.");
fAddWindowsDefine("STATUS_LOG_INCONSISTENT_SECURITY",
  sDescription =    "Security on the log and its containers is inconsistent.");
fAddWindowsDefine("STATUS_LOG_APPENDED_FLUSH_FAILED",
  sDescription =    "Records were appended to the log or reservation changes were made, but the log could not be flushed.");
fAddWindowsDefine("STATUS_LOG_PINNED_RESERVATION",
  sDescription =    "The log is pinned due to reservation consuming most of the log space. Free some reserved records to make space available.");
fAddWindowsDefine("STATUS_VIDEO_HUNG_DISPLAY_DRIVER_THREAD",
  sDescription =    "The %hs display driver has stopped working normally. Save your work and reboot the system to restore full display functionality. The next time you reboot the computer, a dialog box will allow you to upload data about this failure to Microsoft.");
fAddWindowsDefine("STATUS_FLT_NO_HANDLER_DEFINED",
  sDescription =    "A handler was not defined by the filter for this operation.");
fAddWindowsDefine("STATUS_FLT_CONTEXT_ALREADY_DEFINED",
  sDescription =    "A context is already defined for this object.");
fAddWindowsDefine("STATUS_FLT_INVALID_ASYNCHRONOUS_REQUEST",
  sDescription =    "Asynchronous requests are not valid for this operation.");
fAddWindowsDefine("STATUS_FLT_DISALLOW_FAST_IO",
  sDescription =    "This is an internal error code used by the filter manager to determine if a fast I/O operation should be forced down the input/output request packet (IRP) path. Minifilters should never return this value.");
fAddWindowsDefine("STATUS_FLT_INVALID_NAME_REQUEST",
  sDescription =    "An invalid name request was made. The name requested cannot be retrieved at this time.");
fAddWindowsDefine("STATUS_FLT_NOT_SAFE_TO_POST_OPERATION",
  sDescription =    "Posting this operation to a worker thread for further processing is not safe at this time because it could lead to a system deadlock.");
fAddWindowsDefine("STATUS_FLT_NOT_INITIALIZED",
  sDescription =    "The Filter Manager was not initialized when a filter tried to register. Make sure that the Filter Manager is loaded as a driver.");
fAddWindowsDefine("STATUS_FLT_FILTER_NOT_READY",
  sDescription =    "The filter is not ready for attachment to volumes because it has not finished initializing (FltStartFiltering has not been called).");
fAddWindowsDefine("STATUS_FLT_POST_OPERATION_CLEANUP",
  sDescription =    "The filter must clean up any operation-specific context at this time because it is being removed from the system before the operation is completed by the lower drivers.");
fAddWindowsDefine("STATUS_FLT_INTERNAL_ERROR",
  sDescription =    "The Filter Manager had an internal error from which it cannot recover; therefore, the operation has failed. This is usually the result of a filter returning an invalid value from a pre-operation callback.");
fAddWindowsDefine("STATUS_FLT_DELETING_OBJECT",
  sDescription =    "The object specified for this action is in the process of being deleted; therefore, the action requested cannot be completed at this time.");
fAddWindowsDefine("STATUS_FLT_MUST_BE_NONPAGED_POOL",
  sDescription =    "A nonpaged pool must be used for this type of context.");
fAddWindowsDefine("STATUS_FLT_DUPLICATE_ENTRY",
  sDescription =    "A duplicate handler definition has been provided for an operation.");
fAddWindowsDefine("STATUS_FLT_CBDQ_DISABLED",
  sDescription =    "The callback data queue has been disabled.");
fAddWindowsDefine("STATUS_FLT_DO_NOT_ATTACH",
  sDescription =    "Do not attach the filter to the volume at this time.");
fAddWindowsDefine("STATUS_FLT_DO_NOT_DETACH",
  sDescription =    "Do not detach the filter from the volume at this time.");
fAddWindowsDefine("STATUS_FLT_INSTANCE_ALTITUDE_COLLISION",
  sDescription =    "An instance already exists at this altitude on the volume specified.");
fAddWindowsDefine("STATUS_FLT_INSTANCE_NAME_COLLISION",
  sDescription =    "An instance already exists with this name on the volume specified.");
fAddWindowsDefine("STATUS_FLT_FILTER_NOT_FOUND",
  sDescription =    "The system could not find the filter specified.");
fAddWindowsDefine("STATUS_FLT_VOLUME_NOT_FOUND",
  sDescription =    "The system could not find the volume specified.");
fAddWindowsDefine("STATUS_FLT_INSTANCE_NOT_FOUND",
  sDescription =    "The system could not find the instance specified.");
fAddWindowsDefine("STATUS_FLT_CONTEXT_ALLOCATION_NOT_FOUND",
  sDescription =    "No registered context allocation definition was found for the given request.");
fAddWindowsDefine("STATUS_FLT_INVALID_CONTEXT_REGISTRATION",
  sDescription =    "An invalid parameter was specified during context registration.");
fAddWindowsDefine("STATUS_FLT_NAME_CACHE_MISS",
  sDescription =    "The name requested was not found in the Filter Manager name cache and could not be retrieved from the file system.");
fAddWindowsDefine("STATUS_FLT_NO_DEVICE_OBJECT",
  sDescription =    "The requested device object does not exist for the given volume.");
fAddWindowsDefine("STATUS_FLT_VOLUME_ALREADY_MOUNTED",
  sDescription =    "The specified volume is already mounted.");
fAddWindowsDefine("STATUS_FLT_ALREADY_ENLISTED",
  sDescription =    "The specified transaction context is already enlisted in a transaction.");
fAddWindowsDefine("STATUS_FLT_CONTEXT_ALREADY_LINKED",
  sDescription =    "The specified context is already attached to another object.");
fAddWindowsDefine("STATUS_FLT_NO_WAITER_FOR_REPLY",
  sDescription =    "No waiter is present for the filter's reply to this message.");
fAddWindowsDefine("STATUS_MONITOR_NO_DESCRIPTOR",
  sDescription =    "A monitor descriptor could not be obtained.");
fAddWindowsDefine("STATUS_MONITOR_UNKNOWN_DESCRIPTOR_FORMAT",
  sDescription =    "This release does not support the format of the obtained monitor descriptor.");
fAddWindowsDefine("STATUS_MONITOR_INVALID_DESCRIPTOR_CHECKSUM",
  sDescription =    "The checksum of the obtained monitor descriptor is invalid.");
fAddWindowsDefine("STATUS_MONITOR_INVALID_STANDARD_TIMING_BLOCK",
  sDescription =    "The monitor descriptor contains an invalid standard timing block.");
fAddWindowsDefine("STATUS_MONITOR_WMI_DATABLOCK_REGISTRATION_FAILED",
  sDescription =    "WMI data-block registration failed for one of the MSMonitorClass WMI subclasses.");
fAddWindowsDefine("STATUS_MONITOR_INVALID_SERIAL_NUMBER_MONDSC_BLOCK",
  sDescription =    "The provided monitor descriptor block is either corrupted or does not contain the monitor's detailed serial number.");
fAddWindowsDefine("STATUS_MONITOR_INVALID_USER_FRIENDLY_MONDSC_BLOCK",
  sDescription =    "The provided monitor descriptor block is either corrupted or does not contain the monitor's user-friendly name.");
fAddWindowsDefine("STATUS_MONITOR_NO_MORE_DESCRIPTOR_DATA",
  sDescription =    "There is no monitor descriptor data at the specified (offset or size) region.");
fAddWindowsDefine("STATUS_MONITOR_INVALID_DETAILED_TIMING_BLOCK",
  sDescription =    "The monitor descriptor contains an invalid detailed timing block.");
fAddWindowsDefine("STATUS_MONITOR_INVALID_MANUFACTURE_DATE",
  sDescription =    "Monitor descriptor contains invalid manufacture date.");
fAddWindowsDefine("STATUS_GRAPHICS_NOT_EXCLUSIVE_MODE_OWNER",
  sDescription =    "Exclusive mode ownership is needed to create an unmanaged primary allocation.");
fAddWindowsDefine("STATUS_GRAPHICS_INSUFFICIENT_DMA_BUFFER",
  sDescription =    "The driver needs more DMA buffer space to complete the requested operation.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_DISPLAY_ADAPTER",
  sDescription =    "The specified display adapter handle is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_ADAPTER_WAS_RESET",
  sDescription =    "The specified display adapter and all of its state have been reset.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_DRIVER_MODEL",
  sDescription =    "The driver stack does not match the expected driver model.");
fAddWindowsDefine("STATUS_GRAPHICS_PRESENT_MODE_CHANGED",
  sDescription =    "Present happened but ended up into the changed desktop mode.");
fAddWindowsDefine("STATUS_GRAPHICS_PRESENT_OCCLUDED",
  sDescription =    "Nothing to present due to desktop occlusion.");
fAddWindowsDefine("STATUS_GRAPHICS_PRESENT_DENIED",
  sDescription =    "Not able to present due to denial of desktop access.");
fAddWindowsDefine("STATUS_GRAPHICS_CANNOTCOLORCONVERT",
  sDescription =    "Not able to present with color conversion.");
fAddWindowsDefine("STATUS_GRAPHICS_PRESENT_REDIRECTION_DISABLED",
  sDescription =    "Present redirection is disabled (desktop windowing management subsystem is off).");
fAddWindowsDefine("STATUS_GRAPHICS_PRESENT_UNOCCLUDED",
  sDescription =    "Previous exclusive VidPn source owner has released its ownership");
fAddWindowsDefine("STATUS_GRAPHICS_NO_VIDEO_MEMORY",
  sDescription =    "Not enough video memory is available to complete the operation.");
fAddWindowsDefine("STATUS_GRAPHICS_CANT_LOCK_MEMORY",
  sDescription =    "Could not probe and lock the underlying memory of an allocation.");
fAddWindowsDefine("STATUS_GRAPHICS_ALLOCATION_BUSY",
  sDescription =    "The allocation is currently busy.");
fAddWindowsDefine("STATUS_GRAPHICS_TOO_MANY_REFERENCES",
  sDescription =    "An object being referenced has already reached the maximum reference count and cannot be referenced further.");
fAddWindowsDefine("STATUS_GRAPHICS_TRY_AGAIN_LATER",
  sDescription =    "A problem could not be solved due to an existing condition. Try again later.");
fAddWindowsDefine("STATUS_GRAPHICS_TRY_AGAIN_NOW",
  sDescription =    "A problem could not be solved due to an existing condition. Try again now.");
fAddWindowsDefine("STATUS_GRAPHICS_ALLOCATION_INVALID",
  sDescription =    "The allocation is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_UNSWIZZLING_APERTURE_UNAVAILABLE",
  sDescription =    "No more unswizzling apertures are currently available.");
fAddWindowsDefine("STATUS_GRAPHICS_UNSWIZZLING_APERTURE_UNSUPPORTED",
  sDescription =    "The current allocation cannot be unswizzled by an aperture.");
fAddWindowsDefine("STATUS_GRAPHICS_CANT_EVICT_PINNED_ALLOCATION",
  sDescription =    "The request failed because a pinned allocation cannot be evicted.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_ALLOCATION_USAGE",
  sDescription =    "The allocation cannot be used from its current segment location for the specified operation.");
fAddWindowsDefine("STATUS_GRAPHICS_CANT_RENDER_LOCKED_ALLOCATION",
  sDescription =    "A locked allocation cannot be used in the current command buffer.");
fAddWindowsDefine("STATUS_GRAPHICS_ALLOCATION_CLOSED",
  sDescription =    "The allocation being referenced has been closed permanently.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_ALLOCATION_INSTANCE",
  sDescription =    "An invalid allocation instance is being referenced.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_ALLOCATION_HANDLE",
  sDescription =    "An invalid allocation handle is being referenced.");
fAddWindowsDefine("STATUS_GRAPHICS_WRONG_ALLOCATION_DEVICE",
  sDescription =    "The allocation being referenced does not belong to the current device.");
fAddWindowsDefine("STATUS_GRAPHICS_ALLOCATION_CONTENT_LOST",
  sDescription =    "The specified allocation lost its content.");
fAddWindowsDefine("STATUS_GRAPHICS_GPU_EXCEPTION_ON_DEVICE",
  sDescription =    "A GPU exception was detected on the given device. The device cannot be scheduled.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_VIDPN_TOPOLOGY",
  sDescription =    "The specified VidPN topology is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_VIDPN_TOPOLOGY_NOT_SUPPORTED",
  sDescription =    "The specified VidPN topology is valid but is not supported by this model of the display adapter.");
fAddWindowsDefine("STATUS_GRAPHICS_VIDPN_TOPOLOGY_CURRENTLY_NOT_SUPPORTED",
  sDescription =    "The specified VidPN topology is valid but is not currently supported by the display adapter due to allocation of its resources.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_VIDPN",
  sDescription =    "The specified VidPN handle is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_VIDEO_PRESENT_SOURCE",
  sDescription =    "The specified video present source is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_VIDEO_PRESENT_TARGET",
  sDescription =    "The specified video present target is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_VIDPN_MODALITY_NOT_SUPPORTED",
  sDescription =    "The specified VidPN modality is not supported (for example, at least two of the pinned modes are not co-functional).");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_VIDPN_SOURCEMODESET",
  sDescription =    "The specified VidPN source mode set is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_VIDPN_TARGETMODESET",
  sDescription =    "The specified VidPN target mode set is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_FREQUENCY",
  sDescription =    "The specified video signal frequency is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_ACTIVE_REGION",
  sDescription =    "The specified video signal active region is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_TOTAL_REGION",
  sDescription =    "The specified video signal total region is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_VIDEO_PRESENT_SOURCE_MODE",
  sDescription =    "The specified video present source mode is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_VIDEO_PRESENT_TARGET_MODE",
  sDescription =    "The specified video present target mode is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_PINNED_MODE_MUST_REMAIN_IN_SET",
  sDescription =    "The pinned mode must remain in the set on the VidPN's co-functional modality enumeration.");
fAddWindowsDefine("STATUS_GRAPHICS_PATH_ALREADY_IN_TOPOLOGY",
  sDescription =    "The specified video present path is already in the VidPN's topology.");
fAddWindowsDefine("STATUS_GRAPHICS_MODE_ALREADY_IN_MODESET",
  sDescription =    "The specified mode is already in the mode set.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_VIDEOPRESENTSOURCESET",
  sDescription =    "The specified video present source set is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_VIDEOPRESENTTARGETSET",
  sDescription =    "The specified video present target set is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_SOURCE_ALREADY_IN_SET",
  sDescription =    "The specified video present source is already in the video present source set.");
fAddWindowsDefine("STATUS_GRAPHICS_TARGET_ALREADY_IN_SET",
  sDescription =    "The specified video present target is already in the video present target set.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_VIDPN_PRESENT_PATH",
  sDescription =    "The specified VidPN present path is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_NO_RECOMMENDED_VIDPN_TOPOLOGY",
  sDescription =    "The miniport has no recommendation for augmenting the specified VidPN's topology.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_MONITOR_FREQUENCYRANGESET",
  sDescription =    "The specified monitor frequency range set is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_MONITOR_FREQUENCYRANGE",
  sDescription =    "The specified monitor frequency range is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_FREQUENCYRANGE_NOT_IN_SET",
  sDescription =    "The specified frequency range is not in the specified monitor frequency range set.");
fAddWindowsDefine("STATUS_GRAPHICS_FREQUENCYRANGE_ALREADY_IN_SET",
  sDescription =    "The specified frequency range is already in the specified monitor frequency range set.");
fAddWindowsDefine("STATUS_GRAPHICS_STALE_MODESET",
  sDescription =    "The specified mode set is stale. Reacquire the new mode set.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_MONITOR_SOURCEMODESET",
  sDescription =    "The specified monitor source mode set is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_MONITOR_SOURCE_MODE",
  sDescription =    "The specified monitor source mode is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_NO_RECOMMENDED_FUNCTIONAL_VIDPN",
  sDescription =    "The miniport does not have a recommendation regarding the request to provide a functional VidPN given the current display adapter configuration.");
fAddWindowsDefine("STATUS_GRAPHICS_MODE_ID_MUST_BE_UNIQUE",
  sDescription =    "The ID of the specified mode is being used by another mode in the set.");
fAddWindowsDefine("STATUS_GRAPHICS_EMPTY_ADAPTER_MONITOR_MODE_SUPPORT_INTERSECTION",
  sDescription =    "The system failed to determine a mode that is supported by both the display adapter and the monitor connected to it.");
fAddWindowsDefine("STATUS_GRAPHICS_VIDEO_PRESENT_TARGETS_LESS_THAN_SOURCES",
  sDescription =    "The number of video present targets must be greater than or equal to the number of video present sources.");
fAddWindowsDefine("STATUS_GRAPHICS_PATH_NOT_IN_TOPOLOGY",
  sDescription =    "The specified present path is not in the VidPN's topology.");
fAddWindowsDefine("STATUS_GRAPHICS_ADAPTER_MUST_HAVE_AT_LEAST_ONE_SOURCE",
  sDescription =    "The display adapter must have at least one video present source.");
fAddWindowsDefine("STATUS_GRAPHICS_ADAPTER_MUST_HAVE_AT_LEAST_ONE_TARGET",
  sDescription =    "The display adapter must have at least one video present target.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_MONITORDESCRIPTORSET",
  sDescription =    "The specified monitor descriptor set is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_MONITORDESCRIPTOR",
  sDescription =    "The specified monitor descriptor is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_MONITORDESCRIPTOR_NOT_IN_SET",
  sDescription =    "The specified descriptor is not in the specified monitor descriptor set.");
fAddWindowsDefine("STATUS_GRAPHICS_MONITORDESCRIPTOR_ALREADY_IN_SET",
  sDescription =    "The specified descriptor is already in the specified monitor descriptor set.");
fAddWindowsDefine("STATUS_GRAPHICS_MONITORDESCRIPTOR_ID_MUST_BE_UNIQUE",
  sDescription =    "The ID of the specified monitor descriptor is being used by another descriptor in the set.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_VIDPN_TARGET_SUBSET_TYPE",
  sDescription =    "The specified video present target subset type is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_RESOURCES_NOT_RELATED",
  sDescription =    "Two or more of the specified resources are not related to each other, as defined by the interface semantics.");
fAddWindowsDefine("STATUS_GRAPHICS_SOURCE_ID_MUST_BE_UNIQUE",
  sDescription =    "The ID of the specified video present source is being used by another source in the set.");
fAddWindowsDefine("STATUS_GRAPHICS_TARGET_ID_MUST_BE_UNIQUE",
  sDescription =    "The ID of the specified video present target is being used by another target in the set.");
fAddWindowsDefine("STATUS_GRAPHICS_NO_AVAILABLE_VIDPN_TARGET",
  sDescription =    "The specified VidPN source cannot be used because there is no available VidPN target to connect it to.");
fAddWindowsDefine("STATUS_GRAPHICS_MONITOR_COULD_NOT_BE_ASSOCIATED_WITH_ADAPTER",
  sDescription =    "The newly arrived monitor could not be associated with a display adapter.");
fAddWindowsDefine("STATUS_GRAPHICS_NO_VIDPNMGR",
  sDescription =    "The particular display adapter does not have an associated VidPN manager.");
fAddWindowsDefine("STATUS_GRAPHICS_NO_ACTIVE_VIDPN",
  sDescription =    "The VidPN manager of the particular display adapter does not have an active VidPN.");
fAddWindowsDefine("STATUS_GRAPHICS_STALE_VIDPN_TOPOLOGY",
  sDescription =    "The specified VidPN topology is stale; obtain the new topology.");
fAddWindowsDefine("STATUS_GRAPHICS_MONITOR_NOT_CONNECTED",
  sDescription =    "No monitor is connected on the specified video present target.");
fAddWindowsDefine("STATUS_GRAPHICS_SOURCE_NOT_IN_TOPOLOGY",
  sDescription =    "The specified source is not part of the specified VidPN's topology.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_PRIMARYSURFACE_SIZE",
  sDescription =    "The specified primary surface size is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_VISIBLEREGION_SIZE",
  sDescription =    "The specified visible region size is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_STRIDE",
  sDescription =    "The specified stride is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_PIXELFORMAT",
  sDescription =    "The specified pixel format is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_COLORBASIS",
  sDescription =    "The specified color basis is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_PIXELVALUEACCESSMODE",
  sDescription =    "The specified pixel value access mode is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_TARGET_NOT_IN_TOPOLOGY",
  sDescription =    "The specified target is not part of the specified VidPN's topology.");
fAddWindowsDefine("STATUS_GRAPHICS_NO_DISPLAY_MODE_MANAGEMENT_SUPPORT",
  sDescription =    "Failed to acquire the display mode management interface.");
fAddWindowsDefine("STATUS_GRAPHICS_VIDPN_SOURCE_IN_USE",
  sDescription =    "The specified VidPN source is already owned by a DMM client and cannot be used until that client releases it.");
fAddWindowsDefine("STATUS_GRAPHICS_CANT_ACCESS_ACTIVE_VIDPN",
  sDescription =    "The specified VidPN is active and cannot be accessed.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_PATH_IMPORTANCE_ORDINAL",
  sDescription =    "The specified VidPN's present path importance ordinal is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_PATH_CONTENT_GEOMETRY_TRANSFORMATION",
  sDescription =    "The specified VidPN's present path content geometry transformation is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_PATH_CONTENT_GEOMETRY_TRANSFORMATION_NOT_SUPPORTED",
  sDescription =    "The specified content geometry transformation is not supported on the respective VidPN present path.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_GAMMA_RAMP",
  sDescription =    "The specified gamma ramp is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_GAMMA_RAMP_NOT_SUPPORTED",
  sDescription =    "The specified gamma ramp is not supported on the respective VidPN present path.");
fAddWindowsDefine("STATUS_GRAPHICS_MULTISAMPLING_NOT_SUPPORTED",
  sDescription =    "Multisampling is not supported on the respective VidPN present path.");
fAddWindowsDefine("STATUS_GRAPHICS_MODE_NOT_IN_MODESET",
  sDescription =    "The specified mode is not in the specified mode set.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_VIDPN_TOPOLOGY_RECOMMENDATION_REASON",
  sDescription =    "The specified VidPN topology recommendation reason is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_PATH_CONTENT_TYPE",
  sDescription =    "The specified VidPN present path content type is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_COPYPROTECTION_TYPE",
  sDescription =    "The specified VidPN present path copy protection type is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_UNASSIGNED_MODESET_ALREADY_EXISTS",
  sDescription =    "Only one unassigned mode set can exist at any one time for a particular VidPN source or target.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_SCANLINE_ORDERING",
  sDescription =    "The specified scan line ordering type is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_TOPOLOGY_CHANGES_NOT_ALLOWED",
  sDescription =    "The topology changes are not allowed for the specified VidPN.");
fAddWindowsDefine("STATUS_GRAPHICS_NO_AVAILABLE_IMPORTANCE_ORDINALS",
  sDescription =    "All available importance ordinals are being used in the specified topology.");
fAddWindowsDefine("STATUS_GRAPHICS_INCOMPATIBLE_PRIVATE_FORMAT",
  sDescription =    "The specified primary surface has a different private-format attribute than the current primary surface.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_MODE_PRUNING_ALGORITHM",
  sDescription =    "The specified mode-pruning algorithm is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_MONITOR_CAPABILITY_ORIGIN",
  sDescription =    "The specified monitor-capability origin is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_MONITOR_FREQUENCYRANGE_CONSTRAINT",
  sDescription =    "The specified monitor-frequency range constraint is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_MAX_NUM_PATHS_REACHED",
  sDescription =    "The maximum supported number of present paths has been reached.");
fAddWindowsDefine("STATUS_GRAPHICS_CANCEL_VIDPN_TOPOLOGY_AUGMENTATION",
  sDescription =    "The miniport requested that augmentation be canceled for the specified source of the specified VidPN's topology.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_CLIENT_TYPE",
  sDescription =    "The specified client type was not recognized.");
fAddWindowsDefine("STATUS_GRAPHICS_CLIENTVIDPN_NOT_SET",
  sDescription =    "The client VidPN is not set on this adapter (for example, no user mode-initiated mode changes have taken place on this adapter).");
fAddWindowsDefine("STATUS_GRAPHICS_SPECIFIED_CHILD_ALREADY_CONNECTED",
  sDescription =    "The specified display adapter child device already has an external device connected to it.");
fAddWindowsDefine("STATUS_GRAPHICS_CHILD_DESCRIPTOR_NOT_SUPPORTED",
  sDescription =    "The display adapter child device does not support reporting a descriptor.");
fAddWindowsDefine("STATUS_GRAPHICS_NOT_A_LINKED_ADAPTER",
  sDescription =    "The display adapter is not linked to any other adapters.");
fAddWindowsDefine("STATUS_GRAPHICS_LEADLINK_NOT_ENUMERATED",
  sDescription =    "The lead adapter in a linked configuration was not enumerated yet.");
fAddWindowsDefine("STATUS_GRAPHICS_CHAINLINKS_NOT_ENUMERATED",
  sDescription =    "Some chain adapters in a linked configuration have not yet been enumerated.");
fAddWindowsDefine("STATUS_GRAPHICS_ADAPTER_CHAIN_NOT_READY",
  sDescription =    "The chain of linked adapters is not ready to start because of an unknown failure.");
fAddWindowsDefine("STATUS_GRAPHICS_CHAINLINKS_NOT_STARTED",
  sDescription =    "An attempt was made to start a lead link display adapter when the chain links had not yet started.");
fAddWindowsDefine("STATUS_GRAPHICS_CHAINLINKS_NOT_POWERED_ON",
  sDescription =    "An attempt was made to turn on a lead link display adapter when the chain links were turned off.");
fAddWindowsDefine("STATUS_GRAPHICS_INCONSISTENT_DEVICE_LINK_STATE",
  sDescription =    "The adapter link was found in an inconsistent state. Not all adapters are in an expected PNP/power state.");
fAddWindowsDefine("STATUS_GRAPHICS_NOT_POST_DEVICE_DRIVER",
  sDescription =    "The driver trying to start is not the same as the driver for the posted display adapter.");
fAddWindowsDefine("STATUS_GRAPHICS_ADAPTER_ACCESS_NOT_EXCLUDED",
  sDescription =    "An operation is being attempted that requires the display adapter to be in a quiescent state.");
fAddWindowsDefine("STATUS_GRAPHICS_OPM_NOT_SUPPORTED",
  sDescription =    "The driver does not support OPM.");
fAddWindowsDefine("STATUS_GRAPHICS_COPP_NOT_SUPPORTED",
  sDescription =    "The driver does not support COPP.");
fAddWindowsDefine("STATUS_GRAPHICS_UAB_NOT_SUPPORTED",
  sDescription =    "The driver does not support UAB.");
fAddWindowsDefine("STATUS_GRAPHICS_OPM_INVALID_ENCRYPTED_PARAMETERS",
  sDescription =    "The specified encrypted parameters are invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_OPM_PARAMETER_ARRAY_TOO_SMALL",
  sDescription =    "An array passed to a function cannot hold all of the data that the function wants to put in it.");
fAddWindowsDefine("STATUS_GRAPHICS_OPM_NO_PROTECTED_OUTPUTS_EXIST",
  sDescription =    "The GDI display device passed to this function does not have any active protected outputs.");
fAddWindowsDefine("STATUS_GRAPHICS_PVP_NO_DISPLAY_DEVICE_CORRESPONDS_TO_NAME",
  sDescription =    "The PVP cannot find an actual GDI display device that corresponds to the passed-in GDI display device name.");
fAddWindowsDefine("STATUS_GRAPHICS_PVP_DISPLAY_DEVICE_NOT_ATTACHED_TO_DESKTOP",
  sDescription =    "This function failed because the GDI display device passed to it was not attached to the Windows desktop.");
fAddWindowsDefine("STATUS_GRAPHICS_PVP_MIRRORING_DEVICES_NOT_SUPPORTED",
  sDescription =    "The PVP does not support mirroring display devices because they do not have any protected outputs.");
fAddWindowsDefine("STATUS_GRAPHICS_OPM_INVALID_POINTER",
  sDescription =    "The function failed because an invalid pointer parameter was passed to it. A pointer parameter is invalid if it is null, is not correctly aligned, or it points to an invalid address or a kernel mode address.");
fAddWindowsDefine("STATUS_GRAPHICS_OPM_INTERNAL_ERROR",
  sDescription =    "An internal error caused an operation to fail.");
fAddWindowsDefine("STATUS_GRAPHICS_OPM_INVALID_HANDLE",
  sDescription =    "The function failed because the caller passed in an invalid OPM user-mode handle.");
fAddWindowsDefine("STATUS_GRAPHICS_PVP_NO_MONITORS_CORRESPOND_TO_DISPLAY_DEVICE",
  sDescription =    "This function failed because the GDI device passed to it did not have any monitors associated with it.");
fAddWindowsDefine("STATUS_GRAPHICS_PVP_INVALID_CERTIFICATE_LENGTH",
  sDescription =    "A certificate could not be returned because the certificate buffer passed to the function was too small.");
fAddWindowsDefine("STATUS_GRAPHICS_OPM_SPANNING_MODE_ENABLED",
  sDescription =    "DxgkDdiOpmCreateProtectedOutput() could not create a protected output because the video present yarget is in spanning mode.");
fAddWindowsDefine("STATUS_GRAPHICS_OPM_THEATER_MODE_ENABLED",
  sDescription =    "DxgkDdiOpmCreateProtectedOutput() could not create a protected output because the video present target is in theater mode.");
fAddWindowsDefine("STATUS_GRAPHICS_PVP_HFS_FAILED",
  sDescription =    "The function call failed because the display adapter's hardware functionality scan (HFS) failed to validate the graphics hardware.");
fAddWindowsDefine("STATUS_GRAPHICS_OPM_INVALID_SRM",
  sDescription =    "The HDCP SRM passed to this function did not comply with section 5 of the HDCP 1.1 specification.");
fAddWindowsDefine("STATUS_GRAPHICS_OPM_OUTPUT_DOES_NOT_SUPPORT_HDCP",
  sDescription =    "The protected output cannot enable the HDCP system because it does not support it.");
fAddWindowsDefine("STATUS_GRAPHICS_OPM_OUTPUT_DOES_NOT_SUPPORT_ACP",
  sDescription =    "The protected output cannot enable analog copy protection because it does not support it.");
fAddWindowsDefine("STATUS_GRAPHICS_OPM_OUTPUT_DOES_NOT_SUPPORT_CGMSA",
  sDescription =    "The protected output cannot enable the CGMS-A protection technology because it does not support it.");
fAddWindowsDefine("STATUS_GRAPHICS_OPM_HDCP_SRM_NEVER_SET",
  sDescription =    "DxgkDdiOPMGetInformation() cannot return the version of the SRM being used because the application never successfully passed an SRM to the protected output.");
fAddWindowsDefine("STATUS_GRAPHICS_OPM_RESOLUTION_TOO_HIGH",
  sDescription =    "DxgkDdiOPMConfigureProtectedOutput() cannot enable the specified output protection technology because the output's screen resolution is too high.");
fAddWindowsDefine("STATUS_GRAPHICS_OPM_ALL_HDCP_HARDWARE_ALREADY_IN_USE",
  sDescription =    "DxgkDdiOPMConfigureProtectedOutput() cannot enable HDCP because other physical outputs are using the display adapter's HDCP hardware.");
fAddWindowsDefine("STATUS_GRAPHICS_OPM_PROTECTED_OUTPUT_NO_LONGER_EXISTS",
  sDescription =    "The operating system asynchronously destroyed this OPM-protected output because the operating system state changed. This error typically occurs because the monitor PDO associated with this protected output was removed or stopped, the protected output's session became a nonconsole session, or the protected output's desktop became inactive.");
fAddWindowsDefine("STATUS_GRAPHICS_OPM_SESSION_TYPE_CHANGE_IN_PROGRESS",
  sDescription =    "OPM functions cannot be called when a session is changing its type. Three types of sessions currently exist: console, disconnected, and remote (RDP or ICA).");
fAddWindowsDefine("STATUS_GRAPHICS_OPM_PROTECTED_OUTPUT_DOES_NOT_HAVE_COPP_SEMANTICS",
  sDescription =    "The DxgkDdiOPMGetCOPPCompatibleInformation, DxgkDdiOPMGetInformation, or DxgkDdiOPMConfigureProtectedOutput function failed. This error is returned only if a protected output has OPM semantics. DxgkDdiOPMGetCOPPCompatibleInformation always returns this error if a protected output has OPM semantics. DxgkDdiOPMGetInformation returns this error code if the caller requested COPP-specific information. DxgkDdiOPMConfigureProtectedOutput returns this error when the caller tries to use a COPP-specific command.");
fAddWindowsDefine("STATUS_GRAPHICS_OPM_INVALID_INFORMATION_REQUEST",
  sDescription =    "The DxgkDdiOPMGetInformation and DxgkDdiOPMGetCOPPCompatibleInformation functions return this error code if the passed-in sequence number is not the expected sequence number or the passed-in OMAC value is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_OPM_DRIVER_INTERNAL_ERROR",
  sDescription =    "The function failed because an unexpected error occurred inside a display driver.");
fAddWindowsDefine("STATUS_GRAPHICS_OPM_PROTECTED_OUTPUT_DOES_NOT_HAVE_OPM_SEMANTICS",
  sDescription =    "The DxgkDdiOPMGetCOPPCompatibleInformation, DxgkDdiOPMGetInformation, or DxgkDdiOPMConfigureProtectedOutput function failed. This error is returned only if a protected output has COPP semantics. DxgkDdiOPMGetCOPPCompatibleInformation returns this error code if the caller requested OPM-specific information. DxgkDdiOPMGetInformation always returns this error if a protected output has COPP semantics. DxgkDdiOPMConfigureProtectedOutput returns this error when the caller tries to use an OPM-specific command.");
fAddWindowsDefine("STATUS_GRAPHICS_OPM_SIGNALING_NOT_SUPPORTED",
  sDescription =    "The DxgkDdiOPMGetCOPPCompatibleInformation and DxgkDdiOPMConfigureProtectedOutput functions return this error if the display driver does not support the DXGKMDT_OPM_GET_ACP_AND_CGMSA_SIGNALING and DXGKMDT_OPM_SET_ACP_AND_CGMSA_SIGNALING GUIDs.");
fAddWindowsDefine("STATUS_GRAPHICS_OPM_INVALID_CONFIGURATION_REQUEST",
  sDescription =    "The DxgkDdiOPMConfigureProtectedOutput function returns this error code if the passed-in sequence number is not the expected sequence number or the passed-in OMAC value is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_I2C_NOT_SUPPORTED",
  sDescription =    "The monitor connected to the specified video output does not have an I2C bus.");
fAddWindowsDefine("STATUS_GRAPHICS_I2C_DEVICE_DOES_NOT_EXIST",
  sDescription =    "No device on the I2C bus has the specified address.");
fAddWindowsDefine("STATUS_GRAPHICS_I2C_ERROR_TRANSMITTING_DATA",
  sDescription =    "An error occurred while transmitting data to the device on the I2C bus.");
fAddWindowsDefine("STATUS_GRAPHICS_I2C_ERROR_RECEIVING_DATA",
  sDescription =    "An error occurred while receiving data from the device on the I2C bus.");
fAddWindowsDefine("STATUS_GRAPHICS_DDCCI_VCP_NOT_SUPPORTED",
  sDescription =    "The monitor does not support the specified VCP code.");
fAddWindowsDefine("STATUS_GRAPHICS_DDCCI_INVALID_DATA",
  sDescription =    "The data received from the monitor is invalid.");
fAddWindowsDefine("STATUS_GRAPHICS_DDCCI_MONITOR_RETURNED_INVALID_TIMING_STATUS_BYTE",
  sDescription =    "A function call failed because a monitor returned an invalid timing status byte when the operating system used the DDC/CI get timing report and timing message command to get a timing report from a monitor.");
fAddWindowsDefine("STATUS_GRAPHICS_DDCCI_INVALID_CAPABILITIES_STRING",
  sDescription =    "A monitor returned a DDC/CI capabilities string that did not comply with the ACCESS.bus 3.0, DDC/CI 1.1, or MCCS 2 Revision 1 specification.");
fAddWindowsDefine("STATUS_GRAPHICS_MCA_INTERNAL_ERROR",
  sDescription =    "An internal error caused an operation to fail.");
fAddWindowsDefine("STATUS_GRAPHICS_DDCCI_INVALID_MESSAGE_COMMAND",
  sDescription =    "An operation failed because a DDC/CI message had an invalid value in its command field.");
fAddWindowsDefine("STATUS_GRAPHICS_DDCCI_INVALID_MESSAGE_LENGTH",
  sDescription =    "This error occurred because a DDC/CI message had an invalid value in its length field.");
fAddWindowsDefine("STATUS_GRAPHICS_DDCCI_INVALID_MESSAGE_CHECKSUM",
  sDescription =    "This error occurred because the value in a DDC/CI message's checksum field did not match the message's computed checksum value. This error implies that the data was corrupted while it was being transmitted from a monitor to a computer.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_PHYSICAL_MONITOR_HANDLE",
  sDescription =    "This function failed because an invalid monitor handle was passed to it.");
fAddWindowsDefine("STATUS_GRAPHICS_MONITOR_NO_LONGER_EXISTS",
  sDescription =    "The operating system asynchronously destroyed the monitor that corresponds to this handle because the operating system's state changed. This error typically occurs because the monitor PDO associated with this handle was removed or stopped, or a display mode change occurred. A display mode change occurs when Windows sends a WM_DISPLAYCHANGE message to applications.");
fAddWindowsDefine("STATUS_GRAPHICS_ONLY_CONSOLE_SESSION_SUPPORTED",
  sDescription =    "This function can be used only if a program is running in the local console session. It cannot be used if a program is running on a remote desktop session or on a terminal server session.");
fAddWindowsDefine("STATUS_GRAPHICS_NO_DISPLAY_DEVICE_CORRESPONDS_TO_NAME",
  sDescription =    "This function cannot find an actual GDI display device that corresponds to the specified GDI display device name.");
fAddWindowsDefine("STATUS_GRAPHICS_DISPLAY_DEVICE_NOT_ATTACHED_TO_DESKTOP",
  sDescription =    "The function failed because the specified GDI display device was not attached to the Windows desktop.");
fAddWindowsDefine("STATUS_GRAPHICS_MIRRORING_DEVICES_NOT_SUPPORTED",
  sDescription =    "This function does not support GDI mirroring display devices because GDI mirroring display devices do not have any physical monitors associated with them.");
fAddWindowsDefine("STATUS_GRAPHICS_INVALID_POINTER",
  sDescription =    "The function failed because an invalid pointer parameter was passed to it. A pointer parameter is invalid if it is null, is not correctly aligned, or points to an invalid address or to a kernel mode address.");
fAddWindowsDefine("STATUS_GRAPHICS_NO_MONITORS_CORRESPOND_TO_DISPLAY_DEVICE",
  sDescription =    "This function failed because the GDI device passed to it did not have a monitor associated with it.");
fAddWindowsDefine("STATUS_GRAPHICS_PARAMETER_ARRAY_TOO_SMALL",
  sDescription =    "An array passed to the function cannot hold all of the data that the function must copy into the array.");
fAddWindowsDefine("STATUS_GRAPHICS_INTERNAL_ERROR",
  sDescription =    "An internal error caused an operation to fail.");
fAddWindowsDefine("STATUS_GRAPHICS_SESSION_TYPE_CHANGE_IN_PROGRESS",
  sDescription =    "The function failed because the current session is changing its type. This function cannot be called when the current session is changing its type. Three types of sessions currently exist: console, disconnected, and remote (RDP or ICA).");
fAddWindowsDefine("STATUS_FVE_LOCKED_VOLUME",
  sDescription =    "The volume must be unlocked before it can be used.");
fAddWindowsDefine("STATUS_FVE_NOT_ENCRYPTED",
  sDescription =    "The volume is fully decrypted and no key is available.");
fAddWindowsDefine("STATUS_FVE_BAD_INFORMATION",
  sDescription =    "The control block for the encrypted volume is not valid.");
fAddWindowsDefine("STATUS_FVE_TOO_SMALL",
  sDescription =    "Not enough free space remains on the volume to allow encryption.");
fAddWindowsDefine("STATUS_FVE_FAILED_WRONG_FS",
  sDescription =    "The partition cannot be encrypted because the file system is not supported.");
fAddWindowsDefine("STATUS_FVE_FAILED_BAD_FS",
  sDescription =    "The file system is inconsistent. Run the Check Disk utility.");
fAddWindowsDefine("STATUS_FVE_FS_NOT_EXTENDED",
  sDescription =    "The file system does not extend to the end of the volume.");
fAddWindowsDefine("STATUS_FVE_FS_MOUNTED",
  sDescription =    "This operation cannot be performed while a file system is mounted on the volume.");
fAddWindowsDefine("STATUS_FVE_NO_LICENSE",
  sDescription =    "BitLocker Drive Encryption is not included with this version of Windows.");
fAddWindowsDefine("STATUS_FVE_ACTION_NOT_ALLOWED",
  sDescription =    "The requested action was denied by the FVE control engine.");
fAddWindowsDefine("STATUS_FVE_BAD_DATA",
  sDescription =    "The data supplied is malformed.");
fAddWindowsDefine("STATUS_FVE_VOLUME_NOT_BOUND",
  sDescription =    "The volume is not bound to the system.");
fAddWindowsDefine("STATUS_FVE_NOT_DATA_VOLUME",
  sDescription =    "The volume specified is not a data volume.");
fAddWindowsDefine("STATUS_FVE_CONV_READ_ERROR",
  sDescription =    "A read operation failed while converting the volume.");
fAddWindowsDefine("STATUS_FVE_CONV_WRITE_ERROR",
  sDescription =    "A write operation failed while converting the volume.");
fAddWindowsDefine("STATUS_FVE_OVERLAPPED_UPDATE",
  sDescription =    "The control block for the encrypted volume was updated by another thread. Try again.");
fAddWindowsDefine("STATUS_FVE_FAILED_SECTOR_SIZE",
  sDescription =    "The volume encryption algorithm cannot be used on this sector size.");
fAddWindowsDefine("STATUS_FVE_FAILED_AUTHENTICATION",
  sDescription =    "BitLocker recovery authentication failed.");
fAddWindowsDefine("STATUS_FVE_NOT_OS_VOLUME",
  sDescription =    "The volume specified is not the boot operating system volume.");
fAddWindowsDefine("STATUS_FVE_KEYFILE_NOT_FOUND",
  sDescription =    "The BitLocker startup key or recovery password could not be read from external media.");
fAddWindowsDefine("STATUS_FVE_KEYFILE_INVALID",
  sDescription =    "The BitLocker startup key or recovery password file is corrupt or invalid.");
fAddWindowsDefine("STATUS_FVE_KEYFILE_NO_VMK",
  sDescription =    "The BitLocker encryption key could not be obtained from the startup key or the recovery password.");
fAddWindowsDefine("STATUS_FVE_TPM_DISABLED",
  sDescription =    "The TPM is disabled.");
fAddWindowsDefine("STATUS_FVE_TPM_SRK_AUTH_NOT_ZERO",
  sDescription =    "The authorization data for the SRK of the TPM is not zero.");
fAddWindowsDefine("STATUS_FVE_TPM_INVALID_PCR",
  sDescription =    "The system boot information changed or the TPM locked out access to BitLocker encryption keys until the computer is restarted.");
fAddWindowsDefine("STATUS_FVE_TPM_NO_VMK",
  sDescription =    "The BitLocker encryption key could not be obtained from the TPM.");
fAddWindowsDefine("STATUS_FVE_PIN_INVALID",
  sDescription =    "The BitLocker encryption key could not be obtained from the TPM and PIN.");
fAddWindowsDefine("STATUS_FVE_AUTH_INVALID_APPLICATION",
  sDescription =    "A boot application hash does not match the hash computed when BitLocker was turned on.");
fAddWindowsDefine("STATUS_FVE_AUTH_INVALID_CONFIG",
  sDescription =    "The Boot Configuration Data (BCD) settings are not supported or have changed because BitLocker was enabled.");
fAddWindowsDefine("STATUS_FVE_DEBUGGER_ENABLED",
  sDescription =    "Boot debugging is enabled. Run Windows Boot Configuration Data Store Editor (bcdedit.exe) to turn it off.");
fAddWindowsDefine("STATUS_FVE_DRY_RUN_FAILED",
  sDescription =    "The BitLocker encryption key could not be obtained.");
fAddWindowsDefine("STATUS_FVE_BAD_METADATA_POINTER",
  sDescription =    "The metadata disk region pointer is incorrect.");
fAddWindowsDefine("STATUS_FVE_OLD_METADATA_COPY",
  sDescription =    "The backup copy of the metadata is out of date.");
fAddWindowsDefine("STATUS_FVE_REBOOT_REQUIRED",
  sDescription =    "No action was taken because a system restart is required.");
fAddWindowsDefine("STATUS_FVE_RAW_ACCESS",
  sDescription =    "No action was taken because BitLocker Drive Encryption is in RAW access mode.");
fAddWindowsDefine("STATUS_FVE_RAW_BLOCKED",
  sDescription =    "BitLocker Drive Encryption cannot enter RAW access mode for this volume.");
fAddWindowsDefine("STATUS_FVE_NO_FEATURE_LICENSE",
  sDescription =    "This feature of BitLocker Drive Encryption is not included with this version of Windows.");
fAddWindowsDefine("STATUS_FVE_POLICY_USER_DISABLE_RDV_NOT_ALLOWED",
  sDescription =    "Group policy does not permit turning off BitLocker Drive Encryption on roaming data volumes.");
fAddWindowsDefine("STATUS_FVE_CONV_RECOVERY_FAILED",
  sDescription =    "Bitlocker Drive Encryption failed to recover from aborted conversion. This could be due to either all conversion logs being corrupted or the media being write-protected.");
fAddWindowsDefine("STATUS_FVE_VIRTUALIZED_SPACE_TOO_BIG",
  sDescription =    "The requested virtualization size is too big.");
fAddWindowsDefine("STATUS_FVE_VOLUME_TOO_SMALL",
  sDescription =    "The drive is too small to be protected using BitLocker Drive Encryption.");
fAddWindowsDefine("STATUS_FWP_CALLOUT_NOT_FOUND",
  sDescription =    "The callout does not exist.");
fAddWindowsDefine("STATUS_FWP_CONDITION_NOT_FOUND",
  sDescription =    "The filter condition does not exist.");
fAddWindowsDefine("STATUS_FWP_FILTER_NOT_FOUND",
  sDescription =    "The filter does not exist.");
fAddWindowsDefine("STATUS_FWP_LAYER_NOT_FOUND",
  sDescription =    "The layer does not exist.");
fAddWindowsDefine("STATUS_FWP_PROVIDER_NOT_FOUND",
  sDescription =    "The provider does not exist.");
fAddWindowsDefine("STATUS_FWP_PROVIDER_CONTEXT_NOT_FOUND",
  sDescription =    "The provider context does not exist.");
fAddWindowsDefine("STATUS_FWP_SUBLAYER_NOT_FOUND",
  sDescription =    "The sublayer does not exist.");
fAddWindowsDefine("STATUS_FWP_NOT_FOUND",
  sDescription =    "The object does not exist.");
fAddWindowsDefine("STATUS_FWP_ALREADY_EXISTS",
  sDescription =    "An object with that GUID or LUID already exists.");
fAddWindowsDefine("STATUS_FWP_IN_USE",
  sDescription =    "The object is referenced by other objects and cannot be deleted.");
fAddWindowsDefine("STATUS_FWP_DYNAMIC_SESSION_IN_PROGRESS",
  sDescription =    "The call is not allowed from within a dynamic session.");
fAddWindowsDefine("STATUS_FWP_WRONG_SESSION",
  sDescription =    "The call was made from the wrong session and cannot be completed.");
fAddWindowsDefine("STATUS_FWP_NO_TXN_IN_PROGRESS",
  sDescription =    "The call must be made from within an explicit transaction.");
fAddWindowsDefine("STATUS_FWP_TXN_IN_PROGRESS",
  sDescription =    "The call is not allowed from within an explicit transaction.");
fAddWindowsDefine("STATUS_FWP_TXN_ABORTED",
  sDescription =    "The explicit transaction has been forcibly canceled.");
fAddWindowsDefine("STATUS_FWP_SESSION_ABORTED",
  sDescription =    "The session has been canceled.");
fAddWindowsDefine("STATUS_FWP_INCOMPATIBLE_TXN",
  sDescription =    "The call is not allowed from within a read-only transaction.");
fAddWindowsDefine("STATUS_FWP_TIMEOUT",
  sDescription =    "The call timed out while waiting to acquire the transaction lock.");
fAddWindowsDefine("STATUS_FWP_NET_EVENTS_DISABLED",
  sDescription =    "The collection of network diagnostic events is disabled.");
fAddWindowsDefine("STATUS_FWP_INCOMPATIBLE_LAYER",
  sDescription =    "The operation is not supported by the specified layer.");
fAddWindowsDefine("STATUS_FWP_KM_CLIENTS_ONLY",
  sDescription =    "The call is allowed for kernel-mode callers only.");
fAddWindowsDefine("STATUS_FWP_LIFETIME_MISMATCH",
  sDescription =    "The call tried to associate two objects with incompatible lifetimes.");
fAddWindowsDefine("STATUS_FWP_BUILTIN_OBJECT",
  sDescription =    "The object is built-in and cannot be deleted.");
fAddWindowsDefine("STATUS_FWP_TOO_MANY_BOOTTIME_FILTERS",
  sDescription =    "The maximum number of boot-time filters or callouts has been reached.");
fAddWindowsDefine("STATUS_FWP_TOO_MANY_CALLOUTS",
  sDescription =    "The maximum number of boot-time filters or callouts has been reached.");
fAddWindowsDefine("STATUS_FWP_NOTIFICATION_DROPPED",
  sDescription =    "A notification could not be delivered because a message queue has reached maximum capacity.");
fAddWindowsDefine("STATUS_FWP_TRAFFIC_MISMATCH",
  sDescription =    "The traffic parameters do not match those for the security association context.");
fAddWindowsDefine("STATUS_FWP_INCOMPATIBLE_SA_STATE",
  sDescription =    "The call is not allowed for the current security association state.");
fAddWindowsDefine("STATUS_FWP_NULL_POINTER",
  sDescription =    "A required pointer is null.");
fAddWindowsDefine("STATUS_FWP_INVALID_ENUMERATOR",
  sDescription =    "An enumerator is not valid.");
fAddWindowsDefine("STATUS_FWP_INVALID_FLAGS",
  sDescription =    "The flags field contains an invalid value.");
fAddWindowsDefine("STATUS_FWP_INVALID_NET_MASK",
  sDescription =    "A network mask is not valid.");
fAddWindowsDefine("STATUS_FWP_INVALID_RANGE",
  sDescription =    "An FWP_RANGE is not valid.");
fAddWindowsDefine("STATUS_FWP_INVALID_INTERVAL",
  sDescription =    "The time interval is not valid.");
fAddWindowsDefine("STATUS_FWP_ZERO_LENGTH_ARRAY",
  sDescription =    "An array that must contain at least one element has a zero length.");
fAddWindowsDefine("STATUS_FWP_NULL_DISPLAY_NAME",
  sDescription =    "The displayData.name field cannot be null.");
fAddWindowsDefine("STATUS_FWP_INVALID_ACTION_TYPE",
  sDescription =    "The action type is not one of the allowed action types for a filter.");
fAddWindowsDefine("STATUS_FWP_INVALID_WEIGHT",
  sDescription =    "The filter weight is not valid.");
fAddWindowsDefine("STATUS_FWP_MATCH_TYPE_MISMATCH",
  sDescription =    "A filter condition contains a match type that is not compatible with the operands.");
fAddWindowsDefine("STATUS_FWP_TYPE_MISMATCH",
  sDescription =    "An FWP_VALUE or FWPM_CONDITION_VALUE is of the wrong type.");
fAddWindowsDefine("STATUS_FWP_OUT_OF_BOUNDS",
  sDescription =    "An integer value is outside the allowed range.");
fAddWindowsDefine("STATUS_FWP_RESERVED",
  sDescription =    "A reserved field is nonzero.");
fAddWindowsDefine("STATUS_FWP_DUPLICATE_CONDITION",
  sDescription =    "A filter cannot contain multiple conditions operating on a single field.");
fAddWindowsDefine("STATUS_FWP_DUPLICATE_KEYMOD",
  sDescription =    "A policy cannot contain the same keying module more than once.");
fAddWindowsDefine("STATUS_FWP_ACTION_INCOMPATIBLE_WITH_LAYER",
  sDescription =    "The action type is not compatible with the layer.");
fAddWindowsDefine("STATUS_FWP_ACTION_INCOMPATIBLE_WITH_SUBLAYER",
  sDescription =    "The action type is not compatible with the sublayer.");
fAddWindowsDefine("STATUS_FWP_CONTEXT_INCOMPATIBLE_WITH_LAYER",
  sDescription =    "The raw context or the provider context is not compatible with the layer.");
fAddWindowsDefine("STATUS_FWP_CONTEXT_INCOMPATIBLE_WITH_CALLOUT",
  sDescription =    "The raw context or the provider context is not compatible with the callout.");
fAddWindowsDefine("STATUS_FWP_INCOMPATIBLE_AUTH_METHOD",
  sDescription =    "The authentication method is not compatible with the policy type.");
fAddWindowsDefine("STATUS_FWP_INCOMPATIBLE_DH_GROUP",
  sDescription =    "The Diffie-Hellman group is not compatible with the policy type.");
fAddWindowsDefine("STATUS_FWP_EM_NOT_SUPPORTED",
  sDescription =    "An IKE policy cannot contain an Extended Mode policy.");
fAddWindowsDefine("STATUS_FWP_NEVER_MATCH",
  sDescription =    "The enumeration template or subscription will never match any objects.");
fAddWindowsDefine("STATUS_FWP_PROVIDER_CONTEXT_MISMATCH",
  sDescription =    "The provider context is of the wrong type.");
fAddWindowsDefine("STATUS_FWP_INVALID_PARAMETER",
  sDescription =    "The parameter is incorrect.");
fAddWindowsDefine("STATUS_FWP_TOO_MANY_SUBLAYERS",
  sDescription =    "The maximum number of sublayers has been reached.");
fAddWindowsDefine("STATUS_FWP_CALLOUT_NOTIFICATION_FAILED",
  sDescription =    "The notification function for a callout returned an error.");
fAddWindowsDefine("STATUS_FWP_INCOMPATIBLE_AUTH_CONFIG",
  sDescription =    "The IPsec authentication configuration is not compatible with the authentication type.");
fAddWindowsDefine("STATUS_FWP_INCOMPATIBLE_CIPHER_CONFIG",
  sDescription =    "The IPsec cipher configuration is not compatible with the cipher type.");
fAddWindowsDefine("STATUS_FWP_DUPLICATE_AUTH_METHOD",
  sDescription =    "A policy cannot contain the same auth method more than once.");
fAddWindowsDefine("STATUS_FWP_TCPIP_NOT_READY",
  sDescription =    "The TCP/IP stack is not ready.");
fAddWindowsDefine("STATUS_FWP_INJECT_HANDLE_CLOSING",
  sDescription =    "The injection handle is being closed by another thread.");
fAddWindowsDefine("STATUS_FWP_INJECT_HANDLE_STALE",
  sDescription =    "The injection handle is stale.");
fAddWindowsDefine("STATUS_FWP_CANNOT_PEND",
  sDescription =    "The classify cannot be pended.");
fAddWindowsDefine("STATUS_NDIS_CLOSING",
  sDescription =    "The binding to the network interface is being closed.");
fAddWindowsDefine("STATUS_NDIS_BAD_VERSION",
  sDescription =    "An invalid version was specified.");
fAddWindowsDefine("STATUS_NDIS_BAD_CHARACTERISTICS",
  sDescription =    "An invalid characteristics table was used.");
fAddWindowsDefine("STATUS_NDIS_ADAPTER_NOT_FOUND",
  sDescription =    "Failed to find the network interface or the network interface is not ready.");
fAddWindowsDefine("STATUS_NDIS_OPEN_FAILED",
  sDescription =    "Failed to open the network interface.");
fAddWindowsDefine("STATUS_NDIS_DEVICE_FAILED",
  sDescription =    "The network interface has encountered an internal unrecoverable failure.");
fAddWindowsDefine("STATUS_NDIS_MULTICAST_FULL",
  sDescription =    "The multicast list on the network interface is full.");
fAddWindowsDefine("STATUS_NDIS_MULTICAST_EXISTS",
  sDescription =    "An attempt was made to add a duplicate multicast address to the list.");
fAddWindowsDefine("STATUS_NDIS_MULTICAST_NOT_FOUND",
  sDescription =    "At attempt was made to remove a multicast address that was never added.");
fAddWindowsDefine("STATUS_NDIS_REQUEST_ABORTED",
  sDescription =    "The network interface aborted the request.");
fAddWindowsDefine("STATUS_NDIS_RESET_IN_PROGRESS",
  sDescription =    "The network interface cannot process the request because it is being reset.");
fAddWindowsDefine("STATUS_NDIS_INVALID_PACKET",
  sDescription =    "An attempt was made to send an invalid packet on a network interface.");
fAddWindowsDefine("STATUS_NDIS_INVALID_DEVICE_REQUEST",
  sDescription =    "The specified request is not a valid operation for the target device.");
fAddWindowsDefine("STATUS_NDIS_ADAPTER_NOT_READY",
  sDescription =    "The network interface is not ready to complete this operation.");
fAddWindowsDefine("STATUS_NDIS_INVALID_LENGTH",
  sDescription =    "The length of the buffer submitted for this operation is not valid.");
fAddWindowsDefine("STATUS_NDIS_INVALID_DATA",
  sDescription =    "The data used for this operation is not valid.");
fAddWindowsDefine("STATUS_NDIS_BUFFER_TOO_SHORT",
  sDescription =    "The length of the submitted buffer for this operation is too small.");
fAddWindowsDefine("STATUS_NDIS_INVALID_OID",
  sDescription =    "The network interface does not support this object identifier.");
fAddWindowsDefine("STATUS_NDIS_ADAPTER_REMOVED",
  sDescription =    "The network interface has been removed.");
fAddWindowsDefine("STATUS_NDIS_UNSUPPORTED_MEDIA",
  sDescription =    "The network interface does not support this media type.");
fAddWindowsDefine("STATUS_NDIS_GROUP_ADDRESS_IN_USE",
  sDescription =    "An attempt was made to remove a token ring group address that is in use by other components.");
fAddWindowsDefine("STATUS_NDIS_FILE_NOT_FOUND",
  sDescription =    "An attempt was made to map a file that cannot be found.");
fAddWindowsDefine("STATUS_NDIS_ERROR_READING_FILE",
  sDescription =    "An error occurred while NDIS tried to map the file.");
fAddWindowsDefine("STATUS_NDIS_ALREADY_MAPPED",
  sDescription =    "An attempt was made to map a file that is already mapped.");
fAddWindowsDefine("STATUS_NDIS_RESOURCE_CONFLICT",
  sDescription =    "An attempt to allocate a hardware resource failed because the resource is used by another component.");
fAddWindowsDefine("STATUS_NDIS_MEDIA_DISCONNECTED",
  sDescription =    "The I/O operation failed because the network media is disconnected or the wireless access point is out of range.");
fAddWindowsDefine("STATUS_NDIS_INVALID_ADDRESS",
  sDescription =    "The network address used in the request is invalid.");
fAddWindowsDefine("STATUS_NDIS_PAUSED",
  sDescription =    "The offload operation on the network interface has been paused.");
fAddWindowsDefine("STATUS_NDIS_INTERFACE_NOT_FOUND",
  sDescription =    "The network interface was not found.");
fAddWindowsDefine("STATUS_NDIS_UNSUPPORTED_REVISION",
  sDescription =    "The revision number specified in the structure is not supported.");
fAddWindowsDefine("STATUS_NDIS_INVALID_PORT",
  sDescription =    "The specified port does not exist on this network interface.");
fAddWindowsDefine("STATUS_NDIS_INVALID_PORT_STATE",
  sDescription =    "The current state of the specified port on this network interface does not support the requested operation.");
fAddWindowsDefine("STATUS_NDIS_LOW_POWER_STATE",
  sDescription =    "The miniport adapter is in a lower power state.");
fAddWindowsDefine("STATUS_NDIS_NOT_SUPPORTED",
  sDescription =    "The network interface does not support this request.");
fAddWindowsDefine("STATUS_NDIS_OFFLOAD_POLICY",
  sDescription =    "The TCP connection is not offloadable because of a local policy setting.");
fAddWindowsDefine("STATUS_NDIS_OFFLOAD_CONNECTION_REJECTED",
  sDescription =    "The TCP connection is not offloadable by the Chimney offload target.");
fAddWindowsDefine("STATUS_NDIS_OFFLOAD_PATH_REJECTED",
  sDescription =    "The IP Path object is not in an offloadable state.");
fAddWindowsDefine("STATUS_NDIS_DOT11_AUTO_CONFIG_ENABLED",
  sDescription =    "The wireless LAN interface is in auto-configuration mode and does not support the requested parameter change operation.");
fAddWindowsDefine("STATUS_NDIS_DOT11_MEDIA_IN_USE",
  sDescription =    "The wireless LAN interface is busy and cannot perform the requested operation.");
fAddWindowsDefine("STATUS_NDIS_DOT11_POWER_STATE_INVALID",
  sDescription =    "The wireless LAN interface is power down and does not support the requested operation.");
fAddWindowsDefine("STATUS_NDIS_PM_WOL_PATTERN_LIST_FULL",
  sDescription =    "The list of wake on LAN patterns is full.");
fAddWindowsDefine("STATUS_NDIS_PM_PROTOCOL_OFFLOAD_LIST_FULL",
  sDescription =    "The list of low power protocol offloads is full.");
fAddWindowsDefine("STATUS_IPSEC_BAD_SPI",
  sDescription =    "The SPI in the packet does not match a valid IPsec SA.");
fAddWindowsDefine("STATUS_IPSEC_SA_LIFETIME_EXPIRED",
  sDescription =    "The packet was received on an IPsec SA whose lifetime has expired.");
fAddWindowsDefine("STATUS_IPSEC_WRONG_SA",
  sDescription =    "The packet was received on an IPsec SA that does not match the packet characteristics.");
fAddWindowsDefine("STATUS_IPSEC_REPLAY_CHECK_FAILED",
  sDescription =    "The packet sequence number replay check failed.");
fAddWindowsDefine("STATUS_IPSEC_INVALID_PACKET",
  sDescription =    "The IPsec header and/or trailer in the packet is invalid.");
fAddWindowsDefine("STATUS_IPSEC_INTEGRITY_CHECK_FAILED",
  sDescription =    "The IPsec integrity check failed.");
fAddWindowsDefine("STATUS_IPSEC_CLEAR_TEXT_DROP",
  sDescription =    "IPsec dropped a clear text packet.");
fAddWindowsDefine("STATUS_IPSEC_AUTH_FIREWALL_DROP",
  sDescription =    "IPsec dropped an incoming ESP packet in authenticated firewall mode.  This drop is benign.");
fAddWindowsDefine("STATUS_IPSEC_THROTTLE_DROP",
  sDescription =    "IPsec dropped a packet due to DOS throttle.");
fAddWindowsDefine("STATUS_IPSEC_DOSP_BLOCK",
  sDescription =    "IPsec Dos Protection matched an explicit block rule.");
fAddWindowsDefine("STATUS_IPSEC_DOSP_RECEIVED_MULTICAST",
  sDescription =    "IPsec Dos Protection received an IPsec specific multicast packet which is not allowed.");
fAddWindowsDefine("STATUS_IPSEC_DOSP_INVALID_PACKET",
  sDescription =    "IPsec Dos Protection received an incorrectly formatted packet.");
fAddWindowsDefine("STATUS_IPSEC_DOSP_STATE_LOOKUP_FAILED",
  sDescription =    "IPsec Dos Protection failed to lookup state.");
fAddWindowsDefine("STATUS_IPSEC_DOSP_MAX_ENTRIES",
  sDescription =    "IPsec Dos Protection failed to create state because there are already maximum number of entries allowed by policy.");
fAddWindowsDefine("STATUS_IPSEC_DOSP_KEYMOD_NOT_ALLOWED",
  sDescription =    "IPsec Dos Protection received an IPsec negotiation packet for a keying module which is not allowed by policy.");
fAddWindowsDefine("STATUS_IPSEC_DOSP_MAX_PER_IP_RATELIMIT_QUEUES",
  sDescription =    "IPsec Dos Protection failed to create per internal IP ratelimit queue because there is already maximum number of queues allowed by policy.");
fAddWindowsDefine("STATUS_VOLMGR_MIRROR_NOT_SUPPORTED",
  sDescription =    "The system does not support mirrored volumes.");
fAddWindowsDefine("STATUS_VOLMGR_RAID5_NOT_SUPPORTED",
  sDescription =    "The system does not support RAID-5 volumes.");
fAddWindowsDefine("STATUS_VIRTDISK_PROVIDER_NOT_FOUND",
  sDescription =    "A virtual disk support provider for the specified file was not found.");
fAddWindowsDefine("STATUS_VIRTDISK_NOT_VIRTUAL_DISK",
  sDescription =    "The specified disk is not a virtual disk.");
fAddWindowsDefine("STATUS_VHD_PARENT_VHD_ACCESS_DENIED",
  sDescription =    "The chain of virtual hard disks is inaccessible. The process has not been granted access rights to the parent virtual hard disk for the differencing disk.");
fAddWindowsDefine("STATUS_VHD_CHILD_PARENT_SIZE_MISMATCH",
  sDescription =    "The chain of virtual hard disks is corrupted. There is a mismatch in the virtual sizes of the parent virtual hard disk and differencing disk.");
fAddWindowsDefine("STATUS_VHD_DIFFERENCING_CHAIN_CYCLE_DETECTED",
  sDescription =    "The chain of virtual hard disks is corrupted. A differencing disk is indicated in its own parent chain.");
fAddWindowsDefine("STATUS_VHD_DIFFERENCING_CHAIN_ERROR_IN_PARENT",
  sDescription =    "The chain of virtual hard disks is inaccessible. There was an error opening a virtual hard disk further up the chain.");
fAddWindowsDefine("CLR_EXCEPTION_CODE",
  sDescription =    "A Common Language Runtime (CLR) exception was thrown.");
fAddWindowsDefine("CPP_EXCEPTION_CODE",
  sDescription =    "A C++ Exception was thrown.",
  sTypeId =         "C++");

doWindowsDefines_by_uValue = {};
doWindowsDefines_by_sName = {};
for oWindowsDefine in aoWindowsDefines:
  oExistingDefine = doWindowsDefines_by_uValue.get(oWindowsDefine.uValue);
  if oExistingDefine:
    # Multiple names may exist for the same value, but everything else should match:
    assert oExistingDefine.sDescription == oWindowsDefine.sDescription, \
        "The value 0x%08X is defined with description %s and %s" % \
        (oWindowsDefine.uValue, oExistingDefine.sDescription, oWindowsDefine.sDescription);
    assert oExistingDefine.sDescription == oWindowsDefine.sDescription, \
        "The value 0x%08X is defined with type id %s and %s" % \
        (oWindowsDefine.uValue, oExistingDefine.sTypeId, oWindowsDefine.sTypeId);
    assert oExistingDefine.sDescription == oWindowsDefine.sDescription, \
        "The value 0x%08X is defined with security impact %s and %s" % \
        (oWindowsDefine.uValue, oExistingDefine.sSecurityImpact, oWindowsDefine.sSecurityImpact);
    # In such cases, the defines are combined into a new one that mentions all names.
    doWindowsDefines_by_uValue[oWindowsDefine.uValue] = cWindowsDefine(
      uValue = oWindowsDefine.uValue,
      sName = oWindowsDefine.sName + " / " + oExistingDefine.sName,
      sDescription = oWindowsDefine.sDescription,
      sTypeId = oWindowsDefine.sTypeId,
      sSecurityImpact = oWindowsDefine.sSecurityImpact,
    );
  else:
    doWindowsDefines_by_uValue[oWindowsDefine.uValue] = oWindowsDefine;
  
  # Obviously, you cannot define a name to have multiple values.
  assert oWindowsDefine.sName not in doWindowsDefines_by_sName, \
      "The name %s is defined as 0x%08X and 0x%08X" % \
      (sName, doWindowsDefines_by_sName[sName].uValue, oWindowsDefine.uValue);
  doWindowsDefines_by_sName[oWindowsDefine.sName] = oWindowsDefine;
  globals()[oWindowsDefine.sName] = oWindowsDefine.uValue;
