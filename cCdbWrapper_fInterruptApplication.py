import signal, time;
from mWindowsAPI import fSuspendProcessForId, fuCreateThreadInProcessForIdAndAddress, fDebugBreakProcessForId; #fSendCtrlCToProcessForId;

def cCdbWrapper_fInterruptApplication(oCdbWrapper):
  # Asking cdb to interrupt the application can cause it to inject a thread that triggers an int 3. Unfortunately,
  # we have no reliable way of determining if this is the case or if the application itself has triggered an int 3.
  #
  # To remove any confusion, we will create a utility process that we also debug. In this utility process, we will
  # create a new thread and have it attempt to execute code at address 0. This will cause an access violation, which
  # will interrupt the application and cause cdb to report it. We can easily distinguish this exception from any other
  # exception caused by the target application because it will be reported to have happened in the utility process.
  assert oCdbWrapper.bApplicationIsRunnning, \
      "cdb cannot be asked to interrupt the application if the application is not running!";
  assert not oCdbWrapper.uUtilityInterruptThreadId, \
      "cdb cannot be asked to interrupt the application twice!";
  # Suspend all processes immediately.
  for uId in oCdbWrapper.doProcess_by_uId.keys():
    fSuspendProcessForId(uId);
  oCdbWrapper.uUtilityInterruptThreadId = fuCreateThreadInProcessForIdAndAddress(oCdbWrapper.uUtilityProcessId, 0x0);
#  fDebugBreakProcessForId(oCdbWrapper.uUtilityProcessId);
#  fSendCtrlCToProcessForId(oCdbWrapper.oCdbProcess.pid);
