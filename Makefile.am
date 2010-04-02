bin_PROGRAMS=gtktypepad
gtktypepad_SOURCES=gtktypepad.c
AM_CPPFLAGS=-DDATA_DIR=\"$(pkgdatadir)\" -DLOCALE_DIR=\"$(datadir)/locale\"
INCLUDES=${GTK_CFLAGS}
gtktypepad_LDADD=${GTK_LIBS}
dist_pkgdata_DATA=data/typepad.png data/loading.gif data/reload.png data/config.png data/post.png data/home.png data/logo.png
EXTRA_DIST=gtktypepad.spec
