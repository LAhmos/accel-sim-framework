export DATA_ROOT="$( cd "$( dirname "$BASH_SOURCE" )" && pwd )"
TITANX_PASCAL_DATA=$DATA_ROOT/TITAN-X-PASCAL
P100_PASCAL_DATA=$DATA_ROOT/TESLA-P100
FERMI_GTX480_DATA=$DATA_ROOT/GTX480
P1080Ti_DATA=$DATA_ROOT/1080TI_PASCAL
TITANV_DATA=$DATA_ROOT/TITANV
QUADRO_V100_DATA=$DATA_ROOT/QUADRO-V100
TESLA_V100_DATA=$DATA_ROOT/TESLA-V100
TURING_RTX_DATA=$DATA_ROOT/TURING-RTX2060
KEPLER_DATA=$DATA_ROOT/KEPLER-TITAN

rm -rf $TURING_RTX_DATA
rm -rf $TITANX_PASCAL_DATA
rm -rf $P100_PASCAL_DATA
rm -rf $FERMI_GTX480_DATA
rm -rf $P1080Ti_DATA
rm -rf $TITANV_DATA
rm -rf $QUADRO_V100_DATA
rm -rf $TESLA_V100_DATA
rm -rf $KEPLER_DATA
