#! /usr/bin/env python3

def _cardinality_check(events, p_ev):
    if len(events) != len(p_ev):
        # NOTE should I raise this too if p_ev does not sum up to 1?
        raise ValueError("events and p_ev should have the same cardinality")

def expected_value(events, p_ev):
    _cardinality_check(events, p_ev)
    return sum((x[0] * x[1] for x in zip(events, p_ev)))
