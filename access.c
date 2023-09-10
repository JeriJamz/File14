/*This is a lil evil
Its supposed to restrict access, idk where to put it yet
might put it with my next program
Its supposed to set an enviorment

*/


BOOL CreateRestrictedToken(HANDLE ExisitingTokenHandle, DWORD Flags,
			   DWORD DisableSidCount, PSID_AND_ATTRIBUTES SidToDisable,
			   DWORD DeletePrivilegeCount, PLUID_AND_ATTRIBUTES PrivilegesToDelete,
			   DWORD RestrictedSidCount, PSIDAND_ATTRIBUTES SidsToRestrict,
			   HANDLE NewTokenHandle)