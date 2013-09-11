"""Semi-automated code-level dependency tracking for python."""

# Copyright 2011, 2012, 2013 Matt Shannon

# This file is part of codedep.
# See `License` for details of license and warranty.


from codedep.decorators import codeHash, codeDeps, ForwardRef, codedepEvalThunk
from codedep.compute import getHash
