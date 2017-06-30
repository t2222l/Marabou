/*********************                                                        */
/*! \file Debug.h
 ** \verbatim
 ** Top contributors (to current version):
 **   Guy Katz
 ** This file is part of the Marabou project.
 ** Copyright (c) 2016-2017 by the authors listed in the file AUTHORS
 ** in the top-level source directory) and their institutional affiliations.
 ** All rights reserved. See the file COPYING in the top-level source
 ** directory for licensing information.\endverbatim
 **/

#ifndef __Debug_h__
#define __Debug_h__

// #define DEBUG_ON

#ifdef DEBUG_ON
#  define DEBUG(x) x
#else
#  define DEBUG(x)
#endif

#ifdef DEBUG_ON
#  define ASSERTM(x, y)                         \
    {                                           \
        if ( !( x ) )                           \
        {                                       \
            printf( y );                        \
            exit( 1 );                          \
        }                                       \
    }
#else
#  define ASSERTM(x, y)
#endif

#ifdef DEBUG_ON
#  define ASSERT(x)                             \
    {                                           \
        if ( !( x ) )                           \
        {                                       \
            printf( "Assertion violation!\n" ); \
            exit( 1 );                          \
        }                                       \
    }
#else
#  define ASSERT(x)
#endif

#endif // __Debug_h__

//
// Local Variables:
// compile-command: "make -C .. "
// tags-file-name: "../TAGS"
// c-basic-offset: 4
// End:
//
