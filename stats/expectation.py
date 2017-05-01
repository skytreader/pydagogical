#! /usr/bin/env python3

def _cardinality_check(events, p_ev):
    if len(events) != len(p_ev):
        # NOTE should I raise this too if p_ev does not sum up to 1?
        raise ValueError("events and p_ev should have the same cardinality")

def expected_value(events, p_ev):
    _cardinality_check(events, p_ev)
    return sum((x[0] * x[1] for x in zip(events, p_ev)))

def ev_variance(events, p_ev):
    exp_val = expected_value(events, p_ev)
    new_events = tuple(((x - exp_val) ** 2 for x in events))
    return expected_value(new_events, p_ev)
