import pprint
import argparse
import re
import sys

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--part', default="1", choices=("1", "2"))
    return parser.parse_args()

class Field:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def is_valid(self):
        raise NotImplementedError


class ByrField(Field):
    def is_valid(self):
        if not len(self.value) == 4:
            return False

        try:
            year = int(self.value)
        except ValueError:
            return False

        return 1920 <= year <= 2002


class IyrField(Field):
    def is_valid(self):
        if not len(self.value) == 4:
            return False

        try:
            year = int(self.value)
        except ValueError:
            return False

        return 2010 <= year <= 2020


class EyrField(Field):
    def is_valid(self):
        if not len(self.value) == 4:
            return False

        try:
            year = int(self.value)
        except ValueError:
            return False

        return 2020 <= year <= 2030


class HgtField(Field):
    def is_valid(self):
        pattern = re.compile(r"(?P<height>\d+)(?P<unit>cm|in)")
        match = pattern.match(self.value)
        if not match:
            return False
        
        unit = match.group('unit')

        try:
            height = int(match.group('height'))
        except ValueError:
            return False

        if unit == 'cm':
            return 150 <= height <= 193

        return 59 <= height <= 76


class HclField(Field):
    def is_valid(self):
        pattern = re.compile(r"#[0-9a-f]{6}")
        return bool(pattern.match(self.value))


class EclField(Field):
    def is_valid(self):
        return self.value in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")


class PidField(Field):
    def is_valid(self):
        pattern = re.compile(r"^\d{9}$")
        return bool(pattern.match(self.value))


class CidField(Field):
    def is_valid(self):
        return True


def field_factory(name, value):
    if name == 'byr':
        return ByrField(name, value)
    elif name == 'iyr':
        return IyrField(name, value)
    elif name == 'eyr':
        return EyrField(name, value)
    elif name == 'hgt':
        return HgtField(name, value)
    elif name == 'hcl':
        return HclField(name, value)
    elif name == 'ecl':
        return EclField(name, value)
    elif name == 'pid':
        return PidField(name, value)
    elif name == 'cid':
        return CidField(name, value)

    raise RuntimeError("unknown field: %s" % name)


class Passport:
    def __init__(self, **fields):
        self.fields = [field_factory(name, value) for name, value in fields.items()]
        self.required_fields = (
                "byr",
                "iyr",
                "eyr",
                "hgt",
                "hcl",
                "ecl",
                "pid",
        )
        self.optional_fields = (
                "cid",
        )

    def __repr__(self):
        return pprint.pformat(self.fields)

    @classmethod
    def create_from(cls, key_value_pairs):
        fields = {}
        for kv_pair in key_value_pairs:
            key, value = kv_pair.split(':')
            fields[key] = value

        return cls(**fields)

    def is_valid(self):
        field_names = [field.name for field in self.fields]
        return all(rf in field_names for rf in self.required_fields)

    def all_fields_are_valid(self):
        return all(field.is_valid() for field in self.fields)


if __name__ == '__main__':
    args = parse_args()

    passports = []
    key_value_pairs = []
    lines = sys.stdin.readlines() + ['\n']
    for line in lines:
        if line != '\n':
            key_value_pairs.extend(line.strip('\n').split(' '))
            continue

        passports.append(Passport.create_from(key_value_pairs))
        key_value_pairs = []

    valid_passports = [p for p in passports if p.is_valid()]
    print("part 1: %s" % len(valid_passports))

    valid_passports = [p for p in valid_passports if p.all_fields_are_valid()]
    print("part 2: %s" % len(valid_passports))
