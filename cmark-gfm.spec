# html_normalization and roundtriptest_library failing
%bcond_with tests

Name:           cmark-gfm
Version:        0.29.0.gfm.13
Release:        1%{?dist}
Summary:        CommonMark parsing and rendering

License:        BSD-2-Clause AND MIT
URL:            https://github.com/github/cmark-gfm
Source0:        https://github.com/github/cmark-gfm/archive/refs/tags/%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
`cmark-gfm` is an extended version of the C reference implementation of
CommonMark, a rationalized version of Markdown syntax with a spec. This
repository adds GitHub Flavored Markdown extensions to the upstream
implementation, as defined in the spec.

The rest of the README is preserved as-is from the upstream source. Note that
the library and binaries produced by this fork are suffixed with `-gfm` in order
to distinguish them from the upstream.

---

It provides a shared library (`libcmark`) with functions for parsing
CommonMark documents to an abstract syntax tree (AST), manipulating
the AST, and rendering the document to HTML, groff man, LaTeX,
CommonMark, or an XML representation of the AST.  It also provides a
command-line program (`cmark`) for parsing and rendering CommonMark
documents.


%package devel
Summary:        Development files for cmark-gfm
Requires:       cmark-gfm-lib%{?_isa} = %{version}-%{release}
Requires:       cmark-gfm%{?_isa} = %{version}-%{release}

%description devel
This package provides the development files for cmark-gfm.



%package lib
Summary:        GitHub's fork of cmark, a parsing and rendering library

%description lib
This package provides the cmark-gfm library.



%prep
%autosetup


%build
%cmake -DCMARK_STATIC=OFF %{?_without_tests:-DCMARK_TESTS=OFF}
%cmake_build


%install
%cmake_install


%check
%if %{with tests}
%cmake_build --target test
%endif


%ldconfig_scriptlets lib


%files
%license COPYING
%{_bindir}/cmark-gfm
%{_mandir}/man1/cmark-gfm.1*


%files lib
%license COPYING
%{_libdir}/libcmark-gfm.so.%{version}
%{_libdir}/libcmark-gfm-extensions.so.%{version}


%files devel
%doc README.md
%{_includedir}/cmark-gfm.h
%{_includedir}/cmark-gfm_export.h
%{_includedir}/cmark-gfm_version.h
%{_includedir}/cmark-gfm-core-extensions.h
%{_includedir}/cmark-gfm-extension_api.h

%{_libdir}/libcmark-gfm.so
%{_libdir}/libcmark-gfm-extensions.so

%{_libdir}/pkgconfig/libcmark-gfm.pc

%{_libdir}/cmake/cmark-gfm.cmake
%{_libdir}/cmake/cmark-gfm-release.cmake
%{_libdir}/cmake-gfm-extensions/cmark-gfm-extensions.cmake
%{_libdir}/cmake-gfm-extensions/cmark-gfm-extensions-release.cmake

%{_mandir}/man3/cmark-gfm.3*


%changelog
* Wed Aug 20 2025 Quadratech188 <quadratech188@gmail.com> 0.29.0.gfm.13-1
- new package built with tito

