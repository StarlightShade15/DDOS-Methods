ulimit -n 1048576

export GOMAXPROCS=$(nproc)
export OMP_NUM_THREADS=$(nproc)

export MALLOC_ARENA_MAX=2
export MALLOC_TRIM_THRESHOLD_=262144

export RES_OPTIONS="attempts:1 timeout:1"

ethtool -k eth0
ethtool -g eth0
tc qdisc show
