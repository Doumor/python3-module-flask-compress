%define pypi_name flask-compress

%def_with check

Name:    python3-module-%pypi_name
Version: 1.14
Release: alt1

Summary: Compress responses of your Flask application
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/Flask-Compress/
VCS:     https://github.com/colour-science/flask-compress

Packager: Danilkin Danila <danild@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-flask
BuildRequires: python3-module-pytest
BuildRequires: python3-module-brotlipy
%endif

BuildArch: noarch

Source: %name-%version.tar
Patch0: version.patch

%description
Flask-Compress allows you to easily compress your Flask application's responses with gzip, deflate or brotli. It originally started as a fork of Flask-gzip.

The preferred solution is to have a server (like Nginx) automatically compress the static files for you. If you don't have that option Flask-Compress will solve the problem for you.

%prep
%setup -n %name-%version
%patch0
# Get rid of unnecessary dependencies
sed -i '/brotli;/d' setup.py
rm -rf %{pypi_name}.egg-info

# Manually write version to pyproject.toml
sed -i 's|{version}|%{version}|' pyproject.toml
sed -i 's|{version}|%{version}|' setup.py

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.md LICENSE.txt
%python3_sitelibdir/flask_compress/
%python3_sitelibdir/Flask_Compress-%version.dist-info

%changelog
* Tue Oct 03 2023 Danilkin Danila <danild@altlinux.org> 1.14-alt1
- Initial build for Sisyphus
