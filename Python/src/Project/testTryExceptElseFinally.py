#!/usr/bin/env python3

import logging
for i in range(5):
    try:
        assert(1 == i)
        print("try", i)
    except Exception:
        logging.exception("error")
    else:
        assert(1 == 1)
        print("else", i)
    finally:
        print("finally", i, "\n")
print("end")
