%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from test_declarative-0.0.5.gem by gem2rpm -*- rpm-spec -*-
%global gem_name test_declarative

Summary: Simply adds a declarative test method syntax to test/unit
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.0.5
Release: 11%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/svenfuchs/test_declarative
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Minitest 5 support
# https://github.com/svenfuchs/test_declarative/pull/4
Patch0: rubygem-test_declarative-0.0.5-minitest5.patch

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygem(minitest)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Simply adds a declarative test method syntax to test/unit.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - << \EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

pushd .%{gem_instdir}
%patch0 -p1
popd

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
%{?scl:scl enable %{scl} - << \EOF}
ruby -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
%{?scl:EOF}
popd

%files
%dir %{gem_instdir}
%exclude %{gem_cache}
%{gem_libdir}
%{gem_spec}
%doc %{gem_instdir}/MIT-LICENSE

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.textile
%{gem_instdir}/test

%changelog
* Sat Feb 20 2016 Pavel Valena <pvalena@redhat.com> - 0.0.5-11
- Add scl macros

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 19 2015 Josef Stribny <jstribny@redhat.com> - 0.0.5-8
- Use Minitest 5

* Thu Jun 19 2014 Vít Ondruch <vondruch@redhat.com> - 0.0.5-7
- Fix FTBFS in Rawhide (rhbz#1107256).

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 26 2013 Vít Ondruch <vondruch@redhat.com> - 0.0.5-4
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 20 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.0.5-1
- Initial package
