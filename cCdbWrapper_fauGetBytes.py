import re;

def cCdbWrapper_fauGetBytes(oCdbWrapper, uAddress, uSize, sComment):
  auBytes = [];
  asBytesOutput = oCdbWrapper.fasSendCommandAndReadOutput("db /c20 0x%X L0x%X; $ %s" % (uAddress, uSize, sComment));
  if not oCdbWrapper.bCdbRunning: return;
  uLineNumber = 0;
  for sLine in asBytesOutput:
    uLineNumber += 1;
    oBytesMatch = re.match(r"^[0-9a-f`]+ ((?:[ \-][\?0-9a-f]{2})+)  .+$", sLine, re.I);
    assert oBytesMatch, \
        "Unexpected output in line %d:\r\n%s" % (uLineNumber, "\r\n".join(asBytesOutput));
    # Convert " xx xx xx-xx xx ..." into ["xx", "xx", "xx", ...]
    asBytes = oBytesMatch.group(1)[1:].replace("-", " ").split(" ");
    for sByte in asBytes:
      if sByte == "??":
        auBytes.append(None);
      else:
        auBytes.append(int(sByte, 16));
  assert len(auBytes) == uSize, \
      "Internal error: expected %d bytes, got %s\r\n%s" % (uSize, repr(auBytes), "\r\n".join(asBytesOutput));
  return auBytes;
