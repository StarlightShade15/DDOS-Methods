sysctl -w net.core.wmem_max=134217728
sysctl -w net.core.rmem_max=134217728
sysctl -w net.core.wmem_default=33554432
sysctl -w net.core.rmem_default=33554432

sysctl -w net.ipv4.tcp_wmem="4096 87380 134217728"
sysctl -w net.ipv4.tcp_rmem="4096 87380 134217728"

sysctl -w net.ipv4.udp_wmem_min=16384
sysctl -w net.ipv4.udp_rmem_min=16384

sysctl -w net.ipv4.tcp_congestion_control=bbr
sysctl -w net.ipv4.tcp_fastopen=3
sysctl -w net.ipv4.tcp_low_latency=1
sysctl -w net.ipv4.tcp_fin_timeout=10
sysctl -w net.ipv4.tcp_slow_start_after_idle=0

sysctl -w net.core.netdev_max_backlog=250000
sysctl -w net.core.somaxconn=65535
sysctl -w net.ipv4.tcp_max_syn_backlog=65535

sysctl -w net.core.default_qdisc=fq
tc qdisc replace dev eth0 root fq
tc qdisc replace dev eth0 root fq_codel

ethtool -G eth0 rx 4096 tx 4096
ethtool -C eth0 rx-usecs 0 tx-usecs 0
ethtool -K eth0 tso on gso on gro on
ethtool -K eth0 tso off gso off gro off

echo ffffffff > /sys/class/net/eth0/queues/rx-0/rps_cpus
echo ffffffff > /sys/class/net/eth0/queues/tx-0/xps_cpus

sysctl -w net.core.busy_poll=50
sysctl -w net.core.busy_read=50

sysctl -w net.ipv4.route.flush=1
