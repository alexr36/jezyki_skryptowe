from datetime import datetime
import constants as c


class LogParser:
    def __init__(self):
        self.entries = []


    def load(self, filepath):
        self.entries.clear()

        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                if not line.strip():
                    continue

                fields = line.strip().split('\t')

                try:
                    parsed = self.parse_line(fields)
                    self.entries.append(parsed)
                except Exception:
                    continue 


    def parse_line(self, fields):
        return {
            c.TS:                datetime.fromtimestamp(float(fields[0])),
            c.UID:               fields[1],
            c.ID_ORIG_H:         fields[2],
            c.ID_ORIG_P:         int(fields[3]),
            c.ID_RESP_H:         fields[4],
            c.ID_RESP_P:         int(fields[5]),
            c.TRANS_DEPTH:       int(fields[6]),
            c.METHOD:            fields[7],
            c.HOST:              fields[8],
            c.URI:               fields[9],
            c.REFERRER:          fields[10],
            c.USER_AGENT:        fields[11],
            c.REQUEST_BODY_LEN:  int(fields[12]),
            c.RESPONSE_BODY_LEN: int(fields[13]),
            c.STATUS_CODE:       int(fields[14]) if fields[14].isdigit() else None,
            c.STATUS_MSG:        fields[15],
            c.INFO_CODE:         fields[16],
            c.INFO_MSG:          fields[17],
            c.FILENAME:          fields[18],
            c.TAGS:              fields[19],
            c.USERNAME:          fields[20],
            c.PASSWORD:          fields[21],
            c.PROXIED:           fields[22],
            c.ORIG_FUIDS:        fields[23],
            c.ORIG_MIME_TYPES:   fields[24],
            c.RESP_FUIDS:        fields[25],
            c.RESP_MIME_TYPES:   fields[26],
            'raw':               '\t'.join(fields)
        }


    def get_entries(self):
        return self.entries


    def get_entries_between_dates(self, start_str, end_str):
        try:
            start = datetime.strptime(start_str, "%Y-%m-%d")
            end = datetime.strptime(end_str, "%Y-%m-%d")
        except ValueError:
            return []

        return [e for e in self.entries if start <= e[c.TS] <= end]