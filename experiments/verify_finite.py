"""Finite-code evidence, not a probabilistic test or performance benchmark."""
import csv, hashlib, json, platform, subprocess, sys, uuid
from datetime import datetime, timezone
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from reference.codec import offset_decode, signed_decode, recode_nibble, recode_bytes, unpack


def main():
    if subprocess.check_output(['git','status','--porcelain'],cwd=ROOT,text=True).strip():
        raise RuntimeError('Commit source before a provenance-bearing run')
    out=ROOT/'results'/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'_'+uuid.uuid4().hex[:8]);out.mkdir()
    manifest=dict(experiment='finite_codec_v1',source_sha=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),python=sys.version,platform=platform.platform(),command=sys.argv,codec_sha256=hashlib.sha256((ROOT/'reference/codec.py').read_bytes()).hexdigest(),performance_claim=False,status='RUNNING')
    def save(): (out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    save()
    for name,rows in [('nibbles',[dict(code=c,signed_nibble=recode_nibble(c),offset_integer=offset_decode(c),signed_integer=signed_decode(recode_nibble(c)),inverse=recode_nibble(recode_nibble(c))) for c in range(16)]),('bytes',[dict(offset_byte=b,signed_byte=recode_bytes(bytes([b]))[0],offset_low=unpack(bytes([b]))[0],offset_high=unpack(bytes([b]))[1],signed_low=unpack(recode_bytes(bytes([b])),signed=True)[0],signed_high=unpack(recode_bytes(bytes([b])),signed=True)[1]) for b in range(256)])]:
        with (out/(name+'.csv')).open('w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    with (out/'run.log').open('w') as f:
        rc=subprocess.run([sys.executable,'-m','pytest','-q','tests'],cwd=ROOT,stdout=f,stderr=subprocess.STDOUT).returncode
    manifest.update(status='PASS' if rc==0 else 'FAIL',return_code=rc,nibble_states=16,byte_states=256);save()
    (out/'summary.md').write_text('Exhaustive 16-nibble/256-byte codec verification: '+manifest['status']+'. This verifies a finite implementation; the decoder-commutation proof is in theory/EXACT_RECODING.md. No hardware or speed claim.\n')
    print(out,manifest['status'])
    if rc:raise RuntimeError('Finite verification failed; artifacts retained')
if __name__=='__main__':main()
