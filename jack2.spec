#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jack2
Version  : 1.9.18
Release  : 7
URL      : https://github.com/jackaudio/jack2/archive/v1.9.18/jack2-1.9.18.tar.gz
Source0  : https://github.com/jackaudio/jack2/archive/v1.9.18/jack2-1.9.18.tar.gz
Summary  : the Jack Audio Connection Kit: a low-latency synchronous callback-based media server
Group    : Development/Tools
License  : GPL-2.0
Requires: jack2-bin = %{version}-%{release}
Requires: jack2-lib = %{version}-%{release}
Requires: jack2-license = %{version}-%{release}
Requires: jack2-man = %{version}-%{release}
BuildRequires : eigen-dev
BuildRequires : libsamplerate-dev
BuildRequires : libsndfile-dev
BuildRequires : opus-dev
BuildRequires : pkgconfig(alsa)
BuildRequires : readline-dev
Patch1: 0001-Makefile-quick-wrapper-for-waf.patch

%description
-------------------------------
JACK2 on Windows
-------------------------------

%package bin
Summary: bin components for the jack2 package.
Group: Binaries
Requires: jack2-license = %{version}-%{release}

%description bin
bin components for the jack2 package.


%package dev
Summary: dev components for the jack2 package.
Group: Development
Requires: jack2-lib = %{version}-%{release}
Requires: jack2-bin = %{version}-%{release}
Provides: jack2-devel = %{version}-%{release}
Requires: jack2 = %{version}-%{release}

%description dev
dev components for the jack2 package.


%package lib
Summary: lib components for the jack2 package.
Group: Libraries
Requires: jack2-license = %{version}-%{release}

%description lib
lib components for the jack2 package.


%package license
Summary: license components for the jack2 package.
Group: Default

%description license
license components for the jack2 package.


%package man
Summary: man components for the jack2 package.
Group: Default

%description man
man components for the jack2 package.


%prep
%setup -q -n jack2-1.9.18
cd %{_builddir}/jack2-1.9.18
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1618607301
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1618607301
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jack2
cp %{_builddir}/jack2-1.9.18/COPYING %{buildroot}/usr/share/package-licenses/jack2/db95910cb27890d60e596e4c622fc3eeba6693fa
cp %{_builddir}/jack2-1.9.18/android/NOTICE %{buildroot}/usr/share/package-licenses/jack2/56775a72fbc8b1416c51326851d83c2121a92c98
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/alsa_in
/usr/bin/alsa_out
/usr/bin/jack_alias
/usr/bin/jack_bufsize
/usr/bin/jack_connect
/usr/bin/jack_control
/usr/bin/jack_cpu
/usr/bin/jack_cpu_load
/usr/bin/jack_disconnect
/usr/bin/jack_evmon
/usr/bin/jack_freewheel
/usr/bin/jack_iodelay
/usr/bin/jack_latent_client
/usr/bin/jack_load
/usr/bin/jack_lsp
/usr/bin/jack_metro
/usr/bin/jack_midi_dump
/usr/bin/jack_midi_latency_test
/usr/bin/jack_midiseq
/usr/bin/jack_midisine
/usr/bin/jack_monitor_client
/usr/bin/jack_multiple_metro
/usr/bin/jack_net_master
/usr/bin/jack_net_slave
/usr/bin/jack_netsource
/usr/bin/jack_property
/usr/bin/jack_rec
/usr/bin/jack_samplerate
/usr/bin/jack_server_control
/usr/bin/jack_session_notify
/usr/bin/jack_showtime
/usr/bin/jack_simdtests
/usr/bin/jack_simple_client
/usr/bin/jack_simple_session_client
/usr/bin/jack_test
/usr/bin/jack_thru
/usr/bin/jack_transport
/usr/bin/jack_unload
/usr/bin/jack_wait
/usr/bin/jack_zombie
/usr/bin/jackd

%files dev
%defattr(-,root,root,-)
/usr/include/jack/control.h
/usr/include/jack/intclient.h
/usr/include/jack/jack.h
/usr/include/jack/jslist.h
/usr/include/jack/metadata.h
/usr/include/jack/midiport.h
/usr/include/jack/net.h
/usr/include/jack/ringbuffer.h
/usr/include/jack/session.h
/usr/include/jack/statistics.h
/usr/include/jack/systemdeps.h
/usr/include/jack/thread.h
/usr/include/jack/transport.h
/usr/include/jack/types.h
/usr/include/jack/uuid.h
/usr/include/jack/weakjack.h
/usr/include/jack/weakmacros.h
/usr/lib64/libjack.so
/usr/lib64/libjacknet.so
/usr/lib64/libjackserver.so
/usr/lib64/pkgconfig/jack.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/jack/audioadapter.so
/usr/lib64/jack/inprocess.so
/usr/lib64/jack/jack_alsa.so
/usr/lib64/jack/jack_alsarawmidi.so
/usr/lib64/jack/jack_dummy.so
/usr/lib64/jack/jack_loopback.so
/usr/lib64/jack/jack_net.so
/usr/lib64/jack/jack_netone.so
/usr/lib64/jack/jack_proxy.so
/usr/lib64/jack/netadapter.so
/usr/lib64/jack/netmanager.so
/usr/lib64/jack/profiler.so
/usr/lib64/libjack.so.0
/usr/lib64/libjack.so.0.1.0
/usr/lib64/libjacknet.so.0
/usr/lib64/libjacknet.so.0.1.0
/usr/lib64/libjackserver.so.0
/usr/lib64/libjackserver.so.0.1.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jack2/56775a72fbc8b1416c51326851d83c2121a92c98
/usr/share/package-licenses/jack2/db95910cb27890d60e596e4c622fc3eeba6693fa

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/alsa_in.1
/usr/share/man/man1/alsa_out.1
/usr/share/man/man1/jack_bufsize.1
/usr/share/man/man1/jack_connect.1
/usr/share/man/man1/jack_disconnect.1
/usr/share/man/man1/jack_freewheel.1
/usr/share/man/man1/jack_impulse_grabber.1
/usr/share/man/man1/jack_iodelay.1
/usr/share/man/man1/jack_load.1
/usr/share/man/man1/jack_lsp.1
/usr/share/man/man1/jack_metro.1
/usr/share/man/man1/jack_monitor_client.1
/usr/share/man/man1/jack_netsource.1
/usr/share/man/man1/jack_property.1
/usr/share/man/man1/jack_samplerate.1
/usr/share/man/man1/jack_showtime.1
/usr/share/man/man1/jack_simple_client.1
/usr/share/man/man1/jack_transport.1
/usr/share/man/man1/jack_unload.1
/usr/share/man/man1/jack_wait.1
/usr/share/man/man1/jackd.1
/usr/share/man/man1/jackrec.1
