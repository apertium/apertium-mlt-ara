TMPDIR=/tmp

if [[ $1 = "ar-mt" ]]; then

lt-expand ../apertium-mt-ar.ar.dix | sort -u |  sed 's/:/%/g' | cut -f1 -d'%' |  sed 's/^/^/g' | sed 's/$/$ ^.<sent>$/g' | tee $TMPDIR/tmp_testvoc1.txt |
        apertium-pretransfer|
        apertium-transfer ../apertium-mt-ar.ar-mt.t1x  ../ar-mt.t1x.bin  ../ar-mt.autobil.bin | tee $TMPDIR/tmp_testvoc2.txt | 
        lt-proc -d ../ar-mt.autogen.bin > $TMPDIR/tmp_testvoc3.txt
paste -d _ $TMPDIR/tmp_testvoc1.txt $TMPDIR/tmp_testvoc2.txt $TMPDIR/tmp_testvoc3.txt | sed 's/\^.<sent>\$//g' | sed 's/_/   --------->  /g'

elif [[ $1 = "mt-ar" ]]; then

lt-expand ../apertium-mt-ar.mt.dix | sort -u | sed 's/:/%/g' | cut -f1 -d'%' |  sed 's/^/^/g' | sed 's/$/$ ^.<sent>$/g' | tee $TMPDIR/tmp_testvoc1.txt |
        apertium-pretransfer|
        apertium-transfer ../apertium-mt-ar.mt-ar.t1x  ../mt-ar.t1x.bin  ../mt-ar.autobil.bin | tee $TMPDIR/tmp_testvoc2.txt |
        lt-proc -d ../mt-ar.autogen.bin > $TMPDIR/tmp_testvoc3.txt
paste -d _ $TMPDIR/tmp_testvoc1.txt $TMPDIR/tmp_testvoc2.txt $TMPDIR/tmp_testvoc3.txt | sed 's/\^.<sent>\$//g' | sed 's/_/   --------->  /g'

else
	echo "sh inconsistency.sh <direction>";
fi
