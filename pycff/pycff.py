import yatiml

from datetime import datetime
import re
from typing import List, Optional, Union


_valid_license_strings = [
        '0BSD', 'AAL', 'Abstyles', 'Adobe-2006', 'Adobe-Glyph', 'ADSL',
        'AFL-1.1', 'AFL-1.2', 'AFL-2.0', 'AFL-2.1', 'AFL-3.0', 'Afmparse',
        'AGPL-1.0', 'AGPL-3.0-only', 'AGPL-3.0-or-later', 'Aladdin', 'AMDPLPA',
        'AML', 'AMPAS', 'ANTLR-PD', 'Apache-1.0', 'Apache-1.1', 'Apache-2.0',
        'APAFML', 'APL-1.0', 'APSL-1.0', 'APSL-1.1', 'APSL-1.2', 'APSL-2.0',
        'Artistic-1.0', 'Artistic-1.0-cl8', 'Artistic-1.0-Perl',
        'Artistic-2.0', 'Bahyph', 'Barr', 'Beerware', 'BitTorrent-1.0',
        'BitTorrent-1.1', 'Borceux', 'BSD-1-Clause', 'BSD-2-Clause',
        'BSD-2-Clause-FreeBSD', 'BSD-2-Clause-NetBSD', 'BSD-2-Clause-Patent',
        'BSD-3-Clause', 'BSD-3-Clause-Attribution', 'BSD-3-Clause-Clear',
        'BSD-3-Clause-LBNL', 'BSD-3-Clause-No-Nuclear-License',
        'BSD-3-Clause-No-Nuclear-License-2014',
        'BSD-3-Clause-No-Nuclear-Warranty', 'BSD-4-Clause', 'BSD-4-Clause-UC',
        'BSD-Protection', 'BSD-Source-Code', 'BSL-1.0', 'bzip2-1.0.5',
        'bzip2-1.0.6', 'Caldera', 'CATOSL-1.1', 'CC-BY-1.0', 'CC-BY-2.0',
        'CC-BY-2.5', 'CC-BY-3.0', 'CC-BY-4.0', 'CC-BY-NC-1.0', 'CC-BY-NC-2.0',
        'CC-BY-NC-2.5', 'CC-BY-NC-3.0', 'CC-BY-NC-4.0', 'CC-BY-NC-ND-1.0',
        'CC-BY-NC-ND-2.0', 'CC-BY-NC-ND-2.5', 'CC-BY-NC-ND-3.0',
        'CC-BY-NC-ND-4.0', 'CC-BY-NC-SA-1.0', 'CC-BY-NC-SA-2.0',
        'CC-BY-NC-SA-2.5', 'CC-BY-NC-SA-3.0', 'CC-BY-NC-SA-4.0',
        'CC-BY-ND-1.0', 'CC-BY-ND-2.0', 'CC-BY-ND-2.5', 'CC-BY-ND-3.0',
        'CC-BY-ND-4.0', 'CC-BY-SA-1.0', 'CC-BY-SA-2.0', 'CC-BY-SA-2.5',
        'CC-BY-SA-3.0', 'CC-BY-SA-4.0', 'CC0-1.0', 'CDDL-1.0', 'CDDL-1.1',
        'CDLA-Permissive-1.0', 'CDLA-Sharing-1.0', 'CECILL-1.0', 'CECILL-1.1',
        'CECILL-2.0', 'CECILL-2.1', 'CECILL-B', 'CECILL-C', 'ClArtistic',
        'CNRI-Jython', 'CNRI-Python', 'CNRI-Python-GPL-Compatible',
        'Condor-1.1', 'CPAL-1.0', 'CPL-1.0', 'CPOL-1.02', 'Crossword',
        'CrystalStacker', 'CUA-OPL-1.0', 'Cube', 'curl', 'D-FSL-1.0',
        'diffmark', 'DOC', 'Dotseqn', 'DSDP', 'dvipdfm', 'ECL-1.0', 'ECL-2.0',
        'EFL-1.0', 'EFL-2.0', 'eGenix', 'Entessa', 'EPL-1.0', 'EPL-2.0',
        'ErlPL-1.1', 'EUDatagrid', 'EUPL-1.0', 'EUPL-1.1', 'EUPL-1.2',
        'Eurosym', 'Fair', 'Frameworx-1.0', 'FreeImage', 'FSFAP', 'FSFUL',
        'FSFULLR', 'FTL', 'GFDL-1.1-only', 'GFDL-1.1-or-later',
        'GFDL-1.2-only', 'GFDL-1.2-or-later', 'GFDL-1.3-only',
        'GFDL-1.3-or-later', 'Giftware', 'GL2PS', 'Glide', 'Glulxe', 'gnuplot',
        'GPL-1.0-only', 'GPL-1.0-or-later', 'GPL-2.0-only', 'GPL-2.0-or-later',
        'GPL-3.0-only', 'GPL-3.0-or-later', 'gSOAP-1.3b', 'HaskellReport',
        'HPND', 'IBM-pibs', 'ICU', 'IJG', 'ImageMagick', 'iMatix', 'Imlib2',
        'Info-ZIP', 'Intel', 'Intel-ACPI', 'Interbase-1.0', 'IPA', 'IPL-1.0',
        'ISC', 'JasPer-2.0', 'JSON', 'LAL-1.2', 'LAL-1.3', 'Latex2e',
        'Leptonica', 'LGPL-2.0-only', 'LGPL-2.0-or-later', 'LGPL-2.1-only',
        'LGPL-2.1-or-later', 'LGPL-3.0-only', 'LGPL-3.0-or-later', 'LGPLLR',
        'Libpng', 'libtiff', 'LiLiQ-P-1.1', 'LiLiQ-R-1.1', 'LiLiQ-Rplus-1.1',
        'LPL-1.0', 'LPL-1.02', 'LPPL-1.0', 'LPPL-1.1', 'LPPL-1.2', 'LPPL-1.3a',
        'LPPL-1.3c', 'MakeIndex', 'MirOS', 'MIT', 'MIT-advertising', 'MIT-CMU',
        'MIT-enna', 'MIT-feh', 'MITNFA', 'Motosoto', 'mpich2', 'MPL-1.0',
        'MPL-1.1', 'MPL-2.0', 'MPL-2.0-no-copyleft-exception', 'MS-PL',
        'MS-RL', 'MTLL', 'Multics', 'Mup', 'NASA-1.3', 'Naumen', 'NBPL-1.0',
        'NCSA', 'Net-SNMP', 'NetCDF', 'Newsletr', 'NGPL', 'NLOD-1.0', 'NLPL',
        'Nokia', 'NOSL', 'Noweb', 'NPL-1.0', 'NPL-1.1', 'NPOSL-3.0', 'NRL',
        'NTP', 'OCCT-PL', 'OCLC-2.0', 'ODbL-1.0', 'OFL-1.0', 'OFL-1.1',
        'OGTSL', 'OLDAP-1.1', 'OLDAP-1.2', 'OLDAP-1.3', 'OLDAP-1.4',
        'OLDAP-2.0', 'OLDAP-2.0.1', 'OLDAP-2.1', 'OLDAP-2.2', 'OLDAP-2.2.1',
        'OLDAP-2.2.2', 'OLDAP-2.3', 'OLDAP-2.4', 'OLDAP-2.5', 'OLDAP-2.6',
        'OLDAP-2.7', 'OLDAP-2.8', 'OML', 'OpenSSL', 'OPL-1.0', 'OSET-PL-2.1',
        'OSL-1.0', 'OSL-1.1', 'OSL-2.0', 'OSL-2.1', 'OSL-3.0', 'PDDL-1.0',
        'PHP-3.0', 'PHP-3.01', 'Plexus', 'PostgreSQL', 'psfrag', 'psutils',
        'Python-2.0', 'Qhull', 'QPL-1.0', 'Rdisc', 'RHeCos-1.1', 'RPL-1.1',
        'RPL-1.5', 'RPSL-1.0', 'RSA-MD', 'RSCPL', 'Ruby', 'SAX-PD', 'Saxpath',
        'SCEA', 'Sendmail', 'SGI-B-1.0', 'SGI-B-1.1', 'SGI-B-2.0', 'SimPL-2.0',
        'SISSL', 'SISSL-1.2', 'Sleepycat', 'SMLNJ', 'SMPPL', 'SNIA',
        'Spencer-86', 'Spencer-94', 'Spencer-99', 'SPL-1.0', 'SugarCRM-1.1.3',
        'SWL', 'TCL', 'TCP-wrappers', 'TMate', 'TORQUE-1.1', 'TOSL',
        'Unicode-DFS-2015', 'Unicode-DFS-2016', 'Unicode-TOU', 'Unlicense',
        'UPL-1.0', 'Vim', 'VOSTROM', 'VSL-1.0', 'W3C', 'W3C-19980720',
        'W3C-20150513', 'Watcom-1.0', 'Wsuipa', 'WTFPL', 'X11', 'Xerox',
        'XFree86-1.1', 'xinetd', 'Xnet', 'xpp', 'XSkat', 'YPL-1.0', 'YPL-1.1',
        'Zed', 'Zend-2.0', 'Zimbra-1.3', 'Zimbra-1.4', 'Zlib',
        'zlib-acknowledgement', 'ZPL-1.1', 'ZPL-2.0', 'ZPL-2.1']

_valid_country_codes = [
        'AF', 'AX', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM',
        'AW', 'AU', 'AT', 'AZ', 'BS', 'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ',
        'BM', 'BT', 'BO', 'BQ', 'BA', 'BW', 'BV', 'BR', 'IO', 'BN', 'BG', 'BF',
        'BI', 'CV', 'KH', 'CM', 'CA', 'KY', 'CF', 'TD', 'CL', 'CN', 'CX', 'CC',
        'CO', 'KM', 'CG', 'CD', 'CK', 'CR', 'CI', 'HR', 'CU', 'CW', 'CY', 'CZ',
        'DK', 'DJ', 'DM', 'DO', 'EC', 'EG', 'SV', 'GQ', 'ER', 'EE', 'ET', 'FK',
        'FO', 'FJ', 'FI', 'FR', 'GF', 'PF', 'TF', 'GA', 'GM', 'GE', 'DE', 'GH',
        'GI', 'GR', 'GL', 'GD', 'GP', 'GU', 'GT', 'GG', 'GN', 'GW', 'GY', 'HT',
        'HM', 'VA', 'HN', 'HK', 'HU', 'IS', 'IN', 'ID', 'IR', 'IQ', 'IE', 'IM',
        'IL', 'IT', 'JM', 'JP', 'JE', 'JO', 'KZ', 'KE', 'KI', 'KP', 'KR', 'KW'
        'KG', 'LA', 'LV', 'LB', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MO', 'MK',
        'MG', 'MW', 'MY', 'MV', 'ML', 'MT', 'MH', 'MQ', 'MR', 'MU', 'YT', 'MX',
        'FM', 'MD', 'MC', 'MN', 'ME', 'MS', 'MA', 'MZ', 'MM', 'NA', 'NR', 'NP',
        'NL', 'NC', 'NZ', 'NI', 'NE', 'NG', 'NU', 'NF', 'MP', 'NO', 'OM', 'PK',
        'PW', 'PS', 'PA', 'PG', 'PY', 'PE', 'PH', 'PN', 'PL', 'PT', 'PR', 'QA',
        'RE', 'RO', 'RU', 'RW', 'BL', 'SH', 'KN', 'LC', 'MF', 'PM', 'VC', 'WS',
        'SM', 'ST', 'SA', 'SN', 'RS', 'SC', 'SL', 'SG', 'SX', 'SK', 'SI', 'SB',
        'SO', 'ZA', 'GS', 'SS', 'ES', 'LK', 'SD', 'SR', 'SJ', 'SZ', 'SE', 'CH',
        'SY', 'TW', 'TJ', 'TZ', 'TH', 'TL', 'TG', 'TK', 'TO', 'TT', 'TN', 'TR',
        'TM', 'TC', 'TV', 'UG', 'UA', 'AE', 'GB', 'UM', 'US', 'UY', 'UZ', 'VU',
        'VE', 'VN', 'VG', 'VI', 'WF', 'EH', 'YE', 'ZM', 'ZW']

_valid_reference_types = [
        'art', 'article', 'audiovisual', 'bill', 'blog', 'book', 'catalogue',
        'conference', 'conference-paper', 'data', 'database', 'dictionary',
        'edited-work', 'encyclopedia', 'film-broadcast', 'generic',
        'government-document', 'grant', 'hearing', 'historical-work',
        'legal-case', 'legal-rule', 'magazine-article', 'manual', 'map',
        'multimedia', 'music', 'newspaper-article', 'pamphlet', 'patent',
        'personal-communication', 'proceedings', 'report', 'serial', 'slides',
        'software', 'software-code', 'software-container',
        'software-executable', 'software-virtual-machine', 'sound-recording',
        'standard', 'statute', 'thesis', 'unpublished', 'video', 'website']


_regex_url = (
        '^(?:(?:https?|ftp)://)(?:\S+(?::\S*)?@)?(?:(?!(?:10|127)'
        '(?:\.\d{1,3}){3})(?!(?:169\.254|192\.168)(?:\.\d{1,3}){2})'
        '(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?'
        '|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}'
        '(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\u00a1'
        '-\uffff0-9]-?)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-'
        '\uffff0-9]-?)*[a-z\u00a1-\uffff0-9]+)*(?:\.(?:[a-z\u00a1-'
        '\uffff]{2,})))(?::\d{2,5})?(?:/\S*)?$')


_regex_doi = '^10\.\d{4,9}(\.\d+)?/[A-Za-z0-9-\._;\(\)\[\]\\\\:/]+$'

_regex_orcid = ('https://orcid\\.org/[0-9]{4}-[0-9]{4}-[0-9]{4}-'
                '[0-9]{3}[0-9X]{1}')


def _check_arg_regex(value: str, regex: str) -> None:
    if re.fullmatch(regex, value) is None:
        raise RuntimeError('Invalid value "{}".'.format(value))


def _check_arg_url(value: str) -> None:
    try:
        _check_arg_regex(value, _regex_url)
    except RuntimeError:
        raise RuntimeError('"{}" is not a valid URL.'.format(value))


def _check_arg_doi(value: str) -> None:
    try:
        _check_arg_regex(value, _regex_doi)
    except RuntimeError:
        raise RuntimeError('"{}" is not a valid doi.'.format(value))


def _check_arg_orcid(value: str) -> None:
    try:
        _check_arg_regex(value, _regex_orcid)
    except RuntimeError:
        raise RuntimeError('"{}" is not a valid ORCID.'.format(value))


def _check_arg_set(value: str, legal_values: List[str]) -> None:
    if value not in legal_values:
        raise RuntimeError('Invalid value {}'.format(value))


def _check_is_date(value: datetime) -> None:
    if (
            value.hour != 0 or value.minute != 0 or value.second != 0 or
            value.microsecond != 0 or value.tzinfo is not None):
        raise RuntimeError('Invalid date containing time of day "{}".'.format(
            value))


class Identifier:
    """Description of a CFF Identifier.

    An identifier object represents a persistent identifier.
    """
    def __init__(self, typ: str, value: str) -> None:
        """Create an Identifier.

        Args:
            See the CFF standard.
        """
        _check_arg_set(typ, ['doi', 'url', 'swh', 'other'])

        self.typ = typ
        self.value = value


class Person:
    """Description of a person in CFF 1.0.3.
    """
    def __init__(
            self,
            family_names: str,
            given_names: str,
            name_particle: Optional[str] = None,
            name_suffix: Optional[str] = None,
            affiliation: Optional[str] = None,
            address: Optional[str] = None,
            city: Optional[str] = None,
            region: Optional[str] = None,
            post_code: Optional[str] = None,
            country: Optional[str] = None,
            orcid: Optional[str] = None,
            email: Optional[str] = None,
            tel: Optional[str] = None,
            fax: Optional[str] = None,
            website: Optional[str] = None
            ) -> None:

        if country is not None:
            _check_arg_set(country, _valid_country_codes)
        if orcid is not None:
            _check_arg_orcid(orcid)
        if email is not None:
            _check_arg_regex(email, '^[\S]+@[\S]+\.[\S]{2,}$')
        if website is not None:
            _check_arg_url(website)

        self.family_names = family_names
        self.given_names = given_names
        self.name_particle = name_particle
        self.name_suffix = name_suffix
        self.affiliation = affiliation
        self.address = address
        self.city = city
        self.region = region
        self.post_code = post_code
        self.country = country
        self.orcid = orcid
        self.email = email
        self.tel = tel
        self.fax = fax
        self.website = website

    @classmethod
    def _yatiml_savorize(cls, node: yatiml.Node) -> None:
        node.dashes_to_unders_in_keys()

    @classmethod
    def _yatiml_sweeten(cls, node: yatiml.Node) -> None:
        node.unders_to_dashes_in_keys()


class Entity:
    """A class representing an entity.

    This is some legal entity, an organisation.
    """
    def __init__(
            self,
            name: str,
            address: Optional[str] = None,
            city: Optional[str] = None,
            region: Optional[str] = None,
            post_code: Optional[str] = None,
            country: Optional[str] = None,
            orcid: Optional[str] = None,
            email: Optional[str] = None,
            tel: Optional[str] = None,
            fax: Optional[str] = None,
            website: Optional[str] = None,
            date_start: Optional[datetime] = None,
            date_end: Optional[datetime] = None,
            location: Optional[str] = None
            ) -> None:
        """Create an Entity object.

        Args:
            See the standard.
        """
        if orcid is not None:
            _check_arg_orcid(orcid)
        if email is not None:
            _check_arg_regex(email, '^[\S]+@[\S]+\.[\S]{2,}$')
        if website is not None:
            _check_arg_url(website)
        if date_start is not None:
            _check_is_date(date_start)
        if date_end is not None:
            _check_is_date(date_end)

        self.name = name
        self.address = address
        self.city = city
        self.region = region
        self.post_code = post_code
        self.country = country
        self.orcid = orcid
        self.email = email
        self.tel = tel
        self.fax = fax
        self.website = website
        self.date_start = date_start
        self.date_end = date_end
        self.location = location


class Reference:
    """A class representing a reference to some citable object.
    """
    def __init__(
            self,
            typ: str,       # really 'type'
            authors: List[Union[Entity, Person]],
            title: str,
            abbreviation: Optional[str] = None,
            abstract: Optional[str] = None,
            collection_doi: Optional[str] = None,
            collection_title: Optional[str] = None,
            collection_type: Optional[str] = None,
            commit: Optional[str] = None,
            conference: Optional[Entity] = None,
            contact: Optional[List[Union[Entity, Person]]] = None,
            copyright: Optional[str] = None,
            data_type: Optional[str] = None,
            database: Optional[str] = None,
            database_provider: Optional[Entity] = None,
            date_accessed: Optional[datetime] = None,
            date_downloaded: Optional[datetime] = None,
            date_published: Optional[datetime] = None,
            date_released: Optional[datetime] = None,
            department: Optional[str] = None,
            doi: Optional[str] = None,
            edition: Optional[str] = None,
            editors: Optional[List[Union[Entity, Person]]] = None,
            editors_series: Optional[List[Union[Entity, Person]]] = None,
            end: Optional[int] = None,
            entry: Optional[str] = None,
            filename: Optional[str] = None,
            format: Optional[str] = None,
            identifiers: Optional[List[Identifier]] = None,
            institution: Optional[Entity] = None,
            isbn: Optional[str] = None,
            issn: Optional[str] = None,
            issue: Optional[int] = None,
            issue_date: Optional[str] = None,
            issue_title: Optional[str] = None,
            journal: Optional[str] = None,
            keywords: Optional[List[str]] = None,
            languages: Optional[List[str]] = None,
            license: Optional[str] = None,
            license_url: Optional[str] = None,
            location: Optional[Entity] = None,
            loc_start: Optional[int] = None,
            loc_end: Optional[int] = None,
            medium: Optional[str] = None,
            month: Optional[int] = None,
            nihmsid: Optional[str] = None,
            notes: Optional[str] = None,
            number: Optional[str] = None,
            number_volumes: Optional[int] = None,
            pages: Optional[int] = None,
            patent_states: Optional[List[str]] = None,
            pmcid: Optional[str] = None,
            publisher: Optional[Entity] = None,
            recipients: Optional[List[Union[Entity, Person]]] = None,
            repository: Optional[str] = None,
            repository_code: Optional[str] = None,
            repository_artifact: Optional[str] = None,
            scope: Optional[str] = None,
            section: Optional[str] = None,
            senders: Optional[List[Union[Entity, Person]]] = None,
            status: Optional[str] = None,
            start: Optional[int] = None,
            term: Optional[str] = None,
            thesis_type: Optional[str] = None,
            translators: Optional[List[Union[Entity, Person]]] = None,
            url: Optional[str] = None,
            version: Optional[str] = None,
            volume: Optional[int] = None,
            volume_title: Optional[str] = None,
            year: Optional[int] = None,
            year_original: Optional[int] = None
            ) -> None:
                """Create a Reference object.

                Args:
                    See the CFF standard.
                """
                # TODO: check reference type
                if collection_doi is not None:
                    _check_arg_doi(collection_doi)
                if commit is not None:
                    _check_arg_regex(commit, '^[a-f0-9]{7,40}$')
                # TODO: check date_accessed, date_downloaded, date_published, date_released
                if doi is not None:
                    _check_arg_doi(doi)
                if license is not None:
                    _check_arg_set(license, _valid_license_strings)
                if license_url is not None:
                    _check_arg_url(license_url)
                if repository is not None:
                    _check_arg_url(repository)
                if repository_code is not None:
                    _check_arg_url(repository_code)
                if repository_artifact is not None:
                    _check_arg_url(repository_artifact)
                _check_arg_set(typ, _valid_reference_types)
                if url is not None:
                    _check_arg_url(url)

                self.typ = typ
                self.abbreviation = abbreviation
                self.abstract = abstract
                self.authors = authors
                self.collection_doi = collection_doi
                self.collection_title = collection_title
                self.collection_type = collection_type
                self.commit = commit
                self.conference = conference
                self.contact = contact
                self.copyright = copyright
                self.data_type = data_type
                self.database = database
                self.database_provider = database_provider
                self.date_accessed = date_accessed
                self.date_downloaded = date_downloaded
                self.date_published = date_published
                self.date_released = date_released
                self.dapartment = department
                self.doi = doi
                self.edition = edition
                self.editors = editors
                self.editors_series = editors_series
                self.end = end
                self.entry = entry
                self.filename = filename
                self.format = format
                self.identifiers = identifiers
                self.institution = institution
                self.isbn = isbn
                self.issn = issn
                self.issue = issue
                self.issue_date = issue_date
                self.issue_title = issue_title
                self.journal = journal
                self.keywords = keywords
                self.languages = languages
                self.license = license
                self.license_url = license_url
                self.location = location
                self.loc_start = loc_start
                self.loc_end = loc_end
                self.medium = medium
                self.month = month
                self.nihmsid = nihmsid
                self.notes = notes
                self.number = number
                self.number_volumes = number_volumes
                self.pages = pages
                self.patent_states = patent_states
                self.pmcid = pmcid
                self.publisher = publisher
                self.recipients = recipients
                self.repository = repository
                self.repository_code = repository_code
                self.repository_artifact = repository_artifact
                self.scope = scope
                self.section = section
                self.senders = senders
                self.status = status
                self.start = start
                self.term = term
                self.thesis_type = thesis_type
                self.title = title
                self.translators = translators
                self.url = url
                self.version = version
                self.volume = volume
                self.volume_title = volume_title
                self.year = year
                self.year_original = year_original

    @classmethod
    def _yatiml_recognize(cls, node: yatiml.UnknownNode) -> None:
        pass

    @classmethod
    def _yatiml_savorize(cls, node: yatiml.Node) -> None:
        node.dashes_to_unders_in_keys()
        node.rename_attribute('type', 'typ')

    @classmethod
    def _yatiml_sweeten(cls, node: yatiml.Node) -> None:
        node.rename_attribute('typ', 'type')
        node.unders_to_dashes_in_keys()


class CitationCFF:
    """A class representing a CITATION.cff file.
    """
    def __init__(self,
            cff_version: str,
            message: str,
            title: str,
            version: str,
            authors: List[Union[Person, Entity]],
            date_released: datetime,
            abstract: Optional[str] = None,
            identifiers: Optional[List[Identifier]] = None,
            keywords: Optional[str] = None,
            references: Optional[List[Reference]] = None,
            contact: Optional[List[Union[Person, Entity]]] = None,
            doi: Optional[str] = None,
            commit: Optional[str] = None,
            license: Optional[str] = None,
            license_url: Optional[str] = None,
            repository: Optional[str] = None,
            repository_code: Optional[str] = None,
            repository_artifact: Optional[str] = None,
            url: Optional[str] = None,
            ) -> None:
        """Create a CitationCFF object.

        Args:
            See the spec
        """
        _check_arg_regex(cff_version, '1\.1\.0')
        if commit is not None:
            _check_arg_regex(commit, '^[a-f0-9]{7,40}$')
        _check_is_date(date_released)
        if doi is not None:
            _check_arg_doi(doi)
        if license is not None:
            _check_arg_set(license, _valid_license_strings)
        if license_url is not None:
            _check_arg_url(license_url)
        if repository is not None:
            _check_arg_url(repository)
        if repository_code is not None:
            _check_arg_url(repository_code)
        if repository_artifact is not None:
            _check_arg_url(repository_artifact)
        if url is not None:
            _check_arg_url(url)

        self.cff_version = cff_version
        self.message = message
        self.title = title
        self.version = version
        self.authors = authors
        self.date_released = date_released
        self.abstract = abstract
        self.identifiers = identifiers
        self.keywords = keywords
        self.references = references
        self.contact = contact
        self.doi = doi
        self.commit = commit
        self.license = license
        self.license_url = license_url
        self.repository = repository
        self.repository_code = repository_code
        self.repository_artifact = repository_artifact
        self.url = url

    @classmethod
    def _yatiml_savorize(cls, node: yatiml.Node) -> None:
        node.dashes_to_unders_in_keys()

    @classmethod
    def _yatiml_sweeten(cls, node: yatiml.Node) -> None:
        node.unders_to_dashes_in_keys()


_all_classes = (CitationCFF, Identifier, Person, Entity, Reference)


load = yatiml.load_function(*_all_classes)


dump = yatiml.dump_function(*_all_classes)


dumps = yatiml.dumps_function(*_all_classes)
