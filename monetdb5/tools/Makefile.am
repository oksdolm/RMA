
## This file is generated by autogen.py, do not edit
## Process this file with automake to produce Makefile.in
## autogen includes dependencies so automake doesn't need to generated them

AUTOMAKE_OPTIONS = no-dependencies 1.4 foreign

libmonetdb5_la_CFLAGS=-DLIBMONETDB5 $(AM_CFLAGS)
monetdb5dir = $(libdir)
if WIN32
LIB31 = $(libxml2_LIBS)
else
LIB31 =
endif
if WIN32
LIB30 = $(pcre_LIBS)
else
LIB30 =
endif
if WIN32
LIB29 = $(openssl_LIBS)
else
LIB29 =
endif
if WIN32
LIB28 = $(DL_LIBS)
else
LIB28 =
endif
if WIN32
LIB27 = $(PTHREAD_LIBS)
else
LIB27 =
endif
if WIN32
LIB26 = $(MALLOC_LIBS)
else
LIB26 =
endif
if WIN32
LIB25 = $(SOCKET_LIBS)
else
LIB25 =
endif
if WIN32
LIB24 = $(MATH_LIBS)
else
LIB24 =
endif
if WIN32
LIB23 = $(UUID_LIBS)
else
LIB23 =
endif
if WIN32
LIB22 = ../../common/stream/libstream.la
else
LIB22 =
endif
if WIN32
if HAVE_MAPI
LIB21 = ../../clients/mapilib/libmapi.la
else
LIB21 =
endif
else
LIB21 =
endif
if WIN32
LIB20 = ../../gdk/libbat.la
else
LIB20 =
endif
if WIN32
LIB19 = ../../common/utils/libstrptime.la
else
LIB19 =
endif
libmonetdb5_la_LIBADD = ../mal/libmal.la ../modules/atoms/libatoms.la ../modules/kernel/libkernel.la ../modules/mal/libmal.la ../optimizer/liboptimizer.la ../scheduler/libscheduler.la ../../common/utils/libmsabaoth.la ../../common/utils/libmuuid.la $(LIB19) $(LIB20) $(LIB21) $(LIB22) $(LIB23) $(LIB24) $(LIB25) $(LIB26) $(LIB27) $(LIB28) $(LIB29) $(LIB30) $(LIB31)
$(do)install-monetdb5LTLIBRARIES : 
nodist_libmonetdb5_la_SOURCES = 
dist_libmonetdb5_la_SOURCES =
libmonetdb5_la_LDFLAGS = -version-info $(MONETDB5_VERSION)
libmonetdb5.res: libmonetdb5.rc
monetdb5.pc: monetdb5.pc.in
AM_CPPFLAGS = -I$(srcdir)
CFLAGS += $(THREAD_SAVE_FLAGS)
dist-hook:
	mkdir -p $(distdir)/Tests
	cp -pR $(srcdir)/Tests/* $(distdir)/Tests
if NOT_WIN32
C_monetdb5_pc = monetdb5.pc
endif
uninstall-local-:
install-exec-local-:
install-exec-local-monetdb5.pc: monetdb5.pc
	-mkdir -p $(DESTDIR)$(libdir)/pkgconfig
	-$(RM) $(DESTDIR)$(libdir)/pkgconfig/monetdb5.pc
	$(INSTALL_DATA) $< $(DESTDIR)$(libdir)/pkgconfig/monetdb5.pc

uninstall-local-monetdb5.pc: 
	$(RM) $(DESTDIR)$(libdir)/pkgconfig/monetdb5.pc

BUILT_SOURCES = $(C_monetdb5_pc)
MOSTLYCLEANFILES = $(C_monetdb5_pc)
EXTRA_DIST = Makefile.ag Makefile.msc libmonetdb5.rc monetdb5.pc.in
monetdb5_LTLIBRARIES = libmonetdb5.la
uninstall-local: uninstall-local-$(C_monetdb5_pc)
install-exec-local: install-exec-local-$(C_monetdb5_pc)

  include $(top_srcdir)/buildtools/conf/rules.mk
